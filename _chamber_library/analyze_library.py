#!/usr/bin/env python3
"""
Chamber Library Analysis
Analyze converted texts for voice distribution, topics, and Chamber integration potential
"""

import yaml
from pathlib import Path
from collections import Counter, defaultdict
import re

def analyze_converted_library():
    """Analyze the converted library for Chamber integration insights"""
    converted_dir = Path("converted_texts")
    
    if not converted_dir.exists():
        print("❌ No converted texts found")
        return
    
    md_files = list(converted_dir.glob("*.md"))
    print(f"📚 Analyzing {len(md_files)} converted texts...\n")
    
    # Analysis containers
    authors = Counter()
    voices = Counter()
    quote_styles = Counter()
    titles = []
    chamber_voices = []
    unknown_authors = []
    
    for md_file in md_files:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract YAML frontmatter
            if content.startswith('---\n'):
                yaml_end = content.find('\n---\n', 4)
                if yaml_end > 0:
                    yaml_content = content[4:yaml_end]
                    metadata = yaml.safe_load(yaml_content)
                    
                    author = metadata.get('author', 'Unknown')
                    voice = metadata.get('voice', 'Unknown')
                    title = metadata.get('title', 'Unknown')
                    quote_style = metadata.get('quote_style', 'standard')
                    
                    authors[author] += 1
                    voices[voice] += 1
                    quote_styles[quote_style] += 1
                    titles.append(title)
                    
                    # Track Chamber-relevant voices
                    chamber_voices_list = [
                        'Gaston Bachelard', 'Christopher Alexander', 'Walter Benjamin',
                        'Hannah Arendt', 'Simone Weil', 'Emmanuel Levinas',
                        'Martin Heidegger', 'Robin Wall Kimmerer', 'Shoshana Zuboff',
                        'John Berger', 'Aldus Manutius'
                    ]
                    
                    if voice in chamber_voices_list:
                        chamber_voices.append((title, voice))
                    
                    if author == 'Unknown Author':
                        unknown_authors.append(md_file.name)
                        
        except Exception as e:
            print(f"❌ Error analyzing {md_file.name}: {e}")
    
    # Print analysis results
    print("🎭 VOICE DISTRIBUTION")
    print("=" * 50)
    for voice, count in voices.most_common(10):
        print(f"{voice:<30} {count:>3} books")
    
    print(f"\n📝 QUOTE STYLES")
    print("=" * 50)
    for style, count in quote_styles.most_common():
        print(f"{style:<15} {count:>3} books")
    
    print(f"\n🏛️ CHAMBER VOICES FOUND")
    print("=" * 50)
    if chamber_voices:
        for title, voice in chamber_voices:
            print(f"• {voice}: {title[:50]}...")
    else:
        print("No core Chamber voices found in current batch")
    
    print(f"\n❓ UNKNOWN AUTHORS")
    print("=" * 50)
    if unknown_authors:
        print(f"Found {len(unknown_authors)} books needing metadata improvement:")
        for filename in unknown_authors[:5]:
            print(f"  - {filename}")
        if len(unknown_authors) > 5:
            print(f"  ... and {len(unknown_authors) - 5} more")
    else:
        print("All books have identified authors!")
    
    print(f"\n📊 SUMMARY")
    print("=" * 50)
    print(f"Total converted texts: {len(md_files)}")
    print(f"Unique authors: {len(authors)}")
    print(f"Chamber voices: {len(chamber_voices)}")
    print(f"Needs metadata work: {len(unknown_authors)}")
    
    # Chamber integration recommendations
    print(f"\n💡 CHAMBER INTEGRATION RECOMMENDATIONS")
    print("=" * 50)
    
    if len(chamber_voices) > 0:
        print("✅ Ready for Chamber integration with core voices")
    else:
        print("⏳ Continue converting to find core philosophical texts")
    
    if len(unknown_authors) > len(md_files) * 0.2:
        print("🔧 Consider improving metadata extraction")
    else:
        print("✅ Metadata extraction working well")
    
    return {
        'total_books': len(md_files),
        'chamber_voices': len(chamber_voices),
        'unknown_authors': len(unknown_authors),
        'top_voices': voices.most_common(5)
    }

if __name__ == "__main__":
    analyze_converted_library()