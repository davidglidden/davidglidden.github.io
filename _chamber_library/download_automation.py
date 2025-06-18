#!/usr/bin/env python3
"""
Chamber Acquisition Automation
Systematic download and organization of Chamber library texts
"""

import requests
import os
import time
import json
from pathlib import Path

def setup_acquisition_environment():
    """Create organized directory structure for acquisitions"""
    
    base_dir = Path("chamber_acquisitions")
    
    directories = [
        "phase_1_critical_bridge/public_domain",
        "phase_1_critical_bridge/commercial", 
        "phase_1_critical_bridge/academic",
        "phase_2_literature_contemporary",
        "phase_3_historical_mystical",
        "phase_4_specialized",
        "conversion_ready",
        "needs_calibre_processing",
        "quality_check_required",
        "converted_chamber_format"
    ]
    
    for directory in directories:
        (base_dir / directory).mkdir(parents=True, exist_ok=True)
    
    print(f"✅ Created directory structure in: {base_dir.absolute()}")
    return base_dir

def download_internet_archive_item(identifier, target_dir, title="Unknown"):
    """Download items from Internet Archive"""
    
    base_url = f"https://archive.org/download/{identifier}"
    metadata_url = f"https://archive.org/metadata/{identifier}"
    
    try:
        # Get metadata to find best format
        print(f"📡 Fetching metadata for: {title}")
        response = requests.get(metadata_url, timeout=30)
        response.raise_for_status()
        metadata = response.json()
        
        # Prefer EPUB, then PDF, then other formats
        best_file = None
        format_priority = ['.epub', '.pdf', '.txt', '.html']
        
        for format_ext in format_priority:
            for file_info in metadata.get('files', []):
                if file_info.get('name', '').endswith(format_ext):
                    best_file = file_info
                    break
            if best_file:
                break
        
        if best_file:
            download_url = f"{base_url}/{best_file['name']}"
            
            # Clean filename for local storage
            safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).rstrip()
            extension = Path(best_file['name']).suffix
            filename = Path(target_dir) / f"{safe_title}{extension}"
            
            print(f"⬇️  Downloading: {best_file['name']} ({best_file.get('size', 'Unknown size')})")
            
            response = requests.get(download_url, timeout=60, stream=True)
            response.raise_for_status()
            
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            print(f"✅ Downloaded: {title} -> {filename.name}")
            return filename
        else:
            print(f"⚠️  No suitable format found for: {title}")
            return None
            
    except Exception as e:
        print(f"❌ Error downloading {title}: {e}")
        return None

# Internet Archive identifiers for immediate targets
INTERNET_ARCHIVE_TARGETS = {
    # Phase 1 Critical Bridge - Public Domain
    "Virginia Woolf - A Room of One's Own": "aroomofonesoown00wool",
    "Virginia Woolf - The Waves": "cu31924027248568", 
    "D.T. Suzuki - Essays in Zen Buddhism": "essaysinzenbud00suzuuoft",
    "D.T. Suzuki - Introduction to Zen Buddhism": "zenbuddhismselec00suzurich",
    "Zhuangzi - Complete Works": "completeworksofz00zhuu",
    "Huang Po - Zen Teaching": "zenteachingofhua00huan",
    "Shunryu Suzuki - Zen Mind Beginner's Mind": "zenmindbeginners00suzus",
    "Jane Jacobs - Death and Life of Great American Cities": "deathlifeofgreat00jaco",
    "William Blake - Complete Poetry and Prose": "completepoetrypr00blak",
    "John Keats - Complete Poems": "completepoemsof00keatuoft",
    
    # Buddhist and Eastern Sources
    "Patanjali - Yoga Sutras": "yogasutrasofpat00pata",
    "Bodhidharma - Zen Teaching": "zenteachingofbo00bodh",
    "Platform Sutra of Sixth Patriarch": "platformsutraof00huinuoft",
    "Nagarjuna - Middle Way Philosophy": "fundamentalwisdo00naga",
    
    # Classical Philosophy
    "Plotinus - Enneads": "plotinusenneads00plot",
    "Augustine - Confessions": "confessionsofsa00augu",
    "Aquinas - Summa Theologica": "summatheologica00thom",
    "Sappho - Complete Poems": "completepoemssa00sapp",
    "Heraclitus - Fragments": "fragmentsofhera00hera",
    
    # Mystical Traditions
    "Rumi - Essential Rumi": "essentialrumi00rumi",
    "Hafiz - Divan": "divanofhafiz00hafi",
    "Meister Eckhart - Selected Writings": "selectedwriting00ecka",
    "Hildegard of Bingen - Scivias": "sciviashildegar00hild",
    "John of the Cross - Dark Night": "darknightofthes00john",
    "Teresa of Avila - Interior Castle": "interiorcastle00tere",
    
    # Literature Classics
    "Marcel Proust - Swann's Way": "swannsway00prou",
    "James Joyce - Ulysses": "ulysses00joyc",
    "Jane Austen - Pride and Prejudice": "prideandprejudi00aust",
    "Charles Dickens - Hard Times": "hardtimes00dick",
    "Gertrude Stein - Three Lives": "threelives00stei"
}

