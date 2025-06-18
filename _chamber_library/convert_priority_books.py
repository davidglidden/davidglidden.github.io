#!/usr/bin/env python3
"""
Convert Chamber Priority Books
Convert the identified Chamber voice and related philosophical texts
"""

from pathlib import Path
from convert_epub import convert_epub_to_markdown

def convert_priority_books():
    """Convert the specific Chamber-priority books"""
    
    # Priority book list (excluding Foucault's Pendulum which is Umbero Eco)
    priority_books = [
        # Core Chamber Voices
        "source_epubs/Landscapes John Berger on Art.epub",
        "source_epubs/Selected Essays of John Berger.epub",
        
        # Important Related Thinkers
        "source_epubs/The Collected Works of CG Jung Complete Digital Edition.epub",
        "source_epubs/Nietzsche.epub", 
        "source_epubs/Collected Poetical Works of Rumi Delphi Classics.epub",
        "source_epubs/Dune lyre à cinq cordes Pétrarque Le Tasse Leopardi Ungaretti Montale Bertolucci Luzi Bigongiari Erba Góngora Goethe Hölderlin Ferdinand Meyer Maria Rilke Lavant Burkart Mandelstam Skácel.epub"
    ]
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print("🎯 CONVERTING CHAMBER PRIORITY BOOKS")
    print("="*50)
    
    successful = 0
    failed = 0
    chamber_ready = []
    
    for book_path in priority_books:
        epub_path = Path(book_path)
        
        if not epub_path.exists():
            print(f"❌ File not found: {epub_path.name}")
            failed += 1
            continue
            
        print(f"\n📚 Converting: {epub_path.name}")
        
        try:
            if convert_epub_to_markdown(epub_path, output_dir):
                successful += 1
                chamber_ready.append(epub_path.name)
                print(f"✅ Success - Ready for Chamber integration")
            else:
                failed += 1
                print(f"❌ Failed")
        except Exception as e:
            failed += 1
            print(f"❌ Error: {e}")
    
    print(f"\n📊 CONVERSION SUMMARY")
    print("="*50)
    print(f"✅ Successfully converted: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"🏛️ Chamber-ready texts: {len(chamber_ready)}")
    
    if chamber_ready:
        print(f"\n🎭 CHAMBER-READY TEXTS:")
        for book in chamber_ready:
            print(f"   • {book}")
        
        print(f"\n🚀 NEXT STEPS:")
        print(f"   1. Run: python3 analyze_library.py")
        print(f"   2. Review converted texts in converted_texts/")
        print(f"   3. Begin Chamber integration testing")
        
        # Create a Chamber integration status file
        with open("chamber_integration_status.txt", "w") as f:
            f.write("CHAMBER LIBRARY INTEGRATION STATUS\n")
            f.write("="*40 + "\n\n")
            f.write(f"Priority books converted: {successful}/{len(priority_books)}\n")
            f.write(f"Chamber voices available: John Berger\n")
            f.write(f"Related thinkers: Jung, Nietzsche, Rumi, Rilke\n\n")
            
            f.write("READY FOR CHAMBER PROTOCOLS:\n")
            for book in chamber_ready:
                f.write(f"  ✅ {book}\n")
            
            f.write(f"\nINTEGRATION READINESS: ")
            if successful >= 2:
                f.write("🟢 READY - Core Chamber voice available\n")
            else:
                f.write("🟡 PARTIAL - Continue conversion\n")
    
    return successful, failed, chamber_ready

if __name__ == "__main__":
    successful, failed, chamber_ready = convert_priority_books()
    
    if chamber_ready:
        print(f"\n🎉 Chamber library foundation established!")
        print(f"📄 Status saved to: chamber_integration_status.txt")