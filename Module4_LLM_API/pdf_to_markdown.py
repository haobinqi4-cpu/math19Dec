"""
Convert PDF to Markdown and format using LLM API
"""

import PyPDF2
import os
from llm_client import HKBUGenAIClient

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text() + "\n\n"
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None
    return text

def chunk_text(text, max_chunk_size=3000):
    """Split text into chunks for LLM processing"""
    paragraphs = text.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        if len(current_chunk) + len(paragraph) <= max_chunk_size:
            current_chunk += paragraph + "\n\n"
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph + "\n\n"
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def format_with_llm(client, text_chunk, chunk_num, total_chunks):
    """Format text chunk using LLM"""
    prompt = f"""
Please convert the following academic text to well-formatted Markdown. 
This is chunk {chunk_num} of {total_chunks}.

Formatting requirements:
1. Preserve all mathematical formulas and equations
2. Convert section headings to appropriate Markdown headers (#, ##, ###)
3. Format lists as bullet points or numbered lists
4. Preserve all citations and references
5. Make tables readable if present
6. Keep all technical content accurate

Text to format:
{text_chunk}
"""
    
    system_message = """
You are an expert academic editor specializing in converting PDF text to clean, 
well-formatted Markdown while preserving all technical content accurately.
"""
    
    try:
        formatted_text = client.chat(
            prompt=prompt,
            system_message=system_message,
            temperature=0.3,
            max_tokens=2000
        )
        return formatted_text
    except Exception as e:
        print(f"Error formatting chunk {chunk_num}: {e}")
        return text_chunk  # Return original text if formatting fails

def combine_markdown_chunks(chunks, output_path):
    """Combine formatted chunks into a single Markdown file"""
    with open(output_path, 'w', encoding='utf-8') as f:
        # Add a header
        f.write("# Converted Academic Paper\n\n")
        f.write("> Automatically converted from PDF to Markdown\n\n")
        f.write("---\n\n")
        
        # Add all chunks
        for i, chunk in enumerate(chunks, 1):
            f.write(f"\n\n<!-- Chunk {i} -->\n\n")
            f.write(chunk)
            f.write("\n\n---\n")

def main():
    # File paths
    pdf_path = "/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Data/Small Sample Methods for Multilevel Modeling  A Colloquial Elucidation of REML and the Kenward-Roger Correction.pdf"
    output_path = "/Users/simonwang/Documents/Usage/MathAI/MscMinicourse/Module4_LLM_API/converted_paper.md"
    
    print("Starting PDF to Markdown conversion...")
    print(f"PDF Path: {pdf_path}")
    print(f"Output Path: {output_path}")
    
    # Step 1: Extract text from PDF
    print("\n1. Extracting text from PDF...")
    raw_text = extract_text_from_pdf(pdf_path)
    
    if not raw_text:
        print("Failed to extract text from PDF")
        return
    
    print(f"Extracted {len(raw_text)} characters from PDF")
    
    # Step 2: Split text into chunks
    print("\n2. Splitting text into chunks...")
    chunks = chunk_text(raw_text)
    print(f"Split into {len(chunks)} chunks")
    
    # Step 3: Initialize LLM client
    print("\n3. Initializing LLM client...")
    try:
        client = HKBUGenAIClient()
    except Exception as e:
        print(f"Error initializing LLM client: {e}")
        print("Please ensure your API key is set in the HKBU_GENAI_API_KEY environment variable")
        return
    
    # Step 4: Format each chunk with LLM
    print("\n4. Formatting chunks with LLM...")
    formatted_chunks = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"   Formatting chunk {i}/{len(chunks)}...")
        formatted_chunk = format_with_llm(client, chunk, i, len(chunks))
        formatted_chunks.append(formatted_chunk)
    
    # Step 5: Combine chunks into final Markdown file
    print("\n5. Combining chunks into final Markdown file...")
    combine_markdown_chunks(formatted_chunks, output_path)
    
    print(f"\n✅ Conversion complete!")
    print(f"✅ Output saved to: {output_path}")
    print(f"📊 Statistics:")
    print(f"   - PDF pages processed: Unknown (PyPDF2 limitation)")
    print(f"   - Text chunks formatted: {len(chunks)}")
    print(f"   - Output file size: {os.path.getsize(output_path)} bytes")

if __name__ == "__main__":
    main()