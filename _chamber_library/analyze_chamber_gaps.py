#!/usr/bin/env python3
"""
Chamber Voice Gap Analysis
Identify which Chamber voices are missing from the library and suggest acquisitions
"""

import csv
from pathlib import Path
from collections import defaultdict
import re

def analyze_chamber_gaps():
    """Analyze library CSV to find Chamber voice gaps and opportunities"""
    
    csv_file = Path("apple_books_library.csv")
    if not csv_file.exists():
        print("❌ Please run extract_library_csv.py first")
        return
    
    # Core Chamber voices
    chamber_voices = {
        'Gaston Bachelard': {
            'search_terms': ['bachelard', 'gaston'],
            'key_works': [
                'The Poetics of Space',
                'The Psychoanalysis of Fire', 
                'Air and Dreams',
                'The Poetics of Reverie',
                'Water and Dreams'
            ],
            'found': []
        },
        'Christopher Alexander': {
            'search_terms': ['alexander', 'christopher'],
            'key_works': [
                'A Pattern Language',
                'The Timeless Way of Building',
                'The Nature of Order',
                'A City is Not a Tree',
                'The Oregon Experiment'
            ],
            'found': []
        },
        'Walter Benjamin': {
            'search_terms': ['benjamin', 'walter'],
            'key_works': [
                'The Work of Art in the Age of Mechanical Reproduction',
                'Illuminations',
                'The Arcades Project',
                'One-Way Street',
                'The Origin of German Tragic Drama'
            ],
            'found': []
        },
        'Hannah Arendt': {
            'search_terms': ['arendt', 'hannah'],
            'key_works': [
                'The Human Condition',
                'The Origins of Totalitarianism',
                'Between Past and Future',
                'On Revolution',
                'The Life of the Mind'
            ],
            'found': []
        },
        'Simone Weil': {
            'search_terms': ['weil', 'simone'],
            'key_works': [
                'Gravity and Grace',
                'The Need for Roots',
                'Waiting for God',
                'Oppression and Liberty',
                'Notebooks'
            ],
            'found': []
        },
        'Emmanuel Levinas': {
            'search_terms': ['levinas', 'emmanuel'],
            'key_works': [
                'Totality and Infinity',
                'Otherwise than Being',
                'Difficult Freedom',
                'Ethics and Infinity',
                'The Levinas Reader'
            ],
            'found': []
        },
        'Martin Heidegger': {
            'search_terms': ['heidegger', 'martin'],
            'key_works': [
                'Being and Time',
                'The Question Concerning Technology',
                'Poetry, Language, Thought',
                'What is Called Thinking?',
                'Introduction to Metaphysics'
            ],
            'found': []
        },
        'Robin Wall Kimmerer': {
            'search_terms': ['kimmerer', 'robin'],
            'key_works': [
                'Braiding Sweetgrass',
                'Gathering Moss',
                'The Council of Pecans'
            ],
            'found': []
        },
        'Shoshana Zuboff': {
            'search_terms': ['zuboff', 'shoshana'],
            'key_works': [
                'The Age of Surveillance Capitalism',
                'In the Age of the Smart Machine'
            ],
            'found': []
        },
        'John Berger': {
            'search_terms': ['berger'],
            'key_works': [
                'Ways of Seeing',
                'About Looking',
                'The Shape of a Pocket',
                'Here Is Where We Meet',
                'A Fortunate Man'
            ],
            'found': []
        },
        'Aldus Manutius': {
            'search_terms': ['manutius', 'aldus'],
            'key_works': [
                'The Aldine Press',
                'Hypnerotomachia Poliphili',
                'Aldus Manutius: The Legacy of a Renaissance Printer'
            ],
            'found': []
        }
    }
    
    # Extended philosophical constellation for context
    extended_voices = {
        'Maurice Merleau-Ponty': ['merleau', 'ponty'],
        'Jacques Derrida': ['derrida'],
        'Michel Foucault': ['foucault'],
        'Jürgen Habermas': ['habermas'],
        'Theodor Adorno': ['adorno'],
        'Giorgio Agamben': ['agamben'],
        'Juhani Pallasmaa': ['pallasmaa'],
        'Jane Jacobs': ['jane jacobs', 'jacobs'],
        'Lewis Mumford': ['mumford'],
        'Ivan Illich': ['illich'],
        'Jacques Ellul': ['ellul'],
        'Paul Virilio': ['virilio'],
        'Jean Baudrillard': ['baudrillard'],
        'Vilém Flusser': ['flusser'],
        'Peter Sloterdijk': ['sloterdijk']
    }
    
    # Read library CSV
    library_books = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        library_books = list(reader)
    
    print(f"📚 Analyzing {len(library_books)} books for Chamber voice coverage...\n")
    
    # Search for Chamber voices
    for voice_name, voice_data in chamber_voices.items():
        for book in library_books:
            author_lower = book['author'].lower()
            title_lower = book['title'].lower()
            
            # Check if any search terms match
            for term in voice_data['search_terms']:
                if term in author_lower:
                    voice_data['found'].append({
                        'title': book['title'],
                        'author': book['author'],
                        'filename': book['filename']
                    })
                    break
    
    # Search for extended voices
    extended_found = defaultdict(list)
    for voice_name, search_terms in extended_voices.items():
        for book in library_books:
            author_lower = book['author'].lower()
            
            for term in search_terms:
                if term in author_lower:
                    extended_found[voice_name].append({
                        'title': book['title'],
                        'author': book['author']
                    })
                    break
    
    # Generate report
    print("🏛️ CHAMBER VOICE COVERAGE ANALYSIS")
    print("=" * 60)
    
    present_voices = []
    missing_voices = []
    
    for voice_name, voice_data in chamber_voices.items():
        if voice_data['found']:
            present_voices.append(voice_name)
            print(f"\n✅ {voice_name} ({len(voice_data['found'])} books):")
            for book in voice_data['found'][:3]:  # Show first 3
                print(f"   • {book['title']}")
            if len(voice_data['found']) > 3:
                print(f"   ... and {len(voice_data['found']) - 3} more")
        else:
            missing_voices.append(voice_name)
    
    print(f"\n❌ MISSING CHAMBER VOICES ({len(missing_voices)}):")
    print("=" * 60)
    
    acquisition_list = []
    
    for voice_name in missing_voices:
        voice_data = chamber_voices[voice_name]
        print(f"\n🔍 {voice_name}")
        print(f"   Priority acquisitions:")
        for i, work in enumerate(voice_data['key_works'][:3], 1):
            print(f"   {i}. {work}")
            acquisition_list.append(f"{voice_name} - {work}")
        
        if len(voice_data['key_works']) > 3:
            print(f"   ... and {len(voice_data['key_works']) - 3} more key works")
    
    print(f"\n🧠 EXTENDED PHILOSOPHICAL VOICES PRESENT:")
    print("=" * 60)
    
    for voice_name, books in extended_found.items():
        if books:
            print(f"✅ {voice_name} ({len(books)} books)")
    
    missing_extended = [name for name in extended_voices.keys() if name not in extended_found]
    if missing_extended:
        print(f"\n🔍 MISSING EXTENDED VOICES:")
        for voice in missing_extended[:5]:
            print(f"   • {voice}")
        if len(missing_extended) > 5:
            print(f"   ... and {len(missing_extended) - 5} more")
    
    # Summary statistics
    print(f"\n📊 SUMMARY:")
    print("=" * 60)
    print(f"🎭 Core Chamber voices present: {len(present_voices)}/11")
    print(f"❌ Core voices missing: {len(missing_voices)}/11")
    print(f"🧠 Extended voices present: {len([v for v in extended_found.values() if v])}")
    print(f"📚 Total philosophical books: {len(present_voices) + len([v for v in extended_found.values() if v])}")
    
    # Integration readiness
    readiness_score = len(present_voices) / len(chamber_voices) * 100
    print(f"\n🎯 CHAMBER INTEGRATION READINESS: {readiness_score:.1f}%")
    
    if readiness_score >= 70:
        print("🟢 EXCELLENT - Ready for full Chamber protocols")
    elif readiness_score >= 50:
        print("🟡 GOOD - Ready for limited Chamber protocols")
    elif readiness_score >= 30:
        print("🟠 FAIR - Focus on priority acquisitions")
    else:
        print("🔴 NEEDS WORK - Build foundation first")
    
    # Write acquisition recommendations
    with open("chamber_acquisition_recommendations.txt", "w") as f:
        f.write("CHAMBER LIBRARY ACQUISITION RECOMMENDATIONS\n")
        f.write("="*50 + "\n\n")
        
        f.write("MISSING CORE CHAMBER VOICES:\n")
        for voice_name in missing_voices:
            voice_data = chamber_voices[voice_name]
            f.write(f"\n{voice_name}:\n")
            for work in voice_data['key_works']:
                f.write(f"  • {work}\n")
        
        f.write(f"\nPRIORITY ACQUISITION LIST (Top 20):\n")
        for i, item in enumerate(acquisition_list[:20], 1):
            f.write(f"{i:2d}. {item}\n")
        
        f.write(f"\nCURRENT STRENGTHS:\n")
        for voice_name in present_voices:
            f.write(f"  ✅ {voice_name}\n")
    
    print(f"\n📄 Detailed recommendations saved to: chamber_acquisition_recommendations.txt")
    
    return {
        'present_voices': present_voices,
        'missing_voices': missing_voices,
        'readiness_score': readiness_score,
        'acquisition_list': acquisition_list[:20]
    }

if __name__ == "__main__":
    analyze_chamber_gaps()