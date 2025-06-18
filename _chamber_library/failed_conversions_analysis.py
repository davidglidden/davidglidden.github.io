#!/usr/bin/env python3
"""
Failed Conversions Analysis
Complete list of all failed conversions with reasons and alternative approaches
"""

from pathlib import Path

def create_failed_conversions_list():
    """Generate comprehensive list of all failed conversions"""
    
    print("❌ CHAMBER FAILED CONVERSIONS ANALYSIS")
    print("=" * 60)
    print("Complete list of failed conversions with reasons and solutions")
    print()
    
    # Failed conversions organized by reason and potential solutions
    failed_conversions = {
        'MASSIVE COLLECTIONS (TIMEOUT FAILURES)': {
            'reason': 'Files too large for 2-minute pandoc timeout',
            'solution': 'Split into segments or find individual volumes',
            'files': [
                {
                    'filename': 'The Collected Works of C.G. Jung: Complete Digital Edition.epub',
                    'location': '/Users/davidglidden/Desktop/eastern to the library/',
                    'author': 'Carl Jung',
                    'priority': 'CRITICAL',
                    'voice_impact': 'Complete depth psychology foundation',
                    'alternative_approaches': [
                        'Find individual Jung volumes (Red Book, Man and His Symbols, etc.)',
                        'Extract key volumes from complete collection directory',
                        'Use ebook splitting tools to break into segments',
                        'Convert individual text files from the directory structure'
                    ]
                },
                {
                    'filename': 'Complete Harvard Classics.epub',
                    'location': '/Users/davidglidden/Desktop/eastern to the library/',
                    'author': 'Various Classical Authors',
                    'priority': 'HIGH',
                    'voice_impact': 'Complete Western canonical education',
                    'alternative_approaches': [
                        'Extract individual classic works from collection',
                        'Focus on missing classics not already converted',
                        'Use directory structure to convert volumes separately',
                        'Prioritize key works: Dante, Aristotle, Augustine, etc.'
                    ]
                },
                {
                    'filename': 'The Connected Discourses of the Buddha: A Translation of the Samyutta Nikaya.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Buddha',
                    'priority': 'CRITICAL',
                    'voice_impact': 'Complete Buddhist discourse collection',
                    'alternative_approaches': [
                        'Split Samyutta Nikaya into individual discourse groups',
                        'Convert section by section',
                        'Find alternative shorter Buddhist discourse collections'
                    ]
                },
                {
                    'filename': 'The Long Discourses of the Buddha.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Buddha',
                    'priority': 'CRITICAL',
                    'voice_impact': 'Buddhist long discourse collection',
                    'alternative_approaches': [
                        'Convert individual long discourses',
                        'Split into thematic groups',
                        'Use alternative Digha Nikaya editions'
                    ]
                },
                {
                    'filename': 'The Middle Length Discourses of the Buddha: A Translation of the Majjhima Nikaya.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Buddha',
                    'priority': 'CRITICAL',
                    'voice_impact': 'Core Buddhist practical teachings',
                    'alternative_approaches': [
                        'Split into individual middle-length discourses',
                        'Convert by thematic groupings',
                        'Use shorter Majjhima collections'
                    ]
                },
                {
                    'filename': 'The Numerical Discourses of the Buddha.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Buddha',
                    'priority': 'HIGH',
                    'voice_impact': 'Systematically organized Buddhist teachings',
                    'alternative_approaches': [
                        'Convert numerical groups separately (ones, twos, threes, etc.)',
                        'Focus on key numerical discourse collections',
                        'Use alternative Anguttara Nikaya editions'
                    ]
                }
            ]
        },
        
        'METADATA EXTRACTION ERRORS': {
            'reason': 'Conversion failed due to metadata extraction issues',
            'solution': 'Manual metadata specification or alternative extraction',
            'files': [
                {
                    'filename': 'The Trial and Death of Socrates (Third Edition): Euthyphro, Apology, Crito, Death Scene From Phaedo.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Plato',
                    'priority': 'HIGH',
                    'voice_impact': 'Socratic method and philosophical martyrdom',
                    'alternative_approaches': [
                        'Find individual dialogues (Apology, Crito, Phaedo separately)',
                        'Use alternative Plato editions',
                        'Manual metadata specification',
                        'Try different conversion tools'
                    ]
                },
                {
                    'filename': 'The Art of Living: The Classical Mannual on Virtue, Happiness, and Effectiveness.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Epictetus',
                    'priority': 'HIGH',
                    'voice_impact': 'Stoic practical philosophy',
                    'alternative_approaches': [
                        'Find alternative Epictetus editions (Discourses, Enchiridion)',
                        'Use different translation or publisher',
                        'Manual conversion with specified metadata',
                        'Try alternative stoic philosophy collections'
                    ]
                },
                {
                    'filename': 'John Donne: Collected Poetry.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'John Donne',
                    'priority': 'HIGH',
                    'voice_impact': 'Metaphysical poetry tradition',
                    'alternative_approaches': [
                        'Find individual Donne poetry collections',
                        'Use alternative metaphysical poetry anthologies',
                        'Manual metadata specification',
                        'Convert specific poem collections separately'
                    ]
                }
            ]
        },
        
        'COMPLEX MULTI-AUTHOR COLLECTIONS': {
            'reason': 'Multi-author collections with complex structure',
            'solution': 'Extract individual works or use alternative single-author editions',
            'files': [
                {
                    'filename': 'Complete Works of Xenophon (Illustrated) (Delphi Ancient Classics).epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Xenophon',
                    'priority': 'MEDIUM',
                    'voice_impact': 'Socratic historical perspective',
                    'alternative_approaches': [
                        'Extract individual Xenophon works (Anabasis, Memorabilia, etc.)',
                        'Use non-illustrated editions',
                        'Convert key works separately',
                        'Focus on most important Xenophon texts'
                    ]
                },
                {
                    'filename': 'The Sanskrit Epics - Delphi Poets Series.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Vyasa/Various',
                    'priority': 'HIGH',
                    'voice_impact': 'Hindu epic tradition (Mahabharata/Ramayana)',
                    'alternative_approaches': [
                        'Find separate Mahabharata and Ramayana editions',
                        'Use individual epic sections (Bhagavad Gita, etc.)',
                        'Convert epic segments separately',
                        'Use alternative Hindu epic collections'
                    ]
                },
                {
                    'filename': 'Hindu Myths: A Sourcebook Translated From the Sanskrit.epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Various/Wendy Doniger',
                    'priority': 'MEDIUM',
                    'voice_impact': 'Hindu mythological tradition',
                    'alternative_approaches': [
                        'Find individual Hindu mythological texts',
                        'Use thematic myth collections',
                        'Convert by deity or mythological cycle',
                        'Alternative Hindu mythology sourcebooks'
                    ]
                }
            ]
        },
        
        'LARGE SINGLE VOLUMES': {
            'reason': 'Single large volumes exceeding timeout limits',
            'solution': 'Chapter-by-chapter conversion or alternative editions',
            'files': [
                {
                    'filename': 'Delphi Complete Works of Athenaeus (Illustrated).epub',
                    'location': '/Users/davidglidden/Desktop/Myth:Buddha/',
                    'author': 'Athenaeus',
                    'priority': 'LOW',
                    'voice_impact': 'Ancient cultural and literary references',
                    'alternative_approaches': [
                        'Extract key sections of Deipnosophistae',
                        'Use selective Athenaeus anthologies',
                        'Convert by book/section',
                        'Focus on most relevant cultural content'
                    ]
                }
            ]
        },
        
        'CONVERSION TOOL LIMITATIONS': {
            'reason': 'Specific pandoc or conversion tool limitations',
            'solution': 'Try alternative conversion tools or manual processing',
            'files': [
                {
                    'filename': 'Various experimental and contemporary works',
                    'location': 'Multiple locations',
                    'author': 'Various',
                    'priority': 'VARIABLE',
                    'voice_impact': 'Contemporary philosophical voices',
                    'alternative_approaches': [
                        'Try alternative EPUB to Markdown tools',
                        'Use PDF versions if available',
                        'Manual text extraction',
                        'Alternative editions or formats'
                    ]
                }
            ]
        }
    }
    
    print("📊 FAILED CONVERSIONS SUMMARY:")
    total_failed = sum(len(category['files']) for category in failed_conversions.values())
    print(f"   ❌ Total failed conversions: {total_failed}")
    print(f"   📚 Successfully converted: 125")
    print(f"   📈 Success rate: {125/(125+total_failed)*100:.1f}%")
    print()
    
    # Generate detailed analysis for each category
    for category_name, category_data in failed_conversions.items():
        print(f"🔴 {category_name}")
        print(f"   📋 Reason: {category_data['reason']}")
        print(f"   💡 Solution: {category_data['solution']}")
        print(f"   📁 Files: {len(category_data['files'])}")
        print()
        
        for i, file_info in enumerate(category_data['files'], 1):
            print(f"   [{i}] 📖 {file_info['filename']}")
            print(f"       👤 Author: {file_info['author']}")
            print(f"       📍 Location: {file_info['location']}")
            print(f"       🎯 Priority: {file_info['priority']}")
            print(f"       🎭 Voice Impact: {file_info['voice_impact']}")
            print(f"       🔧 Alternative Approaches:")
            for approach in file_info['alternative_approaches']:
                print(f"           • {approach}")
            print()
    
    print("🎯 PRIORITY CONVERSION RECOMMENDATIONS:")
    print()
    
    print("🔥 CRITICAL PRIORITY (Essential for Chamber completion):")
    critical_files = []
    for category in failed_conversions.values():
        critical_files.extend([f for f in category['files'] if f['priority'] == 'CRITICAL'])
    
    for file_info in critical_files:
        print(f"   📖 {file_info['filename']}")
        print(f"       💡 Best approach: {file_info['alternative_approaches'][0]}")
        print()
    
    print("🟡 HIGH PRIORITY (Important for Chamber enhancement):")
    high_files = []
    for category in failed_conversions.values():
        high_files.extend([f for f in category['files'] if f['priority'] == 'HIGH'])
    
    for file_info in high_files[:5]:  # Show first 5 to keep manageable
        print(f"   📖 {file_info['filename']}")
        print(f"       💡 Best approach: {file_info['alternative_approaches'][0]}")
    if len(high_files) > 5:
        print(f"   ... and {len(high_files) - 5} more high priority files")
    print()
    
    print("🛠️ GENERAL ALTERNATIVE STRATEGIES:")
    print()
    print("📂 EPUB SPLITTING TOOLS:")
    print("   • Calibre: Convert to individual chapters")
    print("   • EPUB splitter tools: Break large files into segments")
    print("   • Manual extraction: Use EPUB directory structure")
    print()
    
    print("🔄 ALTERNATIVE CONVERSION APPROACHES:")
    print("   • epub2txt: Simple text extraction")
    print("   • Calibre conversion: Alternative EPUB processor")
    print("   • Manual HTML extraction: From EPUB directory structure")
    print("   • PDF versions: If EPUB conversion fails")
    print()
    
    print("📋 INDIVIDUAL WORK SOURCING:")
    print("   • Project Gutenberg: Free classical works")
    print("   • Internet Archive: Individual volume access")
    print("   • Alternative publishers: Different EPUB formats")
    print("   • Shorter editions: Abridged or selected works")
    print()
    
    print("✨ SUMMARY & NEXT STEPS:")
    print()
    print("The Chamber library conversion has been highly successful with 125 texts")
    print("converted. The failed conversions are primarily due to:")
    print()
    print("1. 🕒 TIMEOUT ISSUES: Very large collections (Jung, Harvard, Buddhist Nikayas)")
    print("2. 📊 METADATA ISSUES: Complex multi-author or illustrated collections")
    print("3. 🔧 TOOL LIMITATIONS: Specific pandoc conversion challenges")
    print()
    print("Most failures can be resolved through alternative approaches:")
    print("• Split large collections into smaller segments")
    print("• Find individual volumes of complete works")
    print("• Use alternative editions or formats")
    print("• Manual extraction for critical works")
    print()
    print("🎭 The Chamber is already comprehensively capable - these additions")
    print("    would enhance rather than fundamentally transform existing abilities.")

if __name__ == "__main__":
    create_failed_conversions_list()