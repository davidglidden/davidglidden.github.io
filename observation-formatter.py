#!/usr/bin/env python3
"""
Observation Formatter for Animal Rationis Capax
===============================================
Specialized formatter for short observational prose poetry and contemplative fragments.
Handles intimate, immediate pieces differently from formal essays.

Usage:
    python observation-formatter.py input.md [output.md]
"""

import re
import sys
from pathlib import Path
from datetime import datetime

class ObservationFormatter:
    def __init__(self):
        # Patterns for observational content
        self.observational_markers = [
            r'\b(café|coffee|street|window|watching|sitting|reading|light|shadow)\b',
            r'\b(December|January|morning|afternoon|evening|today|yesterday)\b',
            r'\b(faces|eyes|watching|observing|seeing|listening|silence)\b',
            r'\b(dream|memory|fragment|moment|instant|glance)\b',
            r'\[Dream:\]|\[Memory:\]|\[Fragment:\]'
        ]
        
        # French phrases and terms
        self.french_terms = [
            r'\b(fond d\'air froid|café allongé|croisement|matins du monde)\b',
            r'\b(terrace|baguette|croissant|arrondissement|quartier)\b'
        ]
        
        # Location markers for Paris observations
        self.paris_markers = [
            r'\b(Paris|Charonne|Ledru Rollin|arrondissement|métro)\b',
            r'\b(Seine|Marais|Bastille|République|Nation)\b'
        ]

    def detect_observation_type(self, text: str) -> str:
        """Detect the specific type of observation."""
        text_lower = text.lower()
        
        if '[dream:' in text_lower or 'dream' in text_lower:
            return 'dream'
        elif any(re.search(pattern, text_lower) for pattern in self.paris_markers):
            return 'paris-observation'
        elif 'café' in text_lower or 'coffee' in text_lower:
            return 'café-observation'
        elif any(word in text_lower for word in ['memory', 'remember', 'childhood']):
            return 'memory'
        else:
            return 'observation'

    def should_be_observation(self, text: str) -> bool:
        """Determine if content should be treated as observational prose."""
        # Count paragraphs and words
        paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
        word_count = len(text.split())
        
        # Short pieces with observational markers
        if word_count < 200 and len(paragraphs) <= 5:
            score = 0
            text_lower = text.lower()
            
            for pattern in self.observational_markers:
                if re.search(pattern, text_lower):
                    score += 1
            
            return score >= 2
        
        return False

    def apply_french_styling(self, text: str) -> str:
        """Apply italic styling to French terms and phrases."""
        for pattern in self.french_terms:
            def replace_func(match):
                return f'*{match.group()}*'
            text = re.sub(pattern, replace_func, text, flags=re.IGNORECASE)
        return text

    def format_fragments(self, text: str) -> str:
        """Add subtle spacing between observational fragments."""
        # Split into paragraphs
        paragraphs = text.split('\n\n')
        formatted_paragraphs = []
        
        for para in paragraphs:
            para = para.strip()
            if para:
                # Add breathing space class for short fragments
                if len(para.split()) <= 15:
                    formatted_paragraphs.append(f'<p class="whisper">{para}</p>')
                else:
                    formatted_paragraphs.append(para)
        
        return '\n\n'.join(formatted_paragraphs)

    def add_subtle_ornaments(self, text: str, observation_type: str) -> str:
        """Add very subtle ornaments for observations."""
        # Only add ornaments if there are natural breaks
        if '---' in text:
            ornament_class = 'personal'  # Default to personal for intimate observations
            
            if observation_type == 'dream':
                ornament_class = 'philosophical'
            elif 'paris' in observation_type:
                ornament_class = 'travel'
            
            # Use a more subtle ornament
            text = re.sub(r'^---+\s*$', f'<div class="ornament {ornament_class}"></div>', text, flags=re.MULTILINE)
        
        return text

    def create_observation_front_matter(self, text: str, observation_type: str) -> str:
        """Create appropriate front matter for observational pieces."""
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # Extract title from first line or create one
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        if lines:
            first_line = lines[0]
            if len(first_line) > 50:
                title = first_line[:47] + '...'
            else:
                title = first_line
        else:
            title = f"Observation {current_date}"
        
        # Determine tags based on content
        tags = ['observation', observation_type]
        if any(re.search(pattern, text.lower()) for pattern in self.paris_markers):
            tags.extend(['Paris', 'France'])
        
        front_matter = f'''title: "{title}"
layout: fragment
date: {current_date}
tags: {tags}
class: observation'''
        
        return f'---\n{front_matter}\n---\n\n{text}'

    def format_observation(self, text: str) -> str:
        """Format an observational piece with appropriate typography."""
        if not self.should_be_observation(text):
            print("⚠️  This content may not be observational prose. Consider using the main typographic-formatter.py instead.")
        
        observation_type = self.detect_observation_type(text)
        
        # Apply specific formatting to content only
        content = text
        if not text.startswith('---'):
            content = self.apply_french_styling(content)
            content = self.add_subtle_ornaments(content, observation_type)
            # Create front matter with formatted content
            text = self.create_observation_front_matter(content, observation_type)
        else:
            # Has front matter, process content part only
            parts = text.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                content = parts[2]
                content = self.apply_french_styling(content)
                content = self.add_subtle_ornaments(content, observation_type)
                text = f'---{front_matter}---{content}'
        
        # Add formatting comment
        comment = f"""
<!-- 
Observation formatted with specialized formatter for Animal Rationis Capax
Observation type: {observation_type}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-->"""
        
        text += comment
        
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python observation-formatter.py input.md [output.md]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Determine output file
    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.parent / f"{input_file.stem}_observation{input_file.suffix}"
    
    # Read and process
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatter = ObservationFormatter()
        formatted_content = formatter.format_observation(content)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        
        print(f"Observation formatted and saved to: {output_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()