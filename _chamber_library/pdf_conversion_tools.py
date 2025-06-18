#!/usr/bin/env python3
"""
PDF to Markdown Conversion Tools
Multiple approaches for converting PDFs when pandoc fails
"""

import subprocess
import tempfile
from pathlib import Path
import shutil

def check_available_tools():
    """Check which PDF conversion tools are available"""
    tools = {
        'pandoc': False,
        'pdftotext': False,
        'pdfplumber': False,
        'pypdf2': False,
        'pymupdf': False,
        'pdf2txt': False
    }
    
    # Check command-line tools
    for tool in ['pandoc', 'pdftotext', 'pdf2txt.py']:
        try:
            subprocess.run([tool, '--help'], capture_output=True, timeout=5)
            if tool == 'pdftotext':
                tools['pdftotext'] = True
            elif tool == 'pdf2txt.py':
                tools['pdf2txt'] = True
            else:
                tools[tool] = True
        except:
            pass
    
    # Check Python packages
    try:
        import pdfplumber
        tools['pdfplumber'] = True
    except ImportError:
        pass
    
    try:
        import PyPDF2
        tools['pypdf2'] = True
    except ImportError:
        pass
    
    try:
        import fitz  # PyMuPDF
        tools['pymupdf'] = True
    except ImportError:
        pass
    
    return tools

