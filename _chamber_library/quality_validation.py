#!/usr/bin/env python3
"""
Chamber Library Quality Validation
Validate downloaded texts for Chamber conversion readiness
"""

import os
import zipfile
import xml.etree.ElementTree as ET
import json
import yaml
from pathlib import Path
import subprocess

def validate_epub_quality(epub_path):
    """Validate EPUB file for Chamber conversion"""
    
    issues = []
    metadata = {}
    
    try:
        with zipfile.ZipFile(epub_path, 'r') as epub:
            # Check for required files
            file_list = epub.namelist()
            
            if 'META-INF/container.xml' not in file_list:
                issues.append("Missing container.xml")
            
            # Check for content.opf
            opf_files = [f for f in file_list if f.endswith('.opf')]
            if not opf_files:
                issues.append("Missing content.opf file")
            
            # Check for actual content files
            content_files = [f for f in file_list if f.endswith('.html') or f.endswith('.xhtml')]
            if len(content_files) < 1:
                issues.append("No content files found")
            else:
                metadata['content_file_count'] = len(content_files)
            
            # Check for images
            image_files = [f for f in file_list if any(f.endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.svg'])]
            metadata['image_count'] = len(image_files)
            
            # Check metadata
            try:
                container = epub.read('META-INF/container.xml')
                container_tree = ET.fromstring(container)
                
                # Find OPF file path
                opf_path = None
                for rootfile in container_tree.findall('.//{urn:oasis:names:tc:opendocument:xmlns:container}rootfile'):
                    opf_path = rootfile.get('full-path')
                    break
                
                if opf_path and opf_path in file_list:
                    opf_content = epub.read(opf_path)
                    opf_tree = ET.fromstring(opf_content)
                    
                    # Extract metadata
                    title_elem = opf_tree.find('.//{http://purl.org/dc/elements/1.1/}title')
                    author_elem = opf_tree.find('.//{http://purl.org/dc/elements/1.1/}creator')
                    publisher_elem = opf_tree.find('.//{http://purl.org/dc/elements/1.1/}publisher')
                    date_elem = opf_tree.find('.//{http://purl.org/dc/elements/1.1/}date')
                    language_elem = opf_tree.find('.//{http://purl.org/dc/elements/1.1/}language')
                    
                    if title_elem is not None:
                        metadata['title'] = title_elem.text
                    else:
                        issues.append("Missing title metadata")
                    
                    if author_elem is not None:
                        metadata['author'] = author_elem.text
                    else:
                        issues.append("Missing author metadata")
                    
                    if publisher_elem is not None:
                        metadata['publisher'] = publisher_elem.text
                    
                    if date_elem is not None:
                        metadata['publication_date'] = date_elem.text
                    
                    if language_elem is not None:
                        metadata['language'] = language_elem.text
                    else:
                        metadata['language'] = 'en'  # Assume English if not specified
                
            except Exception as e:
                issues.append(f"Metadata validation error: {e}")
    
    except zipfile.BadZipFile:
        issues.append("Corrupted EPUB file")
    except Exception as e:
        issues.append(f"EPUB structure error: {e}")
    
    return issues, metadata

def validate_pdf_quality(pdf_path):
    """Basic validation for PDF files"""
    
    issues = []
    metadata = {}
    
    try:
        # Check if file can be opened
        file_size = pdf_path.stat().st_size
        metadata['file_size'] = file_size
        
        if file_size < 1000:  # Less than 1KB is suspicious
            issues.append("File suspiciously small")
        
        # Try to extract metadata using pdfinfo if available
        try:
            result = subprocess.run(['pdfinfo', str(pdf_path)], 
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                for line in result.stdout.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        key = key.strip().lower().replace(' ', '_')
                        value = value.strip()
                        if value:
                            metadata[key] = value
        except (subprocess.TimeoutExpired, FileNotFoundError):
            # pdfinfo not available or timeout
            pass
        
    except Exception as e:
        issues.append(f"PDF validation error: {e}")
    
    return issues, metadata

def determine_conversion_method(file_path, issues):
    """Determine the best conversion method based on file and issues"""
    
    if file_path.suffix.lower() == '.epub':
        if not issues:
            return "pandoc_ready"
        elif len(issues) <= 2 and not any('structure error' in issue.lower() for issue in issues):
            return "calibre_recommended"
        else:
            return "calibre_required"
    elif file_path.suffix.lower() == '.pdf':
        return "calibre_required"  # PDFs generally need Calibre
    else:
        return "manual_processing"

def generate_chamber_yaml_template(metadata, file_path):
    """Generate Chamber YAML frontmatter template based on metadata"""
    
    # Extract voice information
    author = metadata.get('author', 'Unknown Author')
    title = metadata.get('title', file_path.stem)
    
    # Determine voice role based on known patterns
    voice_roles = {
        'suzuki': 'Zen Scholar and East-West Bridge Builder',
        'merleau-ponty': 'Phenomenologist of Embodied Perception', 
        'woolf': 'Modernist Writer and Feminist Theorist',
        'sennett': 'Sociologist of Craft and Labor',
        'carson': 'Classical Scholar and Contemporary Poet',
        'zhuangzi': 'Taoist Master of Transformation',
        'dogen': 'Zen Master of Being-Time',
        'jacobs': 'Urban Theorist and Community Organizer',
        'le guin': 'Science Fiction Philosopher',
        'butler': 'Afrofuturist Visionary',
        'rumi': 'Sufi Mystic and Ecstatic Poet',
        'blake': 'Visionary Poet and Engraver',
        'woolf': 'Stream of Consciousness Pioneer',
        'joyce': 'Modernist Literary Revolutionary',
        'proust': 'Memory and Time Philosopher',
        'austen': 'Social Architecture Novelist',
        'dickens': 'Industrial Society Critic'
    }
    
    # Find matching voice role
    voice_role = 'Philosophical Voice and Cultural Contributor'  # Default
    author_lower = author.lower()
    for key, role in voice_roles.items():
        if key in author_lower or key in title.lower():
            voice_role = role
            break
    
    # Determine tradition based on content
    traditions = {
        'zen': ['suzuki', 'dogen', 'huang po', 'zen'],
        'taoist': ['zhuangzi', 'laozi', 'tao'],
        'buddhist': ['buddha', 'nagarjuna', 'dharma'],
        'western_philosophy': ['merleau-ponty', 'phenomenology'],
        'literature': ['woolf', 'joyce', 'proust', 'austen', 'dickens'],
        'mystical': ['rumi', 'hafiz', 'eckhart', 'teresa', 'john of the cross'],
        'contemporary': ['sennett', 'jacobs', 'carson', 'le guin', 'butler']
    }
    
    tradition = 'Unknown'
    search_text = f"{author} {title}".lower()
    for trad, keywords in traditions.items():
        if any(keyword in search_text for keyword in keywords):
            tradition = trad
            break
    
    yaml_template = {
        'title': title,
        'author': author,
        'voice': author,
        'voice_role': voice_role,
        'source_type': 'literary_work',
        'tradition': tradition,
        'language': metadata.get('language', 'en'),
        'publisher': metadata.get('publisher', 'Unknown'),
        'publication_date': metadata.get('publication_date', 'Unknown'),
        'converted_date': '2025-06-18',
        'conversion_method': 'pending',
        'chamber_integration': 'ready',
        'file_info': {
            'original_format': file_path.suffix.lower(),
            'file_size': metadata.get('file_size', 'Unknown'),
            'content_files': metadata.get('content_file_count', 'Unknown')
        }
    }
    
    return yaml_template

def categorize_by_conversion_method(acquisition_dir):
    """Categorize files by required conversion method"""
    
    categories = {
        'pandoc_ready': [],
        'calibre_recommended': [],
        'calibre_required': [],
        'manual_processing': []
    }
    
    # Find all ebook files
    ebook_files = []
    for pattern in ['*.epub', '*.pdf', '*.txt', '*.html']:
        ebook_files.extend(list(Path(acquisition_dir).rglob(pattern)))
    
    validation_results = []
    
    for file_path in ebook_files:
        if file_path.suffix.lower() == '.epub':
            issues, metadata = validate_epub_quality(file_path)
        elif file_path.suffix.lower() == '.pdf':
            issues, metadata = validate_pdf_quality(file_path)
        else:
            issues, metadata = [], {'file_size': file_path.stat().st_size}
        
        conversion_method = determine_conversion_method(file_path, issues)
        categories[conversion_method].append(file_path)
        
        # Generate Chamber YAML template
        yaml_template = generate_chamber_yaml_template(metadata, file_path)
        
        validation_results.append({
            'file': file_path.name,
            'path': str(file_path),
            'format': file_path.suffix.lower(),
            'conversion_method': conversion_method,
            'issues': issues,
            'metadata': metadata,
            'chamber_yaml': yaml_template
        })
    
    return categories, validation_results

def generate_comprehensive_quality_report(acquisition_dir):
    """Generate comprehensive quality report for all downloaded files"""
    
    print("🔍 CHAMBER LIBRARY QUALITY VALIDATION")
    print("=" * 50)
    print()
    
    categories, validation_results = categorize_by_conversion_method(acquisition_dir)
    
    # Summary statistics
    total_files = len(validation_results)
    ready_files = len(categories['pandoc_ready'])
    calibre_files = len(categories['calibre_recommended']) + len(categories['calibre_required'])
    problem_files = len(categories['manual_processing'])
    
    print(f"📊 VALIDATION SUMMARY:")
    print(f"   📚 Total files processed: {total_files}")
    print(f"   ✅ Ready for pandoc: {ready_files}")
    print(f"   🔧 Need Calibre: {calibre_files}")
    print(f"   ⚠️  Need manual processing: {problem_files}")
    print()
    
    # Detailed breakdown by category
    for category, files in categories.items():
        if files:
            print(f"📋 {category.upper().replace('_', ' ')} ({len(files)} files):")
            for file_path in files[:5]:  # Show first 5
                print(f"   • {file_path.name}")
            if len(files) > 5:
                print(f"   • ... and {len(files) - 5} more files")
            print()
    
    # Quality issues summary
    all_issues = []
    for result in validation_results:
        all_issues.extend(result['issues'])
    
    if all_issues:
        issue_counts = {}
        for issue in all_issues:
            issue_counts[issue] = issue_counts.get(issue, 0) + 1
        
        print("⚠️  COMMON ISSUES FOUND:")
        for issue, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True):
            print(f"   • {issue}: {count} files")
        print()
    
    # Chamber integration readiness
    traditions_found = {}
    for result in validation_results:
        tradition = result['chamber_yaml']['tradition']
        traditions_found[tradition] = traditions_found.get(tradition, 0) + 1
    
    print("🏛️ CHAMBER INTEGRATION ANALYSIS:")
    print(f"   🌍 Philosophical traditions represented: {len(traditions_found)}")
    for tradition, count in sorted(traditions_found.items()):
        print(f"   • {tradition}: {count} texts")
    print()
    
    # Save detailed report
    report_file = Path(acquisition_dir) / "quality_validation_report.json"
    detailed_report = {
        'validation_date': '2025-06-18',
        'summary': {
            'total_files': total_files,
            'pandoc_ready': ready_files,
            'calibre_needed': calibre_files,
            'manual_processing': problem_files
        },
        'categories': {k: [str(p) for p in v] for k, v in categories.items()},
        'detailed_results': validation_results,
        'traditions_represented': traditions_found
    }
    
    with open(report_file, 'w') as f:
        json.dump(detailed_report, f, indent=2)
    
    print(f"📄 Detailed validation report saved: {report_file}")
    
    # Generate conversion priority list
    print("🎯 CONVERSION PRIORITY RECOMMENDATIONS:")
    print()
    
    high_priority = [r for r in validation_results if r['conversion_method'] == 'pandoc_ready']
    medium_priority = [r for r in validation_results if r['conversion_method'] == 'calibre_recommended']
    
    if high_priority:
        print("🚀 HIGH PRIORITY (Ready for immediate conversion):")
        for result in high_priority[:10]:
            author = result['chamber_yaml']['author']
            title = result['chamber_yaml']['title']
            print(f"   • {author} - {title}")
        print()
    
    if medium_priority:
        print("⚡ MEDIUM PRIORITY (Calibre conversion recommended):")
        for result in medium_priority[:10]:
            author = result['chamber_yaml']['author']
            title = result['chamber_yaml']['title']
            print(f"   • {author} - {title}")
        print()
    
    return validation_results, categories

def main():
    """Main quality validation function"""
    
    # Look for acquisition directory
    acquisition_dir = Path("chamber_acquisitions")
    
    if not acquisition_dir.exists():
        print("❌ Chamber acquisitions directory not found!")
        print("   Run download_automation.py first to set up acquisitions.")
        return
    
    # Run comprehensive validation
    validation_results, categories = generate_comprehensive_quality_report(acquisition_dir)
    
    print("✅ Quality validation complete!")
    print()
    print("🔄 NEXT STEPS:")
    print("1. Review validation report and resolve any issues")
    print("2. Start with pandoc_ready files for immediate conversion")
    print("3. Process calibre_recommended files through Calibre")
    print("4. Address manual_processing files individually")
    print("5. Run batch conversion script on validated files")

if __name__ == "__main__":
    main()