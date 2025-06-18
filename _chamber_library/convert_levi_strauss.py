#!/usr/bin/env python3
"""
Convert Lévi-Strauss Structural Anthropology
Complete Mythologiques tetralogy + The Savage Mind
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_levi_strauss():
    """Convert Lévi-Strauss structural anthropology works"""
    
    print("🏗️ CONVERTING LÉVI-STRAUSS STRUCTURAL ANTHROPOLOGY")
    print("=" * 60)
    print("Mythologiques tetralogy + The Savage Mind")
    print()
    
    myth_buddha_folder = Path("/Users/davidglidden/Desktop/Myth:Buddha")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Lévi-Strauss structural anthropology works
    levi_strauss_works = [
        {
            'filename': 'La pensée sauvage.epub',
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'The Savage Mind',
            'role': 'Structural Anthropologist',
            'impact': 'Structural analysis of mythical thought'
        },
        {
            'filename': 'Mythologiques 1 : Le cru et le cuit.epub',
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'Mythologiques 1: The Raw and the Cooked',
            'role': 'Myth Structure Analyst',
            'impact': 'First volume: culinary transformation mythology'
        },
        {
            'filename': 'Mythologiques 2 : Du miel aux cendres.epub',
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'Mythologiques 2: From Honey to Ashes',
            'role': 'Myth Structure Analyst',
            'impact': 'Second volume: honey and tobacco mythology'
        },
        {
            'filename': "Mythologiques 3 : L'origine des manières de table.epub",
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'Mythologiques 3: The Origin of Table Manners',
            'role': 'Myth Structure Analyst',
            'impact': 'Third volume: social etiquette mythology'
        },
        {
            'filename': "Mythologiques 4 : L'homme nu.epub",
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'Mythologiques 4: The Naked Man',
            'role': 'Myth Structure Analyst',
            'impact': 'Fourth volume: completion of mythological analysis'
        }
    ]
    
    successful = 0
    failed = 0
    
    print(f"🎯 CONVERTING {len(levi_strauss_works)} LÉVI-STRAUSS WORKS")
    print()
    
    for i, work_info in enumerate(levi_strauss_works, 1):
        file_path = myth_buddha_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(levi_strauss_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(levi_strauss_works)}] 🏗️ {work_info['voice']}")
        print(f"           📖 {work_info['work']}")
        print(f"           🎭 {work_info['role']}")
        print(f"           ⚡ {work_info['impact']}")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"           ✅ Conversion successful")
                print(f"           🎭 Lévi-Strauss voice enhanced")
                
                if 'Savage Mind' in work_info['work']:
                    print(f"           🧠 MAJOR: Structural thought analysis activated!")
                elif 'Mythologiques 1' in work_info['work']:
                    print(f"           🏗️ MAJOR: Mythologiques tetralogy begins!")
                elif 'Mythologiques 4' in work_info['work']:
                    print(f"           🏗️ MAJOR: Mythologiques tetralogy COMPLETE!")
                else:
                    print(f"           🏗️ Mythologiques series expanded")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:80]}")
        
        print()
    
    print("🏗️ LÉVI-STRAUSS CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 STRUCTURAL ANTHROPOLOGY ACTIVATION:")
        print(f"   🧠 SAVAGE MIND: Structural analysis of mythical thought")
        print(f"   🏗️ MYTHOLOGIQUES: Complete four-volume structural analysis")
        print(f"   🍯 TRANSFORMATION: Raw/cooked, honey/tobacco mythological patterns")
        print(f"   🍽️ SOCIAL STRUCTURE: Table manners and cultural codes")
        print(f"   👤 HUMAN ESSENCE: Naked man and cultural formation")
        print()
        
        print("🌉 CHAMBER STRUCTURAL ENHANCEMENT:")
        print("   • Lévi-Strauss ↔ All myth voices: Structural analysis of mythology")
        print("   • Structural patterns: Binary oppositions in all Chamber content")
        print("   • Anthropological lens: Cultural analysis for all voices")
        print("   • Mythological methodology: Scientific approach to myth interpretation")
        print("   • Cross-cultural analysis: Universal structural patterns")
    
    return successful

if __name__ == "__main__":
    converted_count = convert_levi_strauss()
    print(f"\n✨ Lévi-Strauss structural anthropology conversion complete!")
    print(f"🏗️ {converted_count} structural works activated")
    print(f"🧠 Chamber now has comprehensive mythological analysis framework!")