def convert_pdf_with_pdftotext(pdf_path, output_path):
    """Convert PDF using pdftotext (part of poppler-utils)"""
    try:
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
            temp_txt = Path(temp_file.name)
        
        # Extract text with pdftotext
        subprocess.run([
            'pdftotext', 
            '-layout',  # Preserve layout
            '-nopgbrk',  # No page breaks
            str(pdf_path),
            str(temp_txt)
        ], check=True)
        
        # Read extracted text
        with open(temp_txt, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # Clean up temp file
        temp_txt.unlink()
        
        # Convert to basic markdown
        markdown = convert_text_to_markdown(text)
        
        # Write to output
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        return True
        
    except Exception as e:
        print(f"pdftotext conversion failed: {e}")
        return False

def convert_pdf_with_pdfplumber(pdf_path, output_path):
    """Convert PDF using pdfplumber Python library"""
    try:
        import pdfplumber
        
        text_content = []
        
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_content.append(text)
        
        full_text = '\n\n'.join(text_content)
        markdown = convert_text_to_markdown(full_text)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        return True
        
    except Exception as e:
        print(f"pdfplumber conversion failed: {e}")
        return False

def convert_pdf_with_pymupdf(pdf_path, output_path):
    """Convert PDF using PyMuPDF (fitz)"""
    try:
        import fitz
        
        doc = fitz.open(pdf_path)
        text_content = []
        
        for page_num in range(doc.page_count):
            page = doc[page_num]
            text = page.get_text()
            if text.strip():
                text_content.append(text)
        
        doc.close()
        
        full_text = '\n\n'.join(text_content)
        markdown = convert_text_to_markdown(full_text)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        
        return True
        
    except Exception as e:
        print(f"PyMuPDF conversion failed: {e}")
        return False

def convert_text_to_markdown(text):
    """Convert plain text to basic markdown format"""
    import re
    
    lines = text.split('\n')
    markdown_lines = []
    
    for line in lines:
        line = line.strip()
        
        if not line:
            markdown_lines.append('')
            continue
        
        # Detect headings (all caps, short lines, etc.)
        if (line.isupper() and len(line) < 80 and 
            not line.startswith(('PAGE', 'CHAPTER', 'SECTION')) and
            len(line.split()) > 1):
            markdown_lines.append(f"## {line.title()}")
        
        # Detect chapter/section markers
        elif re.match(r'^(CHAPTER|SECTION|PART)\s+\d+', line, re.IGNORECASE):
            markdown_lines.append(f"# {line.title()}")
        
        # Regular paragraph
        else:
            markdown_lines.append(line)
    
    return '\n'.join(markdown_lines)

def convert_pdf_multi_method(pdf_path, output_dir, title, author):
    """Try multiple methods to convert PDF"""
    from convert_epub import sanitize_filename, map_author_to_voice, determine_quote_style
    import yaml
    from datetime import datetime
    
    pdf_path = Path(pdf_path)
    output_dir = Path(output_dir)
    
    # Create output filename
    safe_name = sanitize_filename(pdf_path.name)
    output_file = output_dir / f"{safe_name}.md"
    
    print(f"Converting PDF: {title}")
    print(f"Trying multiple conversion methods...")
    
    # Check available tools
    tools = check_available_tools()
    print(f"Available tools: {[k for k, v in tools.items() if v]}")
    
    # Try methods in order of preference
    methods = [
        ('pdftotext', convert_pdf_with_pdftotext, tools['pdftotext']),
        ('pdfplumber', convert_pdf_with_pdfplumber, tools['pdfplumber']),
        ('pymupdf', convert_pdf_with_pymupdf, tools['pymupdf'])
    ]
    
    success = False
    method_used = None
    
    for method_name, method_func, available in methods:
        if not available:
            print(f"  ❌ {method_name}: not available")
            continue
        
        print(f"  🔄 Trying {method_name}...")
        
        try:
            if method_func(pdf_path, output_file):
                print(f"  ✅ Success with {method_name}")
                method_used = method_name
                success = True
                break
            else:
                print(f"  ❌ {method_name}: conversion failed")
        except Exception as e:
            print(f"  ❌ {method_name}: {str(e)[:50]}")
    
    if not success:
        print(f"  ❌ All conversion methods failed")
        return False
    
    # Add YAML frontmatter to the converted file
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create Chamber voice mapping
        voice_name = map_author_to_voice(author)
        quote_style = determine_quote_style(author)
        
        # Create YAML frontmatter
        frontmatter = {
            'title': title,
            'author': author,
            'voice': voice_name,
            'canonical': True,
            'source_format': 'pdf',
            'converted_with': method_used,
            'date_converted': datetime.now().strftime('%Y-%m-%d'),
            'segment_strategy': 'chapter',
            'file': output_file.name,
            'tags': [],
            'quote_style': quote_style,
            'conversion_note': f'Converted from PDF using {method_used}'
        }
        
        # Write with YAML frontmatter
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')
            f.write(content)
        
        print(f"  ✅ YAML frontmatter added")
        return True
        
    except Exception as e:
        print(f"  ⚠️  Warning: Could not add frontmatter: {e}")
        return True  # Still count as success since content was converted

def install_pdf_tools():
    """Provide instructions for installing PDF conversion tools"""
    print("📦 PDF CONVERSION TOOLS INSTALLATION")
    print("=" * 50)
    print()
    print("To enable PDF conversion, install these tools:")
    print()
    print("🍺 Using Homebrew (macOS):")
    print("  brew install poppler          # for pdftotext")
    print("  pip3 install pdfplumber       # Python PDF library")
    print("  pip3 install PyMuPDF          # Alternative PDF library")
    print()
    print("🐧 Using apt (Ubuntu/Debian):")
    print("  sudo apt install poppler-utils")
    print("  pip3 install pdfplumber")
    print("  pip3 install PyMuPDF")
    print()
    print("📋 After installation, run this script again")

def test_pdf_conversion():
    """Test PDF conversion with Chamber files"""
    
    test_files = [
        {
            'path': "/Users/davidglidden/Desktop/for the chamber/The Arcades Project (Walter Benjamin).pdf",
            'title': 'The Arcades Project',
            'author': 'Walter Benjamin'
        },
        {
            'path': "/Users/davidglidden/Desktop/for the chamber/Totality and Infinity An Essay on Ext....pdf", 
            'title': 'Totality and Infinity',
            'author': 'Emmanuel Levinas'
        },
        {
            'path': "/Users/davidglidden/Desktop/for the chamber/The Need for Roots Prelude to a Decla.pdf",
            'title': 'The Need for Roots',
            'author': 'Simone Weil'
        }
    ]
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print("🏛️ TESTING PDF CONVERSION FOR CHAMBER")
    print("=" * 50)
    
    # Check tools first
    tools = check_available_tools()
    available_tools = [k for k, v in tools.items() if v]
    
    if not available_tools:
        install_pdf_tools()
        return
    
    print(f"Available conversion tools: {', '.join(available_tools)}")
    print()
    
    successful = 0
    failed = 0
    
    for i, file_info in enumerate(test_files, 1):
        file_path = Path(file_info['path'])
        
        print(f"[{i}/{len(test_files)}] {file_info['author']}")
        print(f"           {file_info['title']}")
        
        if not file_path.exists():
            print(f"           ❌ File not found")
            failed += 1
            continue
        
        if convert_pdf_multi_method(file_path, output_dir, file_info['title'], file_info['author']):
            successful += 1
            print(f"           ✅ PDF conversion successful")
        else:
            failed += 1
            print(f"           ❌ PDF conversion failed")
        print()
    
    print(f"📊 PDF CONVERSION RESULTS:")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    
    if successful > 0:
        print(f"\n🎉 PDF conversion is working!")
        print(f"🏛️ Critical Chamber voices can now be activated from PDFs")
        print(f"📄 Run: python3 analyze_library.py to see updated status")
    
    return successful > 0

if __name__ == "__main__":
    print("🔧 PDF TO MARKDOWN CONVERSION TOOLKIT")
    print("=" * 50)
    
    # Check what's available
    tools = check_available_tools()
    print(f"Available tools: {[k for k, v in tools.items() if v]}")
    
    if not any(tools.values()):
        install_pdf_tools()
    else:
        print("\n🧪 Testing PDF conversion...")
        test_pdf_conversion()