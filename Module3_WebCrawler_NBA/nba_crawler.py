"""
NBA.com Web Crawler
For MSc Mathematics Students
Demonstrates ethical web crawling with IPO model
"""

import requests
from bs4 import BeautifulSoup
import time
import json
import os
from datetime import datetime


class NBAStatsCrawler:
    """
    Ethical web crawler for NBA.com
    Implements Input-Process-Output model with rate limiting
    """
    
    def __init__(self, output_dir='data'):
        """
        Initialize crawler with configuration
        """
        self.base_url = "https://www.nba.com"
        self.output_dir = output_dir
        self.session = requests.Session()
        
        # Set descriptive User-Agent (ethical practice)
        self.session.headers.update({
            'User-Agent': 'Educational-Crawler-MSc-Math-HKBU/1.0 (Learning Project)'
        })
        
        # Create output directories
        os.makedirs(f"{output_dir}/raw", exist_ok=True)
        os.makedirs(f"{output_dir}/processed", exist_ok=True)
        
        print("✓ NBA Stats Crawler initialized")
    
    def check_robots_txt(self):
        """
        INPUT: Fetch robots.txt
        PROCESS: Parse rules
        OUTPUT: Display allowed/disallowed paths
        """
        print("\n=== Checking robots.txt ===")
        
        # INPUT
        url = f"{self.base_url}/robots.txt"
        
        # PROCESS
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                # OUTPUT
                print(f"✓ robots.txt found at {url}")
                print("\nContent:")
                print("-" * 60)
                print(response.text[:500])  # Show first 500 chars
                print("-" * 60)
                return response.text
            else:
                print(f"✗ Could not fetch robots.txt: {response.status_code}")
                return None
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
    
    def find_sitemaps(self):
        """
        Attempt to discover sitemaps
        """
        print("\n=== Looking for Sitemaps ===")
        
        # Common sitemap locations
        sitemap_urls = [
            f"{self.base_url}/sitemap.xml",
            f"{self.base_url}/sitemap_index.xml",
            f"{self.base_url}/sitemap-players.xml",
            f"{self.base_url}/sitemap-teams.xml"
        ]
        
        found_sitemaps = []
        
        for url in sitemap_urls:
            try:
                response = self.session.get(url, timeout=10)
                if response.status_code == 200:
                    print(f"✓ Found: {url}")
                    found_sitemaps.append(url)
                else:
                    print(f"✗ Not found: {url}")
                time.sleep(1)  # Rate limiting
            except Exception as e:
                print(f"✗ Error accessing {url}: {e}")
        
        return found_sitemaps
    
    def crawl_page(self, url, save_html=True):
        """
        Crawl a single page using IPO model
        
        INPUT: URL to crawl
        PROCESS: Fetch, parse, extract
        OUTPUT: Structured data
        """
        print(f"\nCrawling: {url}")
        
        # ===== INPUT =====
        start_time = time.time()
        
        # ===== PROCESS =====
        try:
            # Step 1: HTTP Request
            response = self.session.get(url, timeout=15)
            
            if response.status_code != 200:
                print(f"✗ Error: HTTP {response.status_code}")
                return None
            
            # Step 2: Parse HTML
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Step 3: Extract metadata
            title = soup.title.string if soup.title else 'No title'
            tables = soup.find_all('table')
            links = soup.find_all('a')
            
            # Step 4: Extract data-specific content
            data = {
                'url': url,
                'title': title,
                'crawled_at': datetime.now().isoformat(),
                'status_code': response.status_code,
                'num_tables': len(tables),
                'num_links': len(links),
                'content_length': len(response.content),
                'crawl_time_seconds': time.time() - start_time
            }
            
            # ===== OUTPUT =====
            print(f"✓ Success: {title}")
            print(f"  - Tables found: {len(tables)}")
            print(f"  - Links found: {len(links)}")
            print(f"  - Time: {data['crawl_time_seconds']:.2f}s")
            
            # Save raw HTML if requested
            if save_html:
                filename = url.replace('https://', '').replace('/', '_') + '.html'
                filepath = f"{self.output_dir}/raw/{filename}"
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(response.text)
                print(f"  - Saved HTML to: {filepath}")
            
            return data
            
        except requests.exceptions.Timeout:
            print("✗ Request timed out")
            return None
        except Exception as e:
            print(f"✗ Error: {e}")
            return None
        finally:
            # IMPORTANT: Rate limiting (ethical crawling)
            time.sleep(2)  # Wait 2 seconds between requests
    
    def crawl_multiple(self, urls, max_pages=None):
        """
        Crawl multiple pages and aggregate results
        
        INPUT: List of URLs
        PROCESS: Crawl each page
        OUTPUT: Aggregated data
        """
        print("\n" + "=" * 60)
        print("Starting Multi-Page Crawl")
        print("=" * 60)
        
        if max_pages:
            urls = urls[:max_pages]
            print(f"Limiting to {max_pages} pages")
        
        results = []
        
        for i, url in enumerate(urls, 1):
            print(f"\n[{i}/{len(urls)}]", end=" ")
            data = self.crawl_page(url)
            
            if data:
                results.append(data)
        
        # Save results
        output_file = f"{self.output_dir}/processed/crawl_results.json"
        with open(output_file, 'w') as f:
            json.dump(results, f, indent=2)
        
        print("\n" + "=" * 60)
        print(f"✓ Crawl complete: {len(results)}/{len(urls)} successful")
        print(f"✓ Results saved to: {output_file}")
        print("=" * 60)
        
        return results
    
    def extract_player_data(self, html_content):
        """
        Extract player statistics from HTML
        (This is a template - actual selectors depend on NBA.com structure)
        
        INPUT: HTML content
        PROCESS: Parse and extract player data
        OUTPUT: List of player dictionaries
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        players = []
        
        # Note: These selectors are examples and may need adjustment
        # based on actual NBA.com HTML structure
        
        # Find stats table
        table = soup.find('table', {'class': 'stats'})
        
        if not table:
            print("No player stats table found")
            return players
        
        rows = table.find_all('tr')[1:]  # Skip header
        
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 5:
                try:
                    player = {
                        'name': cols[0].text.strip(),
                        'team': cols[1].text.strip(),
                        'points': float(cols[2].text.strip()),
                        'rebounds': float(cols[3].text.strip()),
                        'assists': float(cols[4].text.strip())
                    }
                    players.append(player)
                except (ValueError, IndexError) as e:
                    print(f"Error parsing row: {e}")
                    continue
        
        return players
    
    def generate_report(self, results):
        """
        Generate summary report
        
        INPUT: Crawl results
        PROCESS: Analyze and summarize
        OUTPUT: Report text
        """
        if not results:
            return "No data to report"
        
        total_pages = len(results)
        total_tables = sum(r['num_tables'] for r in results)
        total_links = sum(r['num_links'] for r in results)
        avg_time = sum(r['crawl_time_seconds'] for r in results) / total_pages
        
        report = f"""
