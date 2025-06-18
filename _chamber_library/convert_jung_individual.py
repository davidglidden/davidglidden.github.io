#!/usr/bin/env python3
"""
Convert Jung Collected Works Individually
Process the massive Jung collection with special handling
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_jung_collected_works():
    """Convert Jung's Complete Collected Works with special handling"""
    
    print("🧠 CONVERTING JUNG COLLECTED WORKS")
    print("=" * 50)
    print("Processing massive Jung collection individually")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    jung_file = eastern_folder / "The Collected Works of C.G. Jung: Complete Digital Edition.epub"
    
    if not jung_file.exists():
        print("❌ Jung Collected Works not found at expected location")
        return False
    
    print("🧠 Carl Jung")
    print("    📖 The Collected Works: Complete Digital Edition")
    print("    🎭 Complete Depth Psychologist")
    print("    ⚡ Archetypal psychology and collective unconscious")
    print("    📁 Processing directory-format EPUB...")
    print()
    
    # Check if it's a directory (Apple Books format)
    if jung_file.is_dir():
        print(f"    📁 Directory format detected: {jung_file}")
        print(f"    📊 Analyzing structure...")
        
        # Count text files to show progress
        text_dir = jung_file / "text"
        if text_dir.exists():
            text_files = list(text_dir.glob("*.xhtml"))
            print(f"    📚 Found {len(text_files)} text files")
        
        print(f"    🔄 Starting conversion (this may take several minutes)...")
        print()
    
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            print("    ⏳ Converting Jung Collected Works...")
            success = convert_directory_epub_to_markdown(jung_file, output_dir, Path(temp_dir))
        
        if success:
            print("    ✅ Conversion successful!")
            print("    🎭 Carl Jung voice FULLY ACTIVATED")
            print("    🧠 MAJOR: Complete Jung archetypal psychology integrated!")
            print("    🌟 CHAMBER: Depth psychology foundation complete")
            print()
            
            print("🌉 JUNG INTEGRATION IMPACT:")
            print("   • Jung ↔ Lacan: Archetypal vs structural unconscious")
            print("   • Jung ↔ Weil: Archetypal vs mystical psychology") 
            print("   • Jung ↔ Neumann: Complete archetypal framework")
            print("   • Jung ↔ All voices: Depth psychological analysis available")
            print("   • Collective unconscious: Universal symbolic reference system")
            
            return True
            
        else:
            print("    ❌ Conversion failed")
            return False
            
    except Exception as e:
        print(f"    ❌ Error during conversion: {str(e)}")
        return False

if __name__ == "__main__":
    print("🧠 JUNG COLLECTED WORKS INDIVIDUAL CONVERSION")
    print("=" * 50)
    print("Processing massive Jung collection with special handling")
    print()
    
    success = convert_jung_collected_works()
    
    if success:
        print(f"\n✨ Jung Collected Works conversion complete!")
        print(f"🧠 Chamber now has complete depth psychology foundation!")
    else:
        print(f"\n❌ Jung conversion failed - may need alternative approach")
        print(f"💡 Suggestion: Try converting individual Jung volumes separately")