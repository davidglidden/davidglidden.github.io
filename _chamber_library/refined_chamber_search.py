#!/usr/bin/env python3
"""
Refined Chamber Voice Search
More precise identification of books by Chamber voices
"""

from pathlib import Path
import re
from collections import defaultdict

def refined_chamber_search():
    """More precise search for Chamber voices"""
    source_dir = Path("source_epubs")
    
    # Define Chamber voices with more precise patterns
    chamber_voices = {
        'Gaston Bachelard': {
            'patterns': [r'bachelard', r'gaston.*bachelard'],
            'books': []
        },
        'Christopher Alexander': {
            'patterns': [r'christopher.*alexander', r'alexander.*pattern', r'alexander.*nature'],
            'books': []
        },
        'Walter Benjamin': {
            'patterns': [r'walter.*benjamin', r'benjamin.*walter'],
            'books': []
        },
        'Hannah Arendt': {
            'patterns': [r'hannah.*arendt', r'arendt.*hannah'],
            'books': []
        },
        'Simone Weil': {
            'patterns': [r'simone.*weil', r'weil.*simone'],
            'books': []
        },
        'Emmanuel Levinas': {
            'patterns': [r'emmanuel.*levinas', r'levinas.*emmanuel', r'\blevinas\b'],
            'books': []
        },
        'Martin Heidegger': {
            'patterns': [r'martin.*heidegger', r'heidegger.*martin', r'\bheidegger\b'],
            'books': []
        },
        'Robin Wall Kimmerer': {
            'patterns': [r'kimmerer', r'robin.*kimmerer'],
            'books': []
        },
        'Shoshana Zuboff': {
            'patterns': [r'zuboff', r'shoshana.*zuboff'],
            'books': []
        },
        'John Berger': {
            'patterns': [r'john berger', r'berger.*john', r'berger on art', r'berger.*ways'],
            'books': []
        },
        'Aldus Manutius': {
            'patterns': [r'manutius', r'aldus.*manutius'],
            'books': []
        }
    }
    
    # Additional important thinkers for Chamber context
    important_thinkers = {
        'Maurice Merleau-Ponty': [r'merleau.ponty', r'maurice.*merleau'],
        'Jacques Derrida': [r'derrida', r'jacques.*derrida'],
        'Michel Foucault': [r'foucault', r'michel.*foucault'],
        'Jean Baudrillard': [r'baudrillard', r'jean.*baudrillard'],
        'Paul Virilio': [r'virilio', r'paul.*virilio'],
        'Giorgio Agamben': [r'agamben', r'giorgio.*agamben'],
        'Juhani Pallasmaa': [r'pallasmaa', r'juhani.*pallasmaa'],
        'Jane Jacobs': [r'jane.*jacobs', r'jacobs.*jane'],
        'Lewis Mumford': [r'lewis.*mumford', r'mumford.*lewis'],
        'Ivan Illich': [r'ivan.*illich', r'illich.*ivan'],
        'Jacques Ellul': [r'jacques.*ellul', r'ellul.*jacques'],
        'Carl Jung': [r'carl.*jung', r'jung.*carl', r'\bjung\b'],
        'Joseph Campbell': [r'joseph.*campbell', r'campbell.*joseph'],
        'Thomas Merton': [r'thomas.*merton', r'merton.*thomas'],
        'Pierre Teilhard de Chardin': [r'teilhard', r'chardin'],
        'Rumi': [r'\brumi\b'],
        'Rainer Maria Rilke': [r'rilke', r'rainer.*rilke'],
        'William Blake': [r'william.*blake', r'blake.*william'],
        'Friedrich Nietzsche': [r'nietzsche', r'friedrich.*nietzsche']
    }
    
    # Collect all EPUB items
    epub_items = []
    for epub_path in source_dir.rglob("*.epub"):
        if epub_path.is_file():
            epub_items.append(epub_path)
    
    for item in source_dir.iterdir():
        if item.is_dir() and item.name.endswith('.epub'):
            epub_items.append(item)
    
    print(f"🔍 Performing refined search on {len(epub_items)} EPUB items...\n")
    
    # Search for Chamber voices
    for epub_item in epub_items:
        filename = epub_item.name.lower()
        
        # Check Chamber voices
        for voice_name, voice_data in chamber_voices.items():
            for pattern in voice_data['patterns']:
                if re.search(pattern, filename):
                    voice_data['books'].append(epub_item)
                    break
        
        # Check important thinkers
        for thinker, patterns in important_thinkers.items():
            for pattern in patterns:
                if re.search(pattern, filename):
                    if thinker not in chamber_voices:
                        chamber_voices[thinker] = {'patterns': patterns, 'books': [epub_item]}
                    else:
                        # Avoid duplicates
                        if epub_item not in chamber_voices[thinker]['books']:
                            chamber_voices[thinker]['books'].append(epub_item)
                    break
    
    # Display results
    print("🏛️ CHAMBER VOICES & IMPORTANT THINKERS FOUND")
    print("=" * 65)
    
    chamber_count = 0
    priority_files = []
    
    # Core Chamber voices first
    core_voices = [
        'Gaston Bachelard', 'Christopher Alexander', 'Walter Benjamin',
        'Hannah Arendt', 'Simone Weil', 'Emmanuel Levinas', 
        'Martin Heidegger', 'Robin Wall Kimmerer', 'Shoshana Zuboff',
        'John Berger', 'Aldus Manutius'
    ]
    
    print("🎭 CORE CHAMBER VOICES:")
    for voice_name in core_voices:
        if voice_name in chamber_voices and chamber_voices[voice_name]['books']:
            books = chamber_voices[voice_name]['books']
            chamber_count += len(books)
            priority_files.extend(books)
            print(f"\n📚 {voice_name} ({len(books)} books):")
            for book in books:
                print(f"   • {book.name}")
    
    print(f"\n🧠 RELATED IMPORTANT THINKERS:")
    for voice_name, voice_data in chamber_voices.items():
        if voice_name not in core_voices and voice_data['books']:
            books = voice_data['books']
            print(f"\n📖 {voice_name} ({len(books)} books):")
            for book in books:
                print(f"   • {book.name}")
    
    # Write detailed results
    with open("chamber_books_refined.txt", "w") as f:
        f.write("REFINED CHAMBER LIBRARY ANALYSIS\n")
        f.write("="*50 + "\n\n")
        
        f.write("CORE CHAMBER VOICES:\n")
        for voice_name in core_voices:
            if voice_name in chamber_voices and chamber_voices[voice_name]['books']:
                books = chamber_voices[voice_name]['books']
                f.write(f"\n{voice_name} ({len(books)} books):\n")
                for book in books:
                    f.write(f"  {book}\n")
        
        f.write(f"\nRELATED THINKERS:\n")
        for voice_name, voice_data in chamber_voices.items():
            if voice_name not in core_voices and voice_data['books']:
                books = voice_data['books']
                f.write(f"\n{voice_name} ({len(books)} books):\n")
                for book in books:
                    f.write(f"  {book}\n")
    
    print(f"\n💡 SUMMARY:")
    print(f"   🎭 Core Chamber voices: {chamber_count} books")
    print(f"   🧠 Total philosophical books found: {sum(len(v['books']) for v in chamber_voices.values())}")
    print(f"   📄 Detailed results saved to: chamber_books_refined.txt")
    
    if chamber_count > 0:
        print(f"\n🚀 READY FOR PRIORITY CONVERSION!")
        print(f"   Use these files for immediate Chamber integration")
    else:
        print(f"\n🔍 CONTINUE SEARCH:")
        print(f"   May need manual inspection or different search terms")
    
    return priority_files

if __name__ == "__main__":
    priority_files = refined_chamber_search()
    
    if priority_files:
        print(f"\n🎯 NEXT STEP: Convert {len(priority_files)} priority books")
        print(f"   python3 convert_priority_books.py")