NBA Web Crawler Report
{'=' * 60}

Summary:
- Pages crawled: {total_pages}
- Total tables found: {total_tables}
- Total links found: {total_links}
- Average crawl time: {avg_time:.2f} seconds

Crawled URLs:
"""
        for i, result in enumerate(results, 1):
            report += f"{i}. {result['title']} ({result['num_tables']} tables)\n"
        
        report += f"\n{'=' * 60}\n"
        
        return report


# ===================================================================
# Main Execution
# ===================================================================

def main():
    """
    Example usage of NBA Stats Crawler
    """
    print("NBA.com Web Crawler - Educational Project")
    print("=" * 60)
    
    # Initialize crawler
    crawler = NBAStatsCrawler(output_dir='data')
    
    # Step 1: Check robots.txt (IMPORTANT!)
    crawler.check_robots_txt()
    
    # Step 2: Find sitemaps
    sitemaps = crawler.find_sitemaps()
    
    # Step 3: Define URLs to crawl
    # Note: Adjust these based on actual NBA.com structure
    # and what robots.txt allows
    urls_to_crawl = [
        "https://www.nba.com",
        "https://www.nba.com/stats",
    ]
    
    # Step 4: Crawl pages (limit to 3 for demo)
    results = crawler.crawl_multiple(urls_to_crawl, max_pages=3)
    
    # Step 5: Generate report
    report = crawler.generate_report(results)
    print("\n" + report)
    
    # Save report
    with open('data/processed/crawl_report.txt', 'w') as f:
        f.write(report)
    
    print("\n✓ All done! Check the 'data' folder for results.")


if __name__ == "__main__":
    main()

