#!/usr/bin/env python3
"""
Convert Jung Works for Chamber Integration
Special handling for Jung's psychological/archetypal voice in the Chamber
"""

import tempfile
from pathlib import Path
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_jung_works():
    """Convert Jung's works with proper Chamber voice classification"""
    
    # Jung works found in library
    jung_books = [
        {
            'path': Path("source_epubs/The Collected Works of CG Jung Complete Digital Edition.epub"),
            'title': "The Collected Works of C.G. Jung: Complete Digital Edition",
            'author': "C. G. Jung"
        },
        {
            'path': Path("source_epubs/The Red Book.epub"),
            'title': "The Red Book",
            'author': "C. G. Jung"
        },
        {
            'path': Path("source_epubs/The Black Books 1913-1932 Notebooks of Transformation.epub"),
            'title': "The Black Books: 1913-1932 : Notebooks of Transformation", 
            'author': "Carl Gustav Jung"
        },
        {
            'path': Path("source_epubs/The Red Book A Readers Edition.epub"),
            'title': "The Red Book: A Reader's Edition",
            'author': "C. G. Jung"
        }
    ]
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print("🧠 CONVERTING CARL JUNG WORKS FOR CHAMBER")
    print("=" * 50)
    print("Jung's role: Depth Psychologist of the Collective Unconscious")
    print("Chamber function: Archetypal analysis, psychological insight, symbolic interpretation")
    print()
    
    successful = 0
    failed = 0
    jung_texts = []
    
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        
        for i, book in enumerate(jung_books, 1):
            print(f"[{i}/4] Converting: {book['title']}")
            
            if not book['path'].exists():
                print(f"       ❌ File not found")
                failed += 1
                continue
            
            try:
                if convert_directory_epub_to_markdown(book['path'], output_dir, temp_dir):
                    successful += 1
                    jung_texts.append(book['title'])
                    print(f"       ✅ Success - Ready for Chamber integration")
                else:
                    failed += 1
                    print(f"       ❌ Failed")
            except Exception as e:
                failed += 1
                print(f"       ❌ Error: {str(e)[:50]}")
    
    print(f"\n📊 JUNG CONVERSION RESULTS")
    print("=" * 50)
    print(f"✅ Successfully converted: {successful}")
    print(f"❌ Failed: {failed}")
    
    if successful > 0:
        print(f"\n🧠 JUNG CHAMBER INTEGRATION:")
        print("Role: Depth Psychologist of Collective Unconscious")
        print("Voice style: Analytical-symbolic")
        print("Dialectical relationships:")
        print("  • Bachelard (imagination, reverie)")
        print("  • Weil (attention, inner work)")
        print("  • Benjamin (aura, collective memory)")
        print("  • Levinas (encounter with the Other)")
        
        print(f"\nConverted Jung texts:")
        for text in jung_texts:
            print(f"  • {text}")
        
        print(f"\n🎭 CHAMBER STATUS UPDATE:")
        print("Jung adds psychological depth and archetypal wisdom to Chamber deliberations")
        print("Particularly valuable for:")
        print("  - Symbolic interpretation")
        print("  - Psychological insight into texts")
        print("  - Collective unconscious themes")
        print("  - Integration of opposites")
    
    return successful, jung_texts

if __name__ == "__main__":
    successful, jung_texts = convert_jung_works()
    
    if successful > 0:
        print(f"\n✨ Jung successfully integrated into Chamber library!")
        print(f"🔄 Run: python3 analyze_library.py to see updated Chamber status")