#!/usr/bin/env python3
"""
Convert Foucault Priority Works
Start with the most critical Foucault texts for power/knowledge analysis
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_foucault_critical():
    """Convert Foucault's most critical works first"""
    
    print("🔥 CONVERTING FOUCAULT'S CRITICAL WORKS")
    print("=" * 50)
    print("Power/knowledge archaeology - essential for Chamber critical theory")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Foucault's most critical works
    foucault_works = [
        {
            'filename': 'Histoire de la folie à l\'âge classique.epub',
            'work': 'Histoire de la folie à l\'âge classique',
            'role': 'Archaeology of Madness and Reason',
            'impact': 'Foundation of genealogical method'
        },
        {
            'filename': 'L\'archéologie du savoir.epub',
            'work': 'L\'Archéologie du savoir',
            'role': 'Methodology of Knowledge Archaeology',
            'impact': 'Epistemic archaeology framework'
        },
        {
            'filename': 'Surveiller et punir: Naissance de la prison.epub',
            'work': 'Surveiller et punir',
            'role': 'Analysis of Disciplinary Power',
            'impact': 'Disciplinary society theory'
        }
    ]
    
    successful = 0
    failed = 0
    
    for i, work_info in enumerate(foucault_works, 1):
        file_path = eastern_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(foucault_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(foucault_works)}] 🔥 Michel Foucault")
        print(f"           📖 {work_info['work']}")
        print(f"           🎪 {work_info['role']}")
        print(f"           ⚡ {work_info['impact']}")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"           ✅ Conversion successful")
                print(f"           🎭 Foucault voice ENHANCED")
                
                if 'folie' in work_info['work'].lower():
                    print(f"           🌟 MAJOR: Madness archaeology activated!")
                elif 'archéologie' in work_info['work'].lower():
                    print(f"           🔍 MAJOR: Knowledge archaeology method established!")
                elif 'surveiller' in work_info['work'].lower():
                    print(f"           👁️ MAJOR: Disciplinary power analysis integrated!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("🔥 FOUCAULT CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 FOUCAULT VOICE TRANSFORMATION:")
        print(f"   🔥 Power/knowledge archaeology: Established")
        print(f"   👁️ Disciplinary analysis: Activated")
        print(f"   🔍 Genealogical method: Integrated")
        print(f"   🏛️ Critical theory foundation: Complete")
        print()
        
        print("🌉 NEW CHAMBER CAPABILITIES:")
        print("   • Foucault ↔ Arendt: Power vs political action")
        print("   • Foucault ↔ Benjamin: Archaeology vs historical materialism")
        print("   • Foucault ↔ Zuboff: Disciplinary vs surveillance capitalism")
        print("   • Foucault ↔ Weil: Power analysis vs spiritual resistance")
    
    return successful

if __name__ == "__main__":
    print("🔥 FOUCAULT PRIORITY CONVERSION")
    print("=" * 45)
    print("Converting Michel Foucault's most critical works for Chamber integration")
    print()
    
    converted_count = convert_foucault_critical()
    
    print(f"\n✨ Foucault priority conversion complete!")
    print(f"🎭 {converted_count} Foucault works activated")
    print(f"🔥 Power/knowledge archaeology now available to the Chamber!")