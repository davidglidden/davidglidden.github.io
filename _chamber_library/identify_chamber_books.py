#!/usr/bin/env python3
"""
Chamber Voice Book Identification
Scan EPUB library to identify books by key Chamber voices
"""

from pathlib import Path
import re
from collections import defaultdict

def identify_chamber_books():
    """Identify EPUBs by Chamber voices and related thinkers"""
    source_dir = Path("source_epubs")
    
    if not source_dir.exists():
        print("❌ source_epubs directory not found")
        return
    
    # Core Chamber voices
    chamber_voices = {
        'Gaston Bachelard': ['bachelard', 'gaston'],
        'Christopher Alexander': ['alexander', 'christopher'],
        'Walter Benjamin': ['benjamin', 'walter'],
        'Hannah Arendt': ['arendt', 'hannah'],
        'Simone Weil': ['weil', 'simone'],
        'Emmanuel Levinas': ['levinas', 'emmanuel'],
        'Martin Heidegger': ['heidegger', 'martin'],
        'Robin Wall Kimmerer': ['kimmerer', 'robin'],
        'Shoshana Zuboff': ['zuboff', 'shoshana'],
        'John Berger': ['berger', 'john'],
        'Aldus Manutius': ['manutius', 'aldus']
    }
    
    # Extended philosophical constellation
    related_thinkers = {
        'Philosophy & Phenomenology': [
            'merleau-ponty', 'husserl', 'sartre', 'beauvoir', 'camus',
            'nietzsche', 'kierkegaard', 'jaspers', 'gadamer'
        ],
        'Critical Theory & Frankfurt School': [
            'adorno', 'horkheimer', 'marcuse', 'habermas', 'fromm'
        ],
        'Architecture & Design': [
            'lynch', 'jacobs', 'norberg-schulz', 'pallasmaa', 'corbusier',
            'wright', 'kahn', 'aalto', 'zumthor'
        ],
        'Technology & Society': [
            'ellul', 'mumford', 'postman', 'turkle', 'winner', 'ihde'
        ],
        'Ecology & Indigenous Thought': [
            'leopold', 'berry', 'snyder', 'deloria', 'cajete'
        ],
        'Mystical & Contemplative': [
            'eckhart', 'ruysbroeck', 'john of the cross', 'teresa',
            'pseudo-dionysius', 'ibn arabi'
        ]
    }
    
    # Find all EPUB items
    epub_items = []
    
    # Regular files
    for epub_file in source_dir.rglob("*.epub"):
        if epub_file.is_file():
            epub_items.append(epub_file)
    
    # Directory-format EPUBs
    for item in source_dir.iterdir():
        if item.is_dir() and item.name.endswith('.epub'):
            epub_items.append(item)
    
    print(f"🔍 Scanning {len(epub_items)} EPUB items for Chamber voices...\n")
    
    # Results containers
    chamber_matches = defaultdict(list)
    related_matches = defaultdict(list)
    potential_matches = []
    
    for epub_item in epub_items:
        filename = epub_item.name.lower()
        
        # Check for Chamber voices
        for voice_name, keywords in chamber_voices.items():
            for keyword in keywords:
                if keyword in filename:
                    chamber_matches[voice_name].append(epub_item)
                    break
        
        # Check for related philosophical thinkers
        for category, thinkers in related_thinkers.items():
            for thinker in thinkers:
                if thinker in filename:
                    related_matches[category].append((thinker, epub_item))
                    break
        
        # Look for philosophical keywords
        phil_keywords = [
            'philosophy', 'metaphysics', 'ethics', 'phenomenology',
            'existential', 'ontology', 'epistemology', 'dialectic',
            'critique', 'consciousness', 'being', 'time', 'space',
            'dwelling', 'place', 'technology', 'nature', 'ecology'
        ]
        
        for keyword in phil_keywords:
            if keyword in filename and epub_item not in [item for sublist in chamber_matches.values() for item in sublist]:
                potential_matches.append((keyword, epub_item))
                break
    
    # Display results
    print("🏛️ CORE CHAMBER VOICES FOUND")
    print("=" * 60)
    
    total_chamber_books = 0
    for voice_name, books in chamber_matches.items():
        if books:
            total_chamber_books += len(books)
            print(f"\n📚 {voice_name} ({len(books)} books):")
            for book in books:
                print(f"   • {book.name}")
    
    if total_chamber_books == 0:
        print("❌ No core Chamber voices found in filenames")
    
    print(f"\n🔗 RELATED PHILOSOPHICAL THINKERS")
    print("=" * 60)
    
    for category, matches in related_matches.items():
        if matches:
            print(f"\n📖 {category} ({len(matches)} books):")
            for thinker, book in matches[:5]:  # Show first 5
                print(f"   • {thinker.title()}: {book.name[:50]}...")
            if len(matches) > 5:
                print(f"   ... and {len(matches) - 5} more")
    
    print(f"\n🎯 POTENTIAL PHILOSOPHICAL TEXTS")
    print("=" * 60)
    
    if potential_matches:
        print(f"Found {len(potential_matches)} books with philosophical keywords:")
        for keyword, book in potential_matches[:10]:
            print(f"   • [{keyword}] {book.name[:50]}...")
        if len(potential_matches) > 10:
            print(f"   ... and {len(potential_matches) - 10} more")
    
    # Priority recommendations
    print(f"\n💡 CONVERSION RECOMMENDATIONS")
    print("=" * 60)
    
    priority_files = []
    
    # Priority 1: Core Chamber voices
    for voice_name, books in chamber_matches.items():
        priority_files.extend(books)
    
    # Priority 2: Key related thinkers (phenomenology, critical theory)
    key_categories = ['Philosophy & Phenomenology', 'Critical Theory & Frankfurt School']
    for category in key_categories:
        if category in related_matches:
            priority_files.extend([book for _, book in related_matches[category]])
    
    print(f"🔥 HIGH PRIORITY: {len(priority_files)} books")
    print("   Convert these first for immediate Chamber integration")
    
    # Write priority list to file
    with open("chamber_priority_books.txt", "w") as f:
        f.write("CHAMBER LIBRARY PRIORITY CONVERSION LIST\n")
        f.write("="*50 + "\n\n")
        
        f.write("CORE CHAMBER VOICES:\n")
        for voice_name, books in chamber_matches.items():
            if books:
                f.write(f"\n{voice_name}:\n")
                for book in books:
                    f.write(f"  {book}\n")
        
        f.write(f"\nKEY RELATED THINKERS:\n")
        for category in key_categories:
            if category in related_matches:
                f.write(f"\n{category}:\n")
                for thinker, book in related_matches[category]:
                    f.write(f"  {book}\n")
    
    print(f"📄 Priority list saved to: chamber_priority_books.txt")
    
    return {
        'chamber_books': total_chamber_books,
        'related_books': sum(len(matches) for matches in related_matches.values()),
        'potential_books': len(potential_matches),
        'priority_files': priority_files
    }

if __name__ == "__main__":
    identify_chamber_books()