#!/usr/bin/env python3
"""
Chamber Library Batch Conversion
Process larger batches of EPUB files with progress tracking and error handling
"""

import sys
from pathlib import Path
from convert_epub import convert_epub_to_markdown
import time

def batch_convert(batch_size=20, start_from=0):
    """Convert EPUBs in batches with progress tracking"""
    source_dir = Path("source_epubs")
    output_dir = Path("converted_texts")
    
    if not source_dir.exists():
        print("❌ source_epubs directory not found")
        return
    
    output_dir.mkdir(exist_ok=True)
    
    # Find all EPUB files
    epub_files = []
    for epub_path in source_dir.rglob("*.epub"):
        if epub_path.is_file():
            epub_files.append(epub_path)
    
    print(f"Found {len(epub_files)} total EPUB files")
    print(f"Processing batch: {start_from} to {start_from + batch_size}")
    
    # Process batch
    batch_files = epub_files[start_from:start_from + batch_size]
    
    successful = 0
    failed = 0
    failed_files = []
    
    for i, epub_file in enumerate(batch_files, start_from + 1):
        print(f"\n[{i}/{len(epub_files)}] Processing: {epub_file.name}")
        
        try:
            if convert_epub_to_markdown(epub_file, output_dir):
                successful += 1
                print(f"✅ Success")
            else:
                failed += 1
                failed_files.append(epub_file.name)
                print(f"❌ Failed")
        except KeyboardInterrupt:
            print(f"\n⏸️  Interrupted by user")
            break
        except Exception as e:
            failed += 1
            failed_files.append(epub_file.name)
            print(f"❌ Error: {e}")
    
    print(f"\n📊 Batch Results:")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")
    
    if failed_files:
        print(f"\n❌ Failed files:")
        for filename in failed_files:
            print(f"  - {filename}")
    
    # Show next batch suggestion
    next_start = start_from + batch_size
    if next_start < len(epub_files):
        print(f"\n💡 To process the next batch, run:")
        print(f"python3 batch_convert.py {batch_size} {next_start}")
    else:
        print("\n🎉 All files processed!")

if __name__ == "__main__":
    # Parse command line arguments
    batch_size = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    start_from = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    
    print(f"🚀 Starting batch conversion...")
    print(f"📦 Batch size: {batch_size}")
    print(f"📍 Starting from: {start_from}")
    
    batch_convert(batch_size, start_from)