#!/usr/bin/env python3
"""
Chamber Conversion Batch Processing
Automated conversion of acquired texts to Chamber format
"""

import subprocess
import yaml
import json
import shutil
from pathlib import Path
import time
import re

def extract_metadata_with_calibre(ebook_path):
    """Extract metadata using Calibre's ebook-meta tool"""
    
    try:
        result = subprocess.run([
            'ebook-meta', str(ebook_path)
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode != 0:
            print(f"⚠️  Calibre metadata extraction failed for {ebook_path.name}")
            return {}
        
        metadata = {}
        for line in result.stdout.split('\n'):
            if ':' in line:
                key, value = line.split(':', 1)
                key = key.strip().lower()
                value = value.strip()
                
                if key == 'title':
                    metadata['title'] = value
                elif key in ['author(s)', 'authors']:
                    # Handle multiple authors
                    authors = [a.strip() for a in value.split('&')]
                    metadata['author'] = authors[0] if authors else value
                    if len(authors) > 1:
                        metadata['additional_authors'] = authors[1:]
                elif key == 'published':
                    metadata['published'] = value
                elif key == 'publisher':
                    metadata['publisher'] = value
                elif key == 'language':
                    metadata['language'] = value
                elif key == 'series':
                    metadata['series'] = value
                elif key == 'tags':
                    metadata['tags'] = [tag.strip() for tag in value.split(',')]
        
        return metadata
    
    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        print(f"❌ Calibre not available or timeout: {e}")
        return {}
    except Exception as e:
        print(f"❌ Metadata extraction error for {ebook_path.name}: {e}")
        return {}

def convert_with_calibre_to_markdown(ebook_path, output_dir):
    """Convert ebook to Markdown using Calibre with optimal settings"""
    
    output_path = Path(output_dir) / f"{ebook_path.stem}.md"
    
    # Calibre conversion with Chamber-optimized settings
    calibre_cmd = [
        'ebook-convert',
        str(ebook_path),
        str(output_path),
        '--output-profile=tablet',
        '--preserve-cover-aspect-ratio',
        '--remove-first-image',  # Remove cover from text
        '--chapter-mark=pagebreak',
        '--page-breaks-before=/',  # Preserve chapter structure
        '--markdown-extensions=extra,codehilite',
        '--max-line-length=80',
        '--preserve-aspect-ratio',
        '--linearize-tables'
    ]
    
    try:
        print(f"🔄 Converting {ebook_path.name} to Markdown...")
        result = subprocess.run(calibre_cmd, capture_output=True, text=True, timeout=300)
        
        if result.returncode == 0:
            print(f"✅ Successfully converted: {ebook_path.name}")
            return output_path
        else:
            print(f"❌ Calibre conversion failed for {ebook_path.name}")
            print(f"   Error: {result.stderr}")
            return None
            
    except subprocess.TimeoutExpired:
        print(f"❌ Conversion timeout for {ebook_path.name}")
        return None
    except Exception as e:
        print(f"❌ Conversion error for {ebook_path.name}: {e}")
        return None

def generate_chamber_yaml_frontmatter(metadata, ebook_path, conversion_method="calibre"):
    """Generate Chamber YAML frontmatter with voice role assignment"""
    
    # Extract basic info
    author = metadata.get('author', ebook_path.stem.split('-')[0] if '-' in ebook_path.stem else 'Unknown Author')
    title = metadata.get('title', ebook_path.stem)
    
    # Clean up author name (remove common artifacts)
    author = re.sub(r'\[.*?\]', '', author).strip()
    author = re.sub(r'\(.*?\)', '', author).strip()
    
    # Comprehensive voice role mapping
    voice_roles = {
        # Eastern Philosophy & Buddhism
        'd.t. suzuki': 'Zen Scholar and East-West Bridge Builder',
        'suzuki': 'Zen Scholar and East-West Bridge Builder', 
        'dogen': 'Zen Master of Being-Time and Buddha Nature',
        'zhuangzi': 'Taoist Master of Transformation and Wu Wei',
        'huang po': 'Chan Master of No-Mind and Direct Pointing',
        'nagarjuna': 'Buddhist Philosopher of Middle Way Emptiness',
        'shankara': 'Advaita Vedanta Master of Non-Dual Reality',
        'krishnamurti': 'Radical Spiritual Teacher and Truth Seeker',
        'patanjali': 'Yoga Philosophy Systematizer',
        'bodhidharma': 'First Chan Patriarch and Wall-Gazing Master',
        'huineng': 'Sixth Patriarch of Sudden Enlightenment',
        
        # Western Philosophy
        'maurice merleau-ponty': 'Phenomenologist of Embodied Perception',
        'merleau-ponty': 'Phenomenologist of Embodied Perception',
        'jane jacobs': 'Urban Theorist and Community Organizer',
        'richard sennett': 'Sociologist of Craft and Labor',
        'martha nussbaum': 'Ethics and Literature Philosopher',
        'donna haraway': 'Feminist Theorist of Posthuman Futures',
        'jacques derrida': 'Deconstructionist Philosopher',
        'maurice merleau': 'Phenomenologist of Embodied Perception',
        
        # Literature & Poetry
        'virginia woolf': 'Modernist Writer and Feminist Theorist',
        'anne carson': 'Classical Scholar and Contemporary Poet',
        'ursula k. le guin': 'Science Fiction Philosopher and Taoist',
        'ursula le guin': 'Science Fiction Philosopher and Taoist',
        'octavia butler': 'Afrofuturist Visionary and Social Prophet',
        'clarice lispector': 'Brazilian Philosophical Novelist',
        'toni morrison': 'American Memory and Healing Novelist',
        'marcel proust': 'Memory and Time Literary Philosopher',
        'james joyce': 'Stream of Consciousness Revolutionary',
        'jane austen': 'Social Architecture Novelist',
        'charles dickens': 'Industrial Society Critic and Humanist',
        'gertrude stein': 'Experimental Language Pioneer',
        
        # Mystical Traditions
        'rumi': 'Sufi Mystic and Ecstatic Poet',
        'hafiz': 'Persian Mystic and Divine Intoxication Poet',
        'william blake': 'Visionary Poet and Engraver of Infinity',
        'meister eckhart': 'Christian Mystic of Divine Detachment',
        'hildegard of bingen': 'Medieval Visionary and Universal Genius',
        'john of the cross': 'Mystical Theologian of Dark Night',
        'teresa of avila': 'Mystic of Interior Castle',
        
        # Classical Philosophy
        'sappho': 'Ancient Lyric Poet of Lesbian Love',
        'heraclitus': 'Pre-Socratic Philosopher of Flow and Change',
        'parmenides': 'Philosopher of Being and Unity',
        'plotinus': 'Neoplatonic Philosopher of Emanation',
        'augustine': 'Christian Philosopher and Spiritual Autobiographer',
        'aquinas': 'Scholastic Synthesizer of Faith and Reason',
        'hypatia': 'Ancient Mathematician and Philosopher'
    }
    
    # Find voice role
    author_key = author.lower().strip()
    voice_role = voice_roles.get(author_key, 'Philosophical Voice and Cultural Contributor')
    
    # If no direct match, try partial matching
    if voice_role == 'Philosophical Voice and Cultural Contributor':
        for key, role in voice_roles.items():
            if key in author_key or any(part in author_key for part in key.split()):
                voice_role = role
                break
    
    # Determine tradition
    traditions = {
        'zen_buddhist': ['suzuki', 'dogen', 'huang po', 'zen', 'chan'],
        'taoist': ['zhuangzi', 'laozi', 'tao te ching'],
        'buddhist': ['buddha', 'nagarjuna', 'dharma', 'buddhist'],
        'hindu_vedantic': ['shankara', 'patanjali', 'yoga', 'vedanta'],
        'western_phenomenology': ['merleau-ponty', 'phenomenology'],
        'urban_planning': ['jacobs', 'urban', 'city'],
        'feminist_philosophy': ['woolf', 'nussbaum', 'haraway', 'morrison'],
        'mystical_christian': ['eckhart', 'john of the cross', 'teresa'],
        'mystical_islamic': ['rumi', 'hafiz', 'sufi'],
        'modernist_literature': ['woolf', 'joyce', 'proust', 'stein'],
        'speculative_fiction': ['le guin', 'butler', 'science fiction'],
        'classical_philosophy': ['sappho', 'heraclitus', 'plotinus', 'augustine'],
        'contemporary_critical': ['sennett', 'derrida', 'critical theory']
    }
    
    tradition = 'Unknown'
    search_text = f"{author} {title}".lower()
    for trad, keywords in traditions.items():
        if any(keyword in search_text for keyword in keywords):
            tradition = trad
            break
    
    # Build YAML frontmatter
    yaml_frontmatter = {
        'title': title,
        'author': author,
        'voice': author,
        'voice_role': voice_role,
        'source_type': 'literary_work',
        'tradition': tradition,
        'language': metadata.get('language', 'en'),
        'publisher': metadata.get('publisher', 'Unknown'),
        'publication_date': metadata.get('published', 'Unknown'),
        'converted_date': '2025-06-18',
        'conversion_method': conversion_method,
        'chamber_integration': 'ready'
    }
    
    # Add optional metadata if available
    if 'series' in metadata:
        yaml_frontmatter['series'] = metadata['series']
    if 'tags' in metadata:
        yaml_frontmatter['tags'] = metadata['tags']
    if 'additional_authors' in metadata:
        yaml_frontmatter['additional_authors'] = metadata['additional_authors']
    
    return yaml_frontmatter

def add_chamber_yaml_to_markdown(markdown_path, yaml_frontmatter):
    """Add Chamber YAML frontmatter to converted Markdown file"""
    
    try:
        # Read existing content
        with open(markdown_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Generate YAML header
        yaml_header = "---\n"
        yaml_header += yaml.dump(yaml_frontmatter, default_flow_style=False, allow_unicode=True)
        yaml_header += "---\n\n"
        
        # Combine with content
        chamber_content = yaml_header + content
        
        # Write back to file
        with open(markdown_path, 'w', encoding='utf-8') as f:
            f.write(chamber_content)
        
        print(f"✅ Added Chamber YAML frontmatter to {markdown_path.name}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to add YAML frontmatter to {markdown_path.name}: {e}")
        return False

def batch_convert_ebooks_to_chamber_format(acquisition_dir, output_dir):
    """Batch convert all ebooks to Chamber-ready format"""
    
    # Create output directory
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Find all ebook files
    ebook_patterns = ['*.epub', '*.pdf', '*.mobi', '*.azw3']
    ebook_files = []
    for pattern in ebook_patterns:
        ebook_files.extend(list(Path(acquisition_dir).rglob(pattern)))
    
    print(f"🔄 CHAMBER BATCH CONVERSION")
    print(f"Found {len(ebook_files)} ebook files to convert")
    print(f"Output directory: {output_path.absolute()}")
    print()
    
    successful_conversions = []
    failed_conversions = []
    
    for i, ebook_path in enumerate(ebook_files, 1):
        print(f"[{i}/{len(ebook_files)}] Processing: {ebook_path.name}")
        
        try:
            # Extract metadata
            metadata = extract_metadata_with_calibre(ebook_path)
            
            # Convert to Markdown
            markdown_path = convert_with_calibre_to_markdown(ebook_path, output_path)
            
            if markdown_path and markdown_path.exists():
                # Generate Chamber YAML frontmatter
                yaml_frontmatter = generate_chamber_yaml_frontmatter(
                    metadata, ebook_path, "calibre"
                )
                
                # Add YAML frontmatter to file
                if add_chamber_yaml_to_markdown(markdown_path, yaml_frontmatter):
                    successful_conversions.append({
                        'original_file': str(ebook_path),
                        'converted_file': str(markdown_path),
                        'voice': yaml_frontmatter['voice'],
                        'voice_role': yaml_frontmatter['voice_role'],
                        'tradition': yaml_frontmatter['tradition']
                    })
                    print(f"✅ Successfully converted: {ebook_path.name}")
                else:
                    failed_conversions.append({
                        'file': str(ebook_path),
                        'reason': 'YAML frontmatter addition failed'
                    })
            else:
                failed_conversions.append({
                    'file': str(ebook_path),
                    'reason': 'Calibre conversion failed'
                })
        
        except Exception as e:
            failed_conversions.append({
                'file': str(ebook_path),
                'reason': f'Unexpected error: {e}'
            })
            print(f"❌ Error processing {ebook_path.name}: {e}")
        
        print()
    
    # Generate conversion report
    print("📊 CONVERSION SUMMARY")
    print("=" * 40)
    print(f"✅ Successful conversions: {len(successful_conversions)}")
    print(f"❌ Failed conversions: {len(failed_conversions)}")
    print()
    
    if successful_conversions:
        print("✅ SUCCESSFULLY CONVERTED VOICES:")
        for conversion in successful_conversions:
            voice = conversion['voice']
            role = conversion['voice_role']
            print(f"   • {voice}: {role}")
        print()
    
    if failed_conversions:
        print("❌ FAILED CONVERSIONS:")
        for failure in failed_conversions:
            file_name = Path(failure['file']).name
            reason = failure['reason']
            print(f"   • {file_name}: {reason}")
        print()
    
    # Save detailed conversion report
    report = {
        'conversion_date': '2025-06-18',
        'total_attempted': len(ebook_files),
        'successful': len(successful_conversions),
        'failed': len(failed_conversions),
        'successful_conversions': successful_conversions,
        'failed_conversions': failed_conversions
    }
    
    report_file = output_path / "conversion_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📄 Detailed conversion report saved: {report_file}")
    
    # Analyze voice coverage
    traditions_added = {}
    for conversion in successful_conversions:
        tradition = conversion['tradition']
        traditions_added[tradition] = traditions_added.get(tradition, 0) + 1
    
    print("🏛️ CHAMBER ENHANCEMENT ANALYSIS:")
    print(f"   🎭 New voices added: {len(successful_conversions)}")
    print(f"   🌍 Traditions enhanced: {len(traditions_added)}")
    for tradition, count in sorted(traditions_added.items()):
        print(f"   • {tradition}: {count} voices")
    print()
    
    return successful_conversions, failed_conversions

def main():
    """Main batch conversion function"""
    
    # Check for required tools
    try:
        subprocess.run(['ebook-convert', '--version'], capture_output=True, check=True)
        print("✅ Calibre found and ready")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Calibre not found! Please install Calibre first.")
        print("   Visit: https://calibre-ebook.com/download")
        return
    
    # Look for acquisition directory
    acquisition_dir = Path("chamber_acquisitions")
    if not acquisition_dir.exists():
        print("❌ Chamber acquisitions directory not found!")
        print("   Run download_automation.py first to acquire texts.")
        return
    
    # Set up output directory
    output_dir = acquisition_dir / "converted_chamber_format"
    
    # Run batch conversion
    successful, failed = batch_convert_ebooks_to_chamber_format(acquisition_dir, output_dir)
    
    print("🎯 NEXT STEPS:")
    print("1. Review converted files in chamber_format directory")
    print("2. Validate YAML frontmatter and voice assignments")
    print("3. Copy validated files to main Chamber library")
    print("4. Test Chamber dialogues with new voices")
    print("5. Update Chamber documentation with new voice count")
    print()
    print(f"🚀 Chamber expansion: +{len(successful)} voices ready for integration!")

if __name__ == "__main__":
    main()