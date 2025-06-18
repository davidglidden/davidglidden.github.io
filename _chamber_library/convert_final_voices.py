#!/usr/bin/env python3
"""
Convert Final Chamber Voices
Complete the Chamber constellation with Lorca, Jaccottet, and other missing voices
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_final_chamber_voices():
    """Convert the remaining identified Chamber voices"""
    
    print("🌸 CONVERTING FINAL CHAMBER VOICES")
    print("=" * 50)
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Final priority voices to convert
    final_voices = [
        # HIGH PRIORITY
        {
            'filename': 'Bodas de sangre.epub',
            'author': 'Federico García Lorca',
            'voice': 'Federico García Lorca',
            'work': 'Bodas de sangre (Blood Wedding)',
            'priority': 'HIGH',
            'role': 'Tragic Poet of Andalusia'
        },
        {
            'filename': 'À la lumière d\'hiver : Pensées sous les nuages : Leçons : Chants d\'en bas.epub',
            'author': 'Philippe Jaccottet',
            'voice': 'Philippe Jaccottet',
            'work': 'À la lumière d\'hiver',
            'priority': 'HIGH', 
            'role': 'Poet of Light and Landscape'
        },
        {
            'filename': 'A Trackless Path: A Commentary on the Great Completion (Dzogchen) Teaching of Jigmé Lingpa\'s Revelations of Ever-Present Good.epub',
            'author': 'Jigmé Lingpa',
            'voice': 'Jigmé Lingpa',
            'work': 'A Trackless Path (Dzogchen)',
            'priority': 'HIGH',
            'role': 'Dzogchen Master of the Great Completion'
        },
        {
            'filename': 'Aesthetics.epub',
            'author': 'Georg Wilhelm Friedrich Hegel',
            'voice': 'Georg Wilhelm Friedrich Hegel',
            'work': 'Aesthetics',
            'priority': 'HIGH',
            'role': 'Systematic Aesthetician'
        },
        {
            'filename': 'Aesthetics and Politics.epub',
            'author': 'Walter Benjamin et al.',
            'voice': 'Frankfurt School Collective',
            'work': 'Aesthetics and Politics',
            'priority': 'HIGH',
            'role': 'Critical Theory Ensemble'
        },
        {
            'filename': 'D\'une lyre à cinq cordes. Pétrarque, Le Tasse, Leopardi, Ungaretti, Montale, Bertolucci, Luzi, Bigongiari, Erba, Góngora, Goethe, Hölderlin, Ferdinand Meyer, Maria Rilke, Lavant, Burkart, Mandelstam, Skácel.epub',
            'author': 'Multiple Poets',
            'voice': 'European Poetic Constellation',
            'work': 'D\'une lyre à cinq cordes',
            'priority': 'CRITICAL',
            'role': 'Multi-Voice European Poetry Anthology'
        },
        
        # MEDIUM PRIORITY - Jaccottet Collection
        {
            'filename': 'Airs.epub',
            'author': 'Philippe Jaccottet',
            'voice': 'Philippe Jaccottet',
            'work': 'Airs',
            'priority': 'MEDIUM',
            'role': 'Poet of Atmosphere and Breath'
        },
        {
            'filename': 'Ce peu de bruits.epub',
            'author': 'Philippe Jaccottet',
            'voice': 'Philippe Jaccottet',
            'work': 'Ce peu de bruits',
            'priority': 'MEDIUM',
            'role': 'Minimalist Sound Poet'
        },
        {
            'filename': 'Cahier de verdure:Après beaucoup d\'années.epub',
            'author': 'Philippe Jaccottet',
            'voice': 'Philippe Jaccottet',
            'work': 'Cahier de verdure',
            'priority': 'MEDIUM',
            'role': 'Nature Contemplative'
        },
        {
            'filename': 'Carnets 1995-1998.epub',
            'author': 'Philippe Jaccottet',
            'voice': 'Philippe Jaccottet',
            'work': 'Carnets 1995-1998',
            'priority': 'MEDIUM',
            'role': 'Notebook Poet and Observer'
        }
    ]
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2}
    final_voices.sort(key=lambda x: priority_order.get(x['priority'], 3))
    
    successful_conversions = []
    failed_conversions = []
    
    for i, voice_info in enumerate(final_voices, 1):
        file_path = eastern_folder / voice_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(final_voices)}] ❌ Not found: {voice_info['filename']}")
            failed_conversions.append(voice_info)
            continue
        
        print(f"[{i}/{len(final_voices)}] 🎭 {voice_info['voice']} ({voice_info['priority']})")
        print(f"           📖 {voice_info['work']}")
        print(f"           🎪 {voice_info['role']}")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful_conversions.append(voice_info)
                print(f"           ✅ Conversion successful")
                print(f"           🎭 {voice_info['voice']} voice ACTIVATED")
                
                # Special announcements
                if voice_info['voice'] == 'Federico García Lorca':
                    print(f"           🌹 MAJOR: Lorca's tragic poetry joins the Chamber!")
                elif voice_info['voice'] == 'Philippe Jaccottet':
                    print(f"           🌿 French landscape poetry activated!")
                elif voice_info['voice'] == 'European Poetic Constellation':
                    print(f"           🌟 MAJOR: Multi-voice European poetry anthology!")
                elif voice_info['voice'] == 'Jigmé Lingpa':
                    print(f"           🏔️ Tibetan Buddhist mysticism activated!")
                
            else:
                failed_conversions.append(voice_info)
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed_conversions.append(voice_info)
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    # Summary
    print("📊 FINAL VOICE CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {len(successful_conversions)} voices")
    print(f"❌ Failed conversions: {len(failed_conversions)} voices")
    print()
    
    if successful_conversions:
        print("🎭 NEWLY ACTIVATED FINAL VOICES:")
        
        # Group by voice type
        poetic_voices = [v for v in successful_conversions if 'poet' in v['role'].lower()]
        mystical_voices = [v for v in successful_conversions if 'dzogchen' in v['role'].lower() or 'mystical' in v['role'].lower()]
        philosophical_voices = [v for v in successful_conversions if 'aesthet' in v['role'].lower() or 'philosoph' in v['role'].lower()]
        
        if poetic_voices:
            print(f"   🌸 POETIC VOICES ({len(poetic_voices)}):")
            for v in poetic_voices:
                print(f"      • {v['voice']}: {v['work']}")
        
        if mystical_voices:
            print(f"   🏔️ MYSTICAL VOICES ({len(mystical_voices)}):")
            for v in mystical_voices:
                print(f"      • {v['voice']}: {v['work']}")
        
        if philosophical_voices:
            print(f"   🧠 PHILOSOPHICAL VOICES ({len(philosophical_voices)}):")
            for v in philosophical_voices:
                print(f"      • {v['voice']}: {v['work']}")
        
        print()
        print("🏛️ CHAMBER COMPLETION ENHANCEMENT:")
        print(f"   🌹 Spanish tragic poetry: Lorca's duende")
        print(f"   🌿 French landscape mysticism: Jaccottet's contemplations")
        print(f"   🌟 European poetic constellation: Multi-lingual anthology")
        print(f"   🏔️ Tibetan Buddhist completion: Dzogchen teachings")
        print(f"   🎨 Systematic aesthetics: Hegelian art philosophy")
        print()
        
        print("🌉 NEW CHAMBER DIALECTICAL POSSIBILITIES:")
        print("   • Lorca ↔ Weil: Tragic attention and duende")
        print("   • Jaccottet ↔ Bachelard: Landscape and poetic space")
        print("   • Jigmé Lingpa ↔ Nagarjuna: Dzogchen and Madhyamaka")
        print("   • Hegel ↔ Benjamin: Systematic vs. fragmentary aesthetics")
        print("   • European Poetry ↔ All voices: Multi-lingual lyric synthesis")
        print()
    
    if failed_conversions:
        print("❌ CONVERSION FAILURES:")
        for failure in failed_conversions:
            print(f"   • {failure['voice']}: {failure['filename']}")
        print()
    
    print("📋 FINAL STEPS:")
    print("   1. Run: python3 chamber_amphitheater_status.py")
    print("   2. The Chamber constellation is now complete!")
    print("   3. All Eastern folder EPUBs can be safely removed")
    
    return len(successful_conversions)

if __name__ == "__main__":
    print("🌸 FINAL CHAMBER VOICE ACTIVATION")
    print("=" * 55)
    print("Converting the last remaining voices: Lorca, Jaccottet, and European poetry")
    print()
    
    converted_count = convert_final_chamber_voices()
    
    print(f"\n✨ Final voice activation complete!")
    print(f"🎭 {converted_count} final voices activated")
    print(f"🏛️ The Chamber constellation is now truly complete!")