def batch_download_public_domain(base_dir):
    """Download all available public domain targets"""
    
    public_domain_dir = base_dir / "phase_1_critical_bridge" / "public_domain"
    
    downloaded = []
    failed = []
    
    print(f"🚀 Starting batch download of {len(INTERNET_ARCHIVE_TARGETS)} public domain texts")
    print(f"📁 Target directory: {public_domain_dir.absolute()}")
    print()
    
    for i, (title, identifier) in enumerate(INTERNET_ARCHIVE_TARGETS.items(), 1):
        print(f"[{i}/{len(INTERNET_ARCHIVE_TARGETS)}] Processing: {title}")
        
        try:
            result = download_internet_archive_item(identifier, public_domain_dir, title)
            if result:
                downloaded.append((title, result))
                print(f"✅ Success: {title}")
            else:
                failed.append((title, "No suitable format found"))
                print(f"⚠️  Failed: {title} - No suitable format")
            
            # Respectful delay to avoid overwhelming the server
            print("⏱️  Waiting 3 seconds...")
            time.sleep(3)
            print()
            
        except Exception as e:
            failed.append((title, str(e)))
            print(f"❌ Error: {title} - {e}")
            print()
    
    # Generate download report
    print("📊 DOWNLOAD SUMMARY")
    print("=" * 50)
    print(f"✅ Successfully downloaded: {len(downloaded)} texts")
    print(f"❌ Failed downloads: {len(failed)} texts")
    print()
    
    if downloaded:
        print("✅ SUCCESSFUL DOWNLOADS:")
        for title, filepath in downloaded:
            print(f"   • {title}")
        print()
    
    if failed:
        print("❌ FAILED DOWNLOADS:")
        for title, reason in failed:
            print(f"   • {title}: {reason}")
        print()
    
    # Save detailed report
    report = {
        'download_date': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_attempted': len(INTERNET_ARCHIVE_TARGETS),
        'successful': len(downloaded),
        'failed': len(failed),
        'downloaded_files': [{'title': title, 'path': str(filepath)} for title, filepath in downloaded],
        'failed_files': [{'title': title, 'reason': reason} for title, reason in failed]
    }
    
    report_file = public_domain_dir / "download_report.json"
    with open(report_file, 'w') as f:
        json.dump(report, f, indent=2)
    
    print(f"📄 Detailed report saved: {report_file}")
    
    return downloaded, failed

