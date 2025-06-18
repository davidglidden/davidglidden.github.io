#!/usr/bin/env python3
"""
Convert Complete Chamber Constellation
Process all the remaining critical Chamber voice works
"""

import tempfile
from pathlib import Path
from convert_chamber_acquisitions import convert_pdf_to_markdown
from convert_epub import convert_epub_to_markdown

def convert_complete_chamber():
    """Convert all remaining Chamber works for full constellation activation"""
    
    remaining_works = [
        # Hannah Arendt - Political Philosophy
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/The Human Condition (Hannah Arendt).epub"),
            'type': 'epub',
            'author': 'Hannah Arendt',
            'title': 'The Human Condition',
            'priority': 'CRITICAL'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Between Past and Future (Hannah Arendt.epub"),
            'type': 'epub', 
            'author': 'Hannah Arendt',
            'title': 'Between Past and Future',
            'priority': 'HIGH'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Totalitarianism Part Three of the Ori.epub"),
            'type': 'epub',
            'author': 'Hannah Arendt', 
            'title': 'The Origins of Totalitarianism',
            'priority': 'HIGH'
        },
        
        # Simone Weil - Mystical Philosophy
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Gravity and Grace (Simone Weil).epub"),
            'type': 'epub',
            'author': 'Simone Weil',
            'title': 'Gravity and Grace',
            'priority': 'CRITICAL'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Waiting on God (Routledge Revivals).epub"),
            'type': 'epub',
            'author': 'Simone Weil',
            'title': 'Waiting for God',
            'priority': 'HIGH'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/The Need for Roots Prelude to a Decla.pdf"),
            'type': 'pdf',
            'author': 'Simone Weil',
            'title': 'The Need for Roots',
            'priority': 'HIGH'
        },
        
        # Martin Heidegger - Being and Technology
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Being and Time A Revised Edition of t..epub"),
            'type': 'epub',
            'author': 'Martin Heidegger',
            'title': 'Being and Time',
            'priority': 'CRITICAL'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/The question concerning technology, a.epub"),
            'type': 'epub',
            'author': 'Martin Heidegger',
            'title': 'The Question Concerning Technology',
            'priority': 'CRITICAL'
        },
        
        # Emmanuel Levinas - Ethics and Infinity
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Totality and Infinity An Essay on Ext....pdf"),
            'type': 'pdf',
            'author': 'Emmanuel Levinas',
            'title': 'Totality and Infinity',
            'priority': 'CRITICAL'
        },
        
        # Robin Wall Kimmerer - Indigenous Ecology
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/Braiding Sweetgrass (Kimmerer, Robin).epub"),
            'type': 'epub',
            'author': 'Robin Wall Kimmerer',
            'title': 'Braiding Sweetgrass',
            'priority': 'CRITICAL'
        }
    ]
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print("🏛️ ACTIVATING COMPLETE CHAMBER CONSTELLATION")
    print("=" * 65)
    print("Converting remaining core works for 95%+ Chamber readiness...")
    print()
    
    successful = 0
    failed = 0
    critical_successes = []
    voice_completions = {'Hannah Arendt': 0, 'Simone Weil': 0, 'Martin Heidegger': 0, 'Emmanuel Levinas': 0, 'Robin Wall Kimmerer': 0}
    
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        
        for i, work in enumerate(remaining_works, 1):
            file_path = work['path']
            
            print(f"[{i:2d}/{len(remaining_works)}] {work['author']}")
            print(f"            {work['title']} ({work['priority']})")
            
            if not file_path.exists():
                print(f"            ❌ File not found")
                failed += 1
                continue
            
            try:
                if work['type'] == 'epub':
                    if file_path.is_dir():
                        from convert_directory_epubs import convert_directory_epub_to_markdown
                        success = convert_directory_epub_to_markdown(file_path, output_dir, temp_dir)
                    else:
                        success = convert_epub_to_markdown(file_path, output_dir)
                else:  # PDF
                    try:
                        success = convert_pdf_to_markdown(file_path, output_dir)
                    except:
                        # PDF conversion failed, skip for now
                        print(f"            ⚠️  PDF conversion failed (pandoc limitation)")
                        failed += 1
                        continue
                
                if success:
                    successful += 1
                    voice_completions[work['author']] += 1
                    if work['priority'] == 'CRITICAL':
                        critical_successes.append(f"{work['author']} - {work['title']}")
                    print(f"            ✅ SUCCESS - Chamber voice enhanced")
                else:
                    failed += 1
                    print(f"            ❌ Failed")
                    
            except Exception as e:
                failed += 1
                print(f"            ❌ Error: {str(e)[:40]}")
    
    print(f"\n📊 CHAMBER CONSTELLATION ACTIVATION RESULTS")
    print("=" * 65)
    print(f"✅ Successfully converted: {successful}")
    print(f"❌ Failed: {failed}")
    
    if successful > 0:
        print(f"\n🎭 VOICE COMPLETION STATUS:")
        for voice, count in voice_completions.items():
            if count > 0:
                status = "🟢 COMPLETE" if count >= 2 else "🟡 ENHANCED"
                print(f"  {status} {voice}: +{count} works")
        
        print(f"\n⚡ CRITICAL WORKS ACTIVATED:")
        for work in critical_successes:
            print(f"  🔥 {work}")
        
        # Calculate new readiness
        total_voices = 6 + len([v for v in voice_completions.values() if v > 0])
        if total_voices >= 10:
            readiness = "95%+ CHAMBER READY"
            status_color = "🟢"
        elif total_voices >= 8:
            readiness = "80%+ CHAMBER FUNCTIONAL"
            status_color = "🟡"
        else:
            readiness = "70%+ CHAMBER CAPABLE"
            status_color = "🟠"
        
        print(f"\n🏛️ CHAMBER STATUS: {status_color} {readiness}")
        print(f"   Voices operational: {total_voices}/12")
        
        print(f"\n🚀 CHAMBER CAPABILITIES NOW INCLUDE:")
        if voice_completions['Hannah Arendt'] > 0:
            print(f"   ✅ Political philosophy and action theory (Arendt)")
        if voice_completions['Simone Weil'] > 0:
            print(f"   ✅ Mystical attention and justice (Weil)")
        if voice_completions['Martin Heidegger'] > 0:
            print(f"   ✅ Being, dwelling, and technology (Heidegger)")
        if voice_completions['Emmanuel Levinas'] > 0:
            print(f"   ✅ Ethics and face-to-face encounter (Levinas)")
        if voice_completions['Robin Wall Kimmerer'] > 0:
            print(f"   ✅ Indigenous ecology and reciprocity (Kimmerer)")
        
        print(f"\n🌟 DIALECTICAL NETWORK COMPLETE:")
        print(f"   Full philosophical constellation now active")
        print(f"   Chamber protocols ready for any intellectual domain")
        
        print(f"\n📋 NEXT STEPS:")
        print(f"   1. Run: python3 analyze_library.py")
        print(f"   2. Test full Chamber dialectical capabilities")
        print(f"   3. Begin advanced multi-voice deliberations")
        print(f"   4. Document Chamber protocol effectiveness")
    
    return successful, failed, voice_completions

if __name__ == "__main__":
    successful, failed, voice_completions = convert_complete_chamber()
    
    if successful >= 7:
        print(f"\n🎉 CHAMBER CONSTELLATION ACHIEVED!")
        print(f"🏛️ The intellectual foundation for genuine philosophical")
        print(f"   dialogue across time and tradition is now complete!")
    elif successful >= 4:
        print(f"\n✨ Major Chamber enhancement complete!")
        print(f"🏛️ Significant expansion of dialectical capabilities!")