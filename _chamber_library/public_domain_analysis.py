#!/usr/bin/env python3
"""
Public Domain Analysis for Chamber Voices
Identify which essential works are in public domain vs require acquisition
"""

from collections import OrderedDict
from datetime import datetime

def analyze_public_domain_status():
    """Analyze copyright status of essential Chamber works"""
    
    current_year = datetime.now().year
    
    # Generally, works enter public domain:
    # - Pre-1928: Public domain in US
    # - Author died 70+ years ago: Public domain in most countries
    # - Some exceptions for renewed copyrights
    
    def get_pd_status(author_death_year, work_year=None, author_name=""):
        """Determine public domain status"""
        if author_death_year:
            years_since_death = current_year - author_death_year
            if years_since_death >= 70:
                return "PUBLIC_DOMAIN", f"Author died {author_death_year} ({years_since_death} years ago)"
            else:
                return "COPYRIGHTED", f"Author died {author_death_year} (copyright until ~{author_death_year + 70})"
        elif work_year and work_year < 1928:
            return "PUBLIC_DOMAIN", f"Published {work_year} (pre-1928)"
        else:
            return "UNCERTAIN", "Need to check specific copyright status"
    
    # Essential works for each voice with copyright analysis
    voice_works_analysis = OrderedDict([
        
        # EASTERN VOICES (Many in Public Domain)
        ('Laozi', {
            'death_year': None,  # Legendary figure ~6th century BCE
            'essential_works': [
                {
                    'title': 'Tao Te Ching (Dao De Jing)',
                    'original_period': '6th century BCE',
                    'pd_status': 'PUBLIC_DOMAIN',
                    'pd_reason': 'Ancient text, multiple translations available',
                    'sources': ['Project Gutenberg', 'Archive.org', 'Wikisource', 'Sacred-texts.com'],
                    'recommended_translations': ['James Legge', 'D.C. Lau', 'Red Pine (Bill Porter)']
                }
            ],
            'minimum_works': 1,
            'priority': 'CRITICAL'
        }),
        
        ('Zhuangzi', {
            'death_year': None,  # ~4th century BCE
            'essential_works': [
                {
                    'title': 'Zhuangzi (Complete Works)',
                    'original_period': '4th century BCE', 
                    'pd_status': 'PUBLIC_DOMAIN',
                    'pd_reason': 'Ancient text, multiple translations available',
                    'sources': ['Project Gutenberg', 'Archive.org', 'Sacred-texts.com'],
                    'recommended_translations': ['James Legge', 'Burton Watson', 'A.C. Graham']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Nagarjuna', {
            'death_year': None,  # ~2nd century CE
            'essential_works': [
                {
                    'title': 'Mulamadhyamakakarika (Root Verses of the Middle Way)',
                    'original_period': '2nd century CE',
                    'pd_status': 'PUBLIC_DOMAIN', 
                    'pd_reason': 'Ancient text, translations vary by translator',
                    'sources': ['Buddhist Text Translation Society', 'Archive.org', 'Various academic sources'],
                    'recommended_translations': ['Jay Garfield', 'Frederick Streng', 'David Kalupahana']
                }
            ],
            'minimum_works': 1,
            'priority': 'CRITICAL'
        }),
        
        ('Confucius', {
            'death_year': None,  # ~479 BCE
            'essential_works': [
                {
                    'title': 'The Analects',
                    'original_period': '5th century BCE',
                    'pd_status': 'PUBLIC_DOMAIN',
                    'pd_reason': 'Ancient text, multiple translations available',
                    'sources': ['Project Gutenberg', 'Archive.org', 'Wikisource'],
                    'recommended_translations': ['James Legge', 'Arthur Waley', 'D.C. Lau']
                }
            ],
            'minimum_works': 1,
            'priority': 'MEDIUM'
        }),
        
        ('Mencius', {
            'death_year': None,  # ~289 BCE
            'essential_works': [
                {
                    'title': 'Mencius',
                    'original_period': '4th century BCE',
                    'pd_status': 'PUBLIC_DOMAIN',
                    'pd_reason': 'Ancient text, multiple translations available',
                    'sources': ['Project Gutenberg', 'Archive.org', 'Sacred-texts.com'],
                    'recommended_translations': ['James Legge', 'D.C. Lau']
                }
            ],
            'minimum_works': 1,
            'priority': 'MEDIUM'
        }),
        
        ('Shankara', {
            'death_year': None,  # ~820 CE
            'essential_works': [
                {
                    'title': 'Vivekachudamani (Crest Jewel of Discrimination)',
                    'original_period': '8th century CE',
                    'pd_status': 'PUBLIC_DOMAIN',
                    'pd_reason': 'Ancient text, translations available',
                    'sources': ['Archive.org', 'Sacred-texts.com', 'Various Vedanta societies'],
                    'recommended_translations': ['Swami Madhavananda', 'John Richards']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        # MODERN EASTERN VOICES (Mixed Copyright Status)
        ('Dogen', {
            'death_year': 1253,  # Medieval, but translations copyrighted
            'essential_works': [
                {
                    'title': 'Shobogenzo (Treasury of the True Dharma Eye)',
                    'original_period': '13th century',
                    'pd_status': 'MIXED',
                    'pd_reason': 'Original ancient, but modern translations copyrighted',
                    'sources': ['Some translations on Archive.org', 'Stanford Digital Repository'],
                    'recommended_translations': ['Gudo Nishijima', 'Kazuaki Tanahashi (copyrighted)']
                }
            ],
            'minimum_works': 1,
            'priority': 'CRITICAL'
        }),
        
        ('Huang Po', {
            'death_year': 850,  # Tang Dynasty
            'essential_works': [
                {
                    'title': 'The Zen Teaching of Huang Po',
                    'original_period': '9th century',
                    'pd_status': 'MIXED',
                    'pd_reason': 'Original ancient, modern translations may be copyrighted',
                    'sources': ['Archive.org', 'Some Buddhist digital libraries'],
                    'recommended_translations': ['John Blofeld', 'Various Buddhist societies']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('D.T. Suzuki', {
            'death_year': 1966,
            'essential_works': [
                {
                    'title': 'An Introduction to Zen Buddhism',
                    'original_period': '1934',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 1966 (copyright until ~2036)',
                    'sources': ['Need to acquire or check specific editions'],
                    'recommended_translations': ['Original English works']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Thich Nhat Hanh', {
            'death_year': 2022,
            'essential_works': [
                {
                    'title': 'The Miracle of Mindfulness',
                    'original_period': '1975',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 2022 (copyright until ~2092)',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Original English works']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Krishnamurti', {
            'death_year': 1986,
            'essential_works': [
                {
                    'title': 'Freedom from the Known',
                    'original_period': '1969',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 1986 (copyright until ~2056)',
                    'sources': ['Krishnamurti Foundation may have some free texts'],
                    'recommended_translations': ['Original English works']
                }
            ],
            'minimum_works': 1,
            'priority': 'MEDIUM'
        }),
        
        # WESTERN VOICES NEEDING ADDITIONAL WORKS
        ('Aldus Manutius', {
            'death_year': 1515,
            'essential_works': [
                {
                    'title': 'Hypnerotomachia Poliphili',
                    'original_period': '1499',
                    'pd_status': 'PUBLIC_DOMAIN',
                    'pd_reason': 'Published 1499, author died 1515',
                    'sources': ['Archive.org', 'Project Gutenberg (Latin)', 'Various digitized editions'],
                    'recommended_translations': ['Joscelyn Godwin translation']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Maurice Merleau-Ponty', {
            'death_year': 1961,
            'essential_works': [
                {
                    'title': 'Phenomenology of Perception',
                    'original_period': '1945',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 1961 (copyright until ~2031)',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Colin Smith translation']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Jane Jacobs', {
            'death_year': 2006,
            'essential_works': [
                {
                    'title': 'The Death and Life of Great American Cities',
                    'original_period': '1961',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 2006 (copyright until ~2076)',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Original English']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Lewis Mumford', {
            'death_year': 1990,
            'essential_works': [
                {
                    'title': 'Technics and Civilization',
                    'original_period': '1934',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 1990 (copyright until ~2060)',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Original English']
                }
            ],
            'minimum_works': 1,
            'priority': 'HIGH'
        }),
        
        ('Jacques Derrida', {
            'death_year': 2004,
            'essential_works': [
                {
                    'title': 'Of Grammatology',
                    'original_period': '1967',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 2004 (copyright until ~2074)',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Gayatri Spivak translation']
                }
            ],
            'minimum_works': 1,
            'priority': 'MEDIUM'
        }),
        
        ('Juhani Pallasmaa', {
            'death_year': None,  # Still living (born 1936)
            'essential_works': [
                {
                    'title': 'The Eyes of the Skin',
                    'original_period': '1996',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Contemporary author, recent work',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Original English']
                }
            ],
            'minimum_works': 1,
            'priority': 'MEDIUM'
        }),
        
        ('Ivan Illich', {
            'death_year': 2002,
            'essential_works': [
                {
                    'title': 'Tools for Conviviality',
                    'original_period': '1973',
                    'pd_status': 'COPYRIGHTED',
                    'pd_reason': 'Author died 2002 (copyright until ~2072)',
                    'sources': ['Need to acquire'],
                    'recommended_translations': ['Original English']
                }
            ],
            'minimum_works': 1,
            'priority': 'MEDIUM'
        })
    ])
    
    return voice_works_analysis

def create_public_domain_report():
    """Generate comprehensive public domain analysis report"""
    
    analysis = analyze_public_domain_status()
    
    with open("chamber_public_domain_analysis.md", "w") as f:
        f.write("# Chamber Voices: Public Domain Analysis\n\n")
        f.write("*Strategic guide to acquiring Chamber texts through public domain vs purchase*\n\n")
        
        # Summary statistics
        pd_count = 0
        copyrighted_count = 0
        mixed_count = 0
        total_voices = len(analysis)
        
        for voice_data in analysis.values():
            for work in voice_data['essential_works']:
                if work['pd_status'] == 'PUBLIC_DOMAIN':
                    pd_count += 1
                elif work['pd_status'] == 'COPYRIGHTED':
                    copyrighted_count += 1
                else:
                    mixed_count += 1
        
        f.write("## Summary\n\n")
        f.write(f"**Total Voices Analyzed**: {total_voices}  \n")
        f.write(f"**📖 Public Domain Works**: {pd_count}  \n")
        f.write(f"**🔒 Copyrighted Works**: {copyrighted_count}  \n")
        f.write(f"**🔀 Mixed Status**: {mixed_count}  \n")
        f.write(f"**Public Domain Percentage**: {(pd_count/(pd_count+copyrighted_count+mixed_count))*100:.1f}%  \n\n")
        
        # Categorize by copyright status
        public_domain_voices = []
        copyrighted_voices = []
        mixed_voices = []
        
        for voice_name, voice_data in analysis.items():
            primary_work = voice_data['essential_works'][0]
            if primary_work['pd_status'] == 'PUBLIC_DOMAIN':
                public_domain_voices.append((voice_name, voice_data))
            elif primary_work['pd_status'] == 'COPYRIGHTED':
                copyrighted_voices.append((voice_name, voice_data))
            else:
                mixed_voices.append((voice_name, voice_data))
        
        # Public Domain section
        f.write("## 📖 Public Domain Voices (Free to Acquire)\n\n")
        f.write("*These voices can be activated immediately through free sources*\n\n")
        
        for voice_name, voice_data in public_domain_voices:
            f.write(f"### {voice_name}\n")
            f.write(f"**Priority**: {voice_data['priority']}  \n")
            
            for work in voice_data['essential_works']:
                f.write(f"**Work**: *{work['title']}*  \n")
                f.write(f"**Status**: ✅ {work['pd_status']}  \n")
                f.write(f"**Reason**: {work['pd_reason']}  \n")
                f.write(f"**Sources**: {', '.join(work['sources'])}  \n")
                if work.get('recommended_translations'):
                    f.write(f"**Recommended Translations**: {', '.join(work['recommended_translations'])}  \n")
                f.write("  \n")
            
            f.write("---\n\n")
        
        # Mixed Status section
        if mixed_voices:
            f.write("## 🔀 Mixed Status Voices (Original Public, Translations May Vary)\n\n")
            
            for voice_name, voice_data in mixed_voices:
                f.write(f"### {voice_name}\n")
                f.write(f"**Priority**: {voice_data['priority']}  \n")
                
                for work in voice_data['essential_works']:
                    f.write(f"**Work**: *{work['title']}*  \n")
                    f.write(f"**Status**: ⚠️ {work['pd_status']}  \n")
                    f.write(f"**Reason**: {work['pd_reason']}  \n")
                    f.write(f"**Sources**: {', '.join(work['sources'])}  \n")
                    f.write("  \n")
                
                f.write("---\n\n")
        
        # Copyrighted section
        f.write("## 🔒 Copyrighted Voices (Require Purchase)\n\n")
        f.write("*These voices need to be acquired through purchase or library access*\n\n")
        
        for voice_name, voice_data in copyrighted_voices:
            f.write(f"### {voice_name}\n")
            f.write(f"**Priority**: {voice_data['priority']}  \n")
            
            for work in voice_data['essential_works']:
                f.write(f"**Work**: *{work['title']}*  \n")
                f.write(f"**Status**: 🔒 {work['pd_status']}  \n")
                f.write(f"**Reason**: {work['pd_reason']}  \n")
                f.write(f"**Acquisition**: {', '.join(work['sources'])}  \n")
                f.write("  \n")
            
            f.write("---\n\n")
        
        # Strategic recommendations
        f.write("## Strategic Acquisition Plan\n\n")
        
        f.write("### Phase 1: Public Domain Foundation (Free)\n")
        f.write("**Immediate acquisition from free sources**:\n\n")
        
        for voice_name, voice_data in public_domain_voices:
            if voice_data['priority'] in ['CRITICAL', 'HIGH']:
                primary_work = voice_data['essential_works'][0]
                f.write(f"1. **{voice_name}**: *{primary_work['title']}*\n")
                f.write(f"   - Sources: {', '.join(primary_work['sources'][:2])}\n")
        
        f.write("\n### Phase 2: Mixed Status Works (Some Free)\n")
        f.write("**Check for free translations, acquire others**:\n\n")
        
        for voice_name, voice_data in mixed_voices:
            if voice_data['priority'] in ['CRITICAL', 'HIGH']:
                primary_work = voice_data['essential_works'][0]
                f.write(f"- **{voice_name}**: *{primary_work['title']}*\n")
        
        f.write("\n### Phase 3: Copyrighted Works (Purchase Required)\n")
        f.write("**Budget for acquisition**:\n\n")
        
        critical_copyrighted = [(vn, vd) for vn, vd in copyrighted_voices if vd['priority'] == 'CRITICAL']
        high_copyrighted = [(vn, vd) for vn, vd in copyrighted_voices if vd['priority'] == 'HIGH']
        
        if critical_copyrighted:
            f.write("**Critical Priority**:\n")
            for voice_name, voice_data in critical_copyrighted:
                primary_work = voice_data['essential_works'][0]
                f.write(f"- **{voice_name}**: *{primary_work['title']}*\n")
        
        if high_copyrighted:
            f.write("\n**High Priority**:\n")
            for voice_name, voice_data in high_copyrighted:
                primary_work = voice_data['essential_works'][0]
                f.write(f"- **{voice_name}**: *{primary_work['title']}*\n")
        
        # Public domain sources guide
        f.write("\n## Public Domain Source Guide\n\n")
        
        f.write("### Primary Sources for Chamber Texts\n")
        f.write("1. **Project Gutenberg** (gutenberg.org)\n")
        f.write("   - Largest collection of public domain texts\n")
        f.write("   - Multiple formats (EPUB, TXT, HTML)\n")
        f.write("   - Excellent for classical Eastern texts\n\n")
        
        f.write("2. **Internet Archive** (archive.org)\n")
        f.write("   - Vast digital library with rare texts\n")
        f.write("   - Academic editions and translations\n")
        f.write("   - Good for Buddhist and philosophical texts\n\n")
        
        f.write("3. **Wikisource** (wikisource.org)\n")
        f.write("   - Collaborative transcription project\n")
        f.write("   - High-quality texts with citations\n")
        f.write("   - Multiple language versions\n\n")
        
        f.write("4. **Sacred-texts.com**\n")
        f.write("   - Comprehensive religious and philosophical texts\n")
        f.write("   - Eastern wisdom traditions well represented\n")
        f.write("   - Multiple translation comparisons\n\n")
        
        f.write("5. **HathiTrust Digital Library**\n")
        f.write("   - Academic library consortium\n")
        f.write("   - Scholarly editions and translations\n")
        f.write("   - Good for out-of-copyright academic works\n\n")
        
        # Immediate action plan
        f.write("## Immediate Action Plan\n\n")
        
        f.write("### Week 1: Eastern Foundation (All Free)\n")
        eastern_pd = [(vn, vd) for vn, vd in public_domain_voices if vn in ['Laozi', 'Zhuangzi', 'Nagarjuna', 'Confucius', 'Shankara']]
        
        for voice_name, voice_data in eastern_pd:
            primary_work = voice_data['essential_works'][0]
            f.write(f"- Download **{voice_name}**: *{primary_work['title']}* from {primary_work['sources'][0]}\n")
        
        f.write("\n### Week 2: Typography and Medieval Works\n")
        f.write("- Download **Aldus Manutius**: *Hypnerotomachia Poliphili* from Archive.org\n")
        f.write("- Research **Dogen** translations on Archive.org\n")
        
        f.write("\n### Week 3: Contemporary Acquisitions\n")
        f.write("- Budget and acquire key contemporary copyrighted works\n")
        f.write("- Focus on Thich Nhat Hanh, D.T. Suzuki, Merleau-Ponty\n")
        
        # Cost analysis
        f.write("\n## Cost Analysis\n\n")
        
        f.write(f"**Free Acquisition Potential**: {pd_count}/{pd_count+copyrighted_count+mixed_count} works ({(pd_count/(pd_count+copyrighted_count+mixed_count))*100:.1f}%)  \n")
        f.write(f"**Estimated Purchase Cost**: ${copyrighted_count * 15}-{copyrighted_count * 25} (assuming $15-25 per book)  \n")
        f.write(f"**Public Domain Savings**: ${pd_count * 20} (estimated value if purchased)  \n\n")
        
        f.write("**Chamber Development Strategy**:  \n")
        f.write("1. 🆓 **Start with public domain** to establish Eastern foundation  \n")
        f.write("2. 💰 **Selectively acquire** high-priority copyrighted works  \n")
        f.write("3. 🎯 **Focus budget** on truly essential contemporary voices  \n\n")
        
        f.write("---\n\n")
        f.write("*This analysis shows that a significant portion of Chamber voices*  \n")
        f.write("*can be activated through public domain sources, especially Eastern traditions.*\n")
    
    print("📄 Public domain analysis saved to: chamber_public_domain_analysis.md")
    
    print(f"\n📊 PUBLIC DOMAIN ANALYSIS SUMMARY:")
    print(f"   📖 Public domain works: {pd_count}")
    print(f"   🔒 Copyrighted works: {copyrighted_count}")
    print(f"   🔀 Mixed status: {mixed_count}")
    print(f"   💰 Free acquisition potential: {(pd_count/(pd_count+copyrighted_count+mixed_count))*100:.1f}%")
    
    return analysis

if __name__ == "__main__":
    print("📚 ANALYZING PUBLIC DOMAIN STATUS FOR CHAMBER VOICES")
    print("=" * 65)
    
    analysis = create_public_domain_report()
    
    print(f"\n✨ Public domain analysis complete!")
    print(f"📋 See chamber_public_domain_analysis.md for acquisition strategy")