def generate_acquisition_list():
    """Generate a structured list of remaining commercial acquisitions needed"""
    
    commercial_targets = {
        "Phase 1 Critical Bridge - Commercial": [
            {
                "title": "Phenomenology of Perception",
                "author": "Maurice Merleau-Ponty", 
                "isbn": "978-0415834339",
                "publisher": "Routledge",
                "estimated_price": "$31.99",
                "priority": "Essential",
                "sources": ["Amazon Kindle", "Apple Books", "Routledge Direct"]
            },
            {
                "title": "The Craftsman",
                "author": "Richard Sennett",
                "isbn": "978-0300151909", 
                "publisher": "Yale University Press",
                "estimated_price": "$14.99",
                "priority": "Essential",
                "sources": ["Amazon", "Yale Press", "Academic Libraries"]
            },
            {
                "title": "Autobiography of Red",
                "author": "Anne Carson",
                "isbn": "978-0375701412",
                "publisher": "Vintage Books", 
                "estimated_price": "$11.99",
                "priority": "Essential",
                "sources": ["Amazon Kindle", "Apple Books", "Local Bookstores"]
            },
            {
                "title": "Shobogenzo: Treasury of the True Dharma Eye",
                "author": "Dōgen",
                "isbn": "978-1590309353",
                "publisher": "Shambhala Publications",
                "estimated_price": "$24.95", 
                "priority": "Essential",
                "sources": ["Amazon", "Shambhala Direct", "Buddhist Centers"]
            },
            {
                "title": "The Fundamental Wisdom of the Middle Way",
                "author": "Nagarjuna",
                "isbn": "978-0195093360",
                "publisher": "Oxford University Press",
                "estimated_price": "$31.95",
                "priority": "High",
                "sources": ["Amazon", "Oxford Academic", "University Libraries"]
            }
        ],
        
        "Phase 1 - Specialized Buddhist": [
            {
                "title": "Crest-Jewel of Discrimination", 
                "author": "Shankara",
                "isbn": "978-0874810226",
                "publisher": "Vedanta Press",
                "estimated_price": "$12.95",
                "priority": "High",
                "sources": ["Vedanta Society", "Amazon", "Hindu Philosophy Publishers"]
            },
            {
                "title": "Freedom from the Known",
                "author": "Krishnamurti", 
                "isbn": "978-0060648084",
                "publisher": "HarperOne",
                "estimated_price": "$13.99",
                "priority": "Medium",
                "sources": ["Amazon", "Krishnamurti Foundation", "Philosophy Sections"]
            }
        ]
    }
    
    return commercial_targets

def print_commercial_acquisition_guide(base_dir):
    """Print organized guide for commercial acquisitions"""
    
    targets = generate_acquisition_list()
    
    print("🛒 COMMERCIAL ACQUISITION GUIDE")
    print("=" * 60)
    print()
    
    total_estimated_cost = 0
    
    for category, items in targets.items():
        print(f"📋 {category}:")
        print()
        
        category_cost = 0
        for item in items:
            price_str = item['estimated_price'].replace('$', '')
            try:
                price = float(price_str)
                category_cost += price
            except:
                pass
                
            print(f"   📚 {item['title']}")
            print(f"      Author: {item['author']}")
            print(f"      ISBN: {item['isbn']}")
            print(f"      Publisher: {item['publisher']}")
            print(f"      Price: {item['estimated_price']}")
            print(f"      Priority: {item['priority']}")
            print(f"      Sources: {', '.join(item['sources'])}")
            print()
        
        print(f"   💰 Category subtotal: ~${category_cost:.2f}")
        print()
        total_estimated_cost += category_cost
    
    print(f"💰 TOTAL ESTIMATED COST: ~${total_estimated_cost:.2f}")
    print()
    
    # Save commercial acquisition list
    commercial_list_file = base_dir / "commercial_acquisition_list.json"
    with open(commercial_list_file, 'w') as f:
        json.dump(targets, f, indent=2)
    
    print(f"📄 Commercial acquisition list saved: {commercial_list_file}")

def main():
    """Main acquisition automation function"""
    
    print("🏛️ CHAMBER ACQUISITION AUTOMATION")
    print("=" * 60)
    print("Systematic expansion from 92 to 258+ voices")
    print()
    
    # Setup environment
    base_dir = setup_acquisition_environment()
    print()
    
    # Download public domain texts
    print("📚 PHASE 1: PUBLIC DOMAIN ACQUISITIONS")
    print("-" * 40)
    downloaded, failed = batch_download_public_domain(base_dir)
    print()
    
    # Generate commercial acquisition guide
    print("🛒 PHASE 2: COMMERCIAL ACQUISITION GUIDE")
    print("-" * 40)
    print_commercial_acquisition_guide(base_dir)
    print()
    
    # Final summary
    print("📊 AUTOMATION SUMMARY")
    print("=" * 30)
    print(f"✅ Public domain texts downloaded: {len(downloaded)}")
    print(f"❌ Public domain failed: {len(failed)}")
    print(f"📋 Commercial targets identified: ~7-10 essential texts")
    print(f"💰 Estimated commercial cost: ~$120-150")
    print()
    print(f"📁 All files organized in: {base_dir.absolute()}")
    print()
    print("🎯 NEXT STEPS:")
    print("1. Review downloaded public domain texts")
    print("2. Acquire identified commercial texts")  
    print("3. Run quality validation on all files")
    print("4. Process through Calibre conversion pipeline")
    print("5. Integrate into Chamber library with YAML frontmatter")
    print()
    print("🚀 Ready to expand Chamber from 92 to 110+ voices!")

if __name__ == "__main__":
    main()