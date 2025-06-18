#!/usr/bin/env python3
"""
Convert Harvard Classics Individually
Process the massive Harvard Classics collection
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_harvard_classics():
    """Convert Harvard Classics with special handling"""
    
    print("📚 CONVERTING HARVARD CLASSICS")
    print("=" * 40)
    print("Processing complete Harvard Classics collection")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    harvard_file = eastern_folder / "Complete Harvard Classics.epub"
    
    if not harvard_file.exists():
        print("❌ Harvard Classics not found at expected location")
        return False
    
    print("📚 Harvard Classics")
    print("    📖 Complete Collection")
    print("    🎭 Western Canon Compilation")
    print("    ⚡ Complete classical education collection")
    print("    📁 Processing directory-format EPUB...")
    print()
    
    # Check if it's a directory (Apple Books format)
    if harvard_file.is_dir():
        print(f"    📁 Directory format detected: {harvard_file}")
        print(f"    📊 Analyzing structure...")
        
        # Count files to show progress
        ops_dir = harvard_file / "Ops"
        if ops_dir.exists():
            ops_files = list(ops_dir.glob("*.xhtml"))
            print(f"    📚 Found {len(ops_files)} content files")
        
        print(f"    🔄 Starting conversion (this may take several minutes)...")
        print()
    
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            print("    ⏳ Converting Harvard Classics...")
            success = convert_directory_epub_to_markdown(harvard_file, output_dir, Path(temp_dir))
        
        if success:
            print("    ✅ Conversion successful!")
            print("    🎭 Harvard Classics FULLY ACTIVATED")
            print("    📚 MAJOR: Complete Western canon integrated!")
            print("    🌟 CHAMBER: Classical education foundation complete")
            print()
            
            print("🌉 HARVARD CLASSICS INTEGRATION IMPACT:")
            print("   • Complete Western canon: From ancient to modern")
            print("   • Classical education: Comprehensive liberal arts foundation")
            print("   • Reference system: Universal classical references for all voices")
            print("   • Historical perspective: Complete chronological development")
            print("   • Cross-cultural dialogue: Western canon in global context")
            
            return True
            
        else:
            print("    ❌ Conversion failed")
            return False
            
    except Exception as e:
        print(f"    ❌ Error during conversion: {str(e)}")
        return False

if __name__ == "__main__":
    print("📚 HARVARD CLASSICS INDIVIDUAL CONVERSION")
    print("=" * 40)
    print("Processing complete Harvard Classics collection")
    print()
    
    success = convert_harvard_classics()
    
    if success:
        print(f"\n✨ Harvard Classics conversion complete!")
        print(f"📚 Chamber now has complete Western canonical foundation!")
    else:
        print(f"\n❌ Harvard Classics conversion failed - collection too large")
        print(f"💡 Suggestion: Extract individual volumes or use alternative approach")