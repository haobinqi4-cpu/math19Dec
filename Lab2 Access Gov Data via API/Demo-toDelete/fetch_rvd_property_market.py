#!/usr/bin/env python3
"""Fetch a data.gov.hk resource (CKAN) by resource id or dataset resource URL,
download a small sample, and generate a markdown report next to this script.

Usage:
    python fetch_rvd_property_market.py [resource-id-or-url]

If no argument is given, the default resource URL from the lab instruction will be used.
"""
import io
import json
import os
import re
import sys
from typing import Optional

import pandas as pd
import requests
from urllib.parse import urljoin
import zipfile
import xml.etree.ElementTree as ET
from typing import List, Dict


DEFAULT_RESOURCE_URL = (
    "https://data.gov.hk/en-data/dataset/hk-rvd-tsinfo_rvd-property-market-statistics/resource/"
    "d8ecc5e6-3721-4d07-a0f2-163f08e39b89"
)


def extract_resource_id(s: str) -> Optional[str]:
    # match UUID-looking segment after /resource/
    m = re.search(r"/resource/([0-9a-fA-F\-]{36})", s)
    if m:
        return m.group(1)
    # if the user passed only the id
    if re.fullmatch(r"[0-9a-fA-F\-]{36}", s):
        return s
    return None


def get_resource_metadata(resource_id: str) -> dict:
    # Try known CKAN endpoints; some datasets use '/en-data/api/3/action/'
    endpoints = [
        f"https://data.gov.hk/api/3/action/resource_show?id={resource_id}",
        f"https://data.gov.hk/en-data/api/3/action/resource_show?id={resource_id}",
    ]
    last_err = None
    for api in endpoints:
        try:
            r = requests.get(api, timeout=20)
            r.raise_for_status()
            payload = r.json()
            if payload.get("success"):
                return payload["result"]
            last_err = RuntimeError("CKAN API did not return success for resource_show")
        except Exception as e:
            last_err = e
    # if we reach here, raise the last error or a generic RuntimeError
    if last_err:
        raise last_err
    raise RuntimeError("Could not contact CKAN resource_show endpoints")


def extract_dataset_id_from_url(s: str) -> Optional[str]:
    m = re.search(r"/dataset/([^/\?#]+)", s)
    if m:
        return m.group(1)
    return None


def get_package_metadata(package_id_or_name: str) -> dict:
    """Fetch package_show (dataset) metadata from CKAN. Tries both localized and default endpoints."""
    endpoints = [
        f"https://data.gov.hk/api/3/action/package_show?id={package_id_or_name}",
        f"https://data.gov.hk/en-data/api/3/action/package_show?id={package_id_or_name}",
    ]
    last_err = None
    for api in endpoints:
        try:
            r = requests.get(api, timeout=30)
            r.raise_for_status()
            payload = r.json()
            if payload.get("success"):
                return payload["result"]
            last_err = RuntimeError("CKAN API did not return success for package_show")
        except Exception as e:
            last_err = e
    if last_err:
        raise last_err
    raise RuntimeError("Could not contact CKAN package_show endpoints")


def generate_resources_report(folder: str, package_meta: dict) -> str:
    """Generate a markdown report summarizing all resources in the package/dataset."""
    lines = []
    title = package_meta.get("title") or package_meta.get("name") or "Dataset resources"
    lines.append(f"# Resources Report — {title}")
    lines.append("")
    resources = package_meta.get("resources", []) if package_meta else []
    lines.append(f"- dataset id: {package_meta.get('id')}")
    lines.append(f"- resources found: {len(resources)}")
    lines.append("")
    lines.append("## Resource list")
    lines.append("")
    # build table rows
    header = ["index", "id", "name", "format", "url", "last_modified", "size", "description"]
    rows = []
    for i, r in enumerate(resources, start=1):
        rows.append([
            i,
            r.get("id") or "",
            (r.get("name") or r.get("title") or "").replace("\n", " "),
            r.get("format") or "",
            r.get("url") or r.get("download_url") or "",
            r.get("last_modified") or r.get("created") or "",
            r.get("size") or r.get("bytes") or "",
            (r.get("description") or "").replace("\n", " ")[:300],
        ])

    # attempt to use pandas to format as markdown (pandas is available)
    try:
        df = pd.DataFrame(rows, columns=header)
        md = df.to_markdown(index=False)
        lines.append(md)
    except Exception:
        # fallback plain text
        for row in rows:
            lines.append(" | ".join([str(x) for x in row]))

    out = "\n".join(lines)
    out_path = os.path.join(folder, "testAPI_resources_report.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    return out_path


def sample_csv_resources(folder: str, package_meta: dict, max_resources: int = 10, max_rows: int = 5) -> str:
    """Download up to max_resources CSV resources from the package and write a samples markdown file.
    Returns the path to the generated samples file.
    """
    resources = package_meta.get("resources", []) if package_meta else []
    samples_lines = []
    samples_lines.append(f"# Resource samples — {package_meta.get('title') or package_meta.get('name')}")
    samples_lines.append("")
    count = 0
    for r in resources:
        if count >= max_resources:
            break
        fmt = (r.get("format") or "").lower()
        url = r.get("url") or r.get("download_url")
        if not url:
            continue
        if fmt not in ("csv", "xls", "xlsx") and ".csv" not in url.lower():
            continue
        # attempt to download and parse CSV
        samples_lines.append(f"## Resource {count+1}: {r.get('name')}")
        samples_lines.append("")
        samples_lines.append(f"- id: {r.get('id')}")
        samples_lines.append(f"- url: {url}")
        samples_lines.append("")
        try:
            b = download_resource(url, max_bytes=2_000_000)
            text = b.decode("utf-8", errors="replace")
            try:
                df = pd.read_csv(io.StringIO(text), nrows=max_rows)
                samples_lines.append(df.to_markdown(index=False))
            except Exception:
                # try reading as excel if not CSV
                try:
                    import tempfile

                    with open("/tmp/_tmp_resource.xls", "wb") as fh:
                        fh.write(b)
                    df = pd.read_excel("/tmp/_tmp_resource.xls", nrows=max_rows)
                    samples_lines.append(df.to_markdown(index=False))
                except Exception:
                    samples_lines.append("Could not parse sample from this resource; binary or unsupported format.")
        except Exception as e:
            samples_lines.append(f"Failed to download resource: {e}")
        samples_lines.append("")
        count += 1

    out_path = os.path.join(folder, "testAPI_samples.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write("\n".join(samples_lines))
    return out_path


def download_resource(url: str, max_bytes: int = 10_000_000) -> bytes:
    # stream download but cap to max_bytes for safety
    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()
    content = bytearray()
    for chunk in resp.iter_content(chunk_size=8192):
        if chunk:
            content.extend(chunk)
        if len(content) >= max_bytes:
            break
    return bytes(content)


def looks_like_text(b: bytes, threshold: float = 0.9) -> bool:
    """Return True if a bytes object appears to be mostly UTF-8-decodable text.
    threshold is fraction of printable characters required.
    """
    if not b:
        return True
    # quick check for common binary signatures
    if b.startswith(b"PK") or b.startswith(b"\x1f\x8b"):
        return False
    try:
        txt = b.decode("utf-8")
    except Exception:
        return False
    # fraction printable
    printable = sum(1 for ch in txt if ch.isprintable() or ch.isspace())
    return (printable / max(1, len(txt))) >= threshold


def extract_first_text_from_zip(b: bytes) -> Dict[str, str]:
    """Return dict with keys: file_list (comma sep) and text of first .gml/.xml/.txt file found.
    If none found, returns file_list and empty text.
    """
    res = {"file_list": "", "text": ""}
    try:
        with zipfile.ZipFile(io.BytesIO(b)) as z:
            names = z.namelist()
            res["file_list"] = ", ".join(names)
            # prefer gml or xml
            for ext in (".gml", ".xml", ".txt", ".json", ".csv"):
                for name in names:
                    if name.lower().endswith(ext):
                        with z.open(name) as fh:
                            raw = fh.read()
                            try:
                                text = raw.decode("utf-8")
                            except Exception:
                                text = raw.decode("utf-8", errors="replace")
                            res["text"] = text
                            return res
            # otherwise read first file as text fallback
            if names:
                with z.open(names[0]) as fh:
                    raw = fh.read()
                    try:
                        text = raw.decode("utf-8")
                    except Exception:
                        text = raw.decode("utf-8", errors="replace")
                    res["text"] = text
    except Exception:
        pass
    return res


def parse_gml_infer_fields_and_samples(text: str, max_features: int = 10):
    """Parse a GML/XML string and return a list of inferred field names and sample rows.
    This is heuristic-based: it finds candidate feature elements (those having child elements with text)
    and extracts their child tags as fields.
    """
    fields = []
    samples: List[Dict[str, str]] = []
    try:
        root = ET.fromstring(text)
    except Exception:
        return fields, samples

    # helper to get local-name
    def local(tag: str) -> str:
        return tag.split("}")[-1] if "}" in tag else tag

    # find candidate feature parents: elements that have children with text and not just gml wrapper tags
    candidates = []
    for elem in root.iter():
        child_texts = [c for c in list(elem) if (c.text and c.text.strip())]
        if child_texts:
            # skip generic GML containers
            name = local(elem.tag).lower()
            if name in ("featurecollection", "featuremembers", "features", "gml:featurecollection"):
                continue
            candidates.append(elem)
            if len(candidates) >= max_features:
                break

    if not candidates:
        # fallback: try deeper search for elements named like '*feature*'
        for elem in root.iter():
            if "feature" in local(elem.tag).lower():
                candidates.append(elem)
            if len(candidates) >= max_features:
                break

    # collect fields from candidates
    field_set = []
    for cand in candidates:
        row = {}
        for c in list(cand):
            key = local(c.tag)
            val = (c.text or "").strip()
            row[key] = val
            if key not in field_set:
                field_set.append(key)
        samples.append(row)

    return field_set, samples


def find_download_link_from_page(page_url: str) -> Optional[str]:
    """Fetch an HTML page and heuristically find a CSV/JSON download link."""
    try:
        r = requests.get(page_url, timeout=20)
        r.raise_for_status()
    except Exception:
        return None
    html = r.text
    # find hrefs
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', html)
    candidates = []
    for h in hrefs:
        low = h.lower()
        # prefer direct file links or filestore/resource download links
        if "download-queue" in low:
            continue
        if ".csv" in low or ".json" in low or "/filestore/" in low or ("/resource/" in low and "download" in low) or "/download?" in low:
            candidates.append(h)
    if not candidates:
        return None
    # convert to absolute and prefer the first candidate
    first = candidates[0]
    return urljoin(page_url, first)


def generate_report(folder: str, metadata: dict, sample_df: Optional[pd.DataFrame], sample_text: str, inferred_fields=None, inferred_samples=None) -> str:
    lines = []
    lines.append(f"# Report — RVD Property Market Resource")
    lines.append("")
    lines.append("## Resource metadata")
    lines.append("")
    for k in ["id", "name", "format", "url", "package_id", "last_modified"]:
        if k in metadata:
            lines.append(f"- **{k}**: {metadata.get(k)}")
    lines.append("")
    lines.append("## Notes on retrieval")
    lines.append("")
    lines.append(f"- Retrieved using CKAN resource_show for id `{metadata.get('id')}`.")
    lines.append("")
    lines.append("## Fields / Schema (inferred)")
    lines.append("")
    if inferred_fields:
        for c in inferred_fields:
            lines.append(f"- {c}")
    elif sample_df is not None:
        cols = list(sample_df.columns)
        for c in cols:
            lines.append(f"- {c}")
    else:
        # If sample_text is empty (likely binary), say so
        if not sample_text:
            lines.append("No tabular sample could be parsed; the downloaded resource appears to be a binary archive or non-text format. See notes above for file list or URL.")
        else:
            lines.append("No tabular sample could be parsed; see raw sample below.")
    lines.append("")
    lines.append("## Sample rows")
    lines.append("")
    if inferred_samples:
        # render inferred samples as a markdown table
        try:
            import tabulate
            # build rows with union of fields
            all_fields = inferred_fields or []
            rows = []
            for s in inferred_samples[:10]:
                rows.append([s.get(f, "") for f in all_fields])
            md = tabulate.tabulate(rows, headers=all_fields, tablefmt="github")
            lines.append(md)
        except Exception:
            # fallback simple text
            for s in inferred_samples[:10]:
                lines.append(str(s))
    elif sample_df is not None:
        # include the top rows as a markdown table
        try:
            md_table = sample_df.head(10).to_markdown(index=False)
            lines.append(md_table)
        except Exception:
            lines.append("Could not render sample as table; showing raw text sample below.")
            lines.append("```")
            lines.append(sample_text[:10000])
            lines.append("```")
    else:
        if sample_text:
            lines.append("```")
            lines.append(sample_text[:10000])
            lines.append("```")
        else:
            lines.append("- (no text sample available; resource likely binary or compressed)")

    out = "\n".join(lines)
    out_path = os.path.join(folder, "testAPI_report.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    return out_path


def main(argv):
    arg = argv[1] if len(argv) > 1 else DEFAULT_RESOURCE_URL

    resource_id = extract_resource_id(arg)
    metadata = None
    resource_url = None
    if resource_id:
        print(f"Found resource id: {resource_id}")
        try:
            metadata = get_resource_metadata(resource_id)
            resource_url = metadata.get("url")
        except requests.HTTPError as e:
            print("CKAN resource_show failed (HTTP error):", e)
            # fallback: try finding a link in the provided page (arg)
            resource_url = find_download_link_from_page(arg)
            if resource_url:
                print("Found candidate download link on the page:", resource_url)
        except Exception as e:
            print("CKAN resource_show failed:", e)
            resource_url = find_download_link_from_page(arg)
    else:
        print("No resource id detected; treating argument as direct URL")
        resource_url = arg

    # If we have dataset context (package_id from resource metadata) or the user passed a dataset URL,
    # fetch package metadata (list of resources) and write a resources report first.
    folder = os.path.dirname(os.path.abspath(__file__))
    package_meta = None
    try:
        pkg_id = None
        if metadata and metadata.get("package_id"):
            pkg_id = metadata.get("package_id")
        else:
            ds = extract_dataset_id_from_url(arg)
            if ds:
                pkg_id = ds
        if pkg_id:
            print(f"Fetching package metadata for: {pkg_id}")
            try:
                package_meta = get_package_metadata(pkg_id)
                outp = generate_resources_report(folder, package_meta)
                print(f"Wrote resources report to: {outp}")
                # produce CSV samples for top resources (prefer CSV formats)
                try:
                    samples_path = sample_csv_resources(folder, package_meta, max_resources=10, max_rows=5)
                    print(f"Wrote resource samples to: {samples_path}")
                except Exception as e:
                    print("Failed to sample CSV resources:", e)
            except Exception as e:
                print("Failed to fetch package metadata:", e)
    except Exception:
        pass

    if not resource_url:
        raise RuntimeError("Could not determine a resource download URL")

    print(f"Attempting to download resource from: {resource_url}")
    raw = download_resource(resource_url)

    sample_df = None
    sample_text = ""
    inferred_fields = None
    inferred_samples = None

    # handle ZIP (PK), gzip, or plain text
    if raw.startswith(b"PK"):
        print("Resource appears to be a ZIP archive; attempting to inspect contents")
        zinfo = extract_first_text_from_zip(raw)
        sample_text = zinfo.get("text", "")
        file_list = zinfo.get("file_list", "")
        print("ZIP contains:", file_list)
        # try parse extracted text as CSV/JSON/XML
        if sample_text:
            try:
                sample_df = pd.read_csv(io.StringIO(sample_text), nrows=100)
                print("Parsed extracted file as CSV with columns:", list(sample_df.columns)[:10])
            except Exception:
                try:
                    js = json.loads(sample_text)
                    if isinstance(js, list) and js:
                        sample_df = pd.DataFrame(js[:100])
                        print("Parsed extracted file as JSON list -> DataFrame")
                except Exception:
                            # try GML/XML parsing
                            fields, samples = parse_gml_infer_fields_and_samples(sample_text)
                            if fields:
                                inferred_fields = fields
                                inferred_samples = samples
                                print("Inferred fields from GML/XML:", fields[:10])
    elif raw.startswith(b"\x1f\x8b"):
        # gzip
        try:
            import gzip

            with gzip.GzipFile(fileobj=io.BytesIO(raw)) as gz:
                txt = gz.read().decode("utf-8", errors="replace")
                sample_text = txt
                try:
                    sample_df = pd.read_csv(io.StringIO(sample_text), nrows=100)
                    print("Parsed gzip-extracted text as CSV")
                except Exception:
                    try:
                        js = json.loads(sample_text)
                        if isinstance(js, list) and js:
                            sample_df = pd.DataFrame(js[:100])
                            print("Parsed gzip-extracted text as JSON -> DataFrame")
                    except Exception:
                            fields, samples = parse_gml_infer_fields_and_samples(sample_text)
                            if fields:
                                inferred_fields = fields
                                inferred_samples = samples
                                print("Inferred fields from GML/XML in gzip:", fields[:10])
        except Exception:
            print("Failed to decompress gzip resource; will include binary info in report")
    else:
        # plain text attempt
        try:
            sample_text = raw.decode("utf-8", errors="replace")
        except Exception:
            sample_text = ""

        # try parse as CSV
        try:
            sample_df = pd.read_csv(io.StringIO(sample_text), nrows=100)
            print("Parsed sample as CSV with columns:", list(sample_df.columns)[:10])
        except Exception:
            # try json
            try:
                js = json.loads(sample_text)
                # if it's a list of dicts
                if isinstance(js, list) and js:
                    sample_df = pd.DataFrame(js[:100])
                    print("Parsed sample as JSON list -> DataFrame")
            except Exception:
                # try XML/GML
                fields, samples = parse_gml_infer_fields_and_samples(sample_text)
                if fields:
                    inferred_fields = fields
                    inferred_samples = samples
                    print("Inferred fields from GML/XML:", fields[:10])

    folder = os.path.dirname(os.path.abspath(__file__))
    out_path = generate_report(folder, metadata or {}, sample_df, sample_text, inferred_fields=inferred_fields, inferred_samples=inferred_samples)
    print(f"Wrote report to: {out_path}")


if __name__ == "__main__":
    main(sys.argv)
