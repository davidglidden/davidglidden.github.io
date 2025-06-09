#!/usr/bin/env python3
"""
Typographic Formatter for Animal Rationis Capax
================================================
Automatically prepares Markdown documents with appropriate typographic markup
based on classical typography principles and the site's ornament system.

Usage:
    python typographic-formatter.py input.md [output.md]
    
If no output file is specified, the script will create a new file with '_formatted' suffix.
"""

import re
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class TypographicFormatter:
    def __init__(self):
        # Content type patterns for contextual ornaments
        self.content_patterns = {
            'musical': [
                r'\b(music|melody|harmony|rhythm|symphony|opera|composer|piano|violin|orchestra|song|ballad|aria)\b',
                r'\b(Mozart|Beethoven|Bach|Chopin|Vivaldi|Schubert|Brahms|Debussy|Monteverdi)\b',
                r'\b(♪|♫|♬|♭|♯|𝄞)\b'
            ],
            'philosophical': [
                r'\b(philosophy|wisdom|truth|being|existence|consciousness|reality|metaphysics|ethics|logic)\b',
                r'\b(Aristotle|Plato|Kant|Heidegger|Nietzsche|Descartes|Wittgenstein|Socrates)\b',
                r'\b(cogito|logos|ethos|pathos|dialectic|syllogism|phenomenology)\b'
            ],
            'personal': [
                r'\b(memory|childhood|family|friend|love|heart|soul|dream|hope|fear|joy|sorrow)\b',
                r'\b(I remember|In my|When I|My father|My mother|Dear|Beloved)\b',
                r'\b(nostalgia|melancholy|longing|yearning|contemplation)\b'
            ],
            'travel': [
                r'\b(journey|travel|city|town|village|landscape|mountain|river|sea|road|path)\b',
                r'\b(Paris|London|Rome|Vienna|Venice|Florence|Prague|Budapest|Berlin)\b',
                r'\b(cathedral|church|abbey|palace|castle|square|bridge|garden)\b'
            ]
        }
        
        # Latin phrases that should use small caps
        self.latin_phrases = [
            r'\b(ad astra|ad infinitum|alma mater|alter ego|anno domini|carpe diem|circa|et cetera|ex libris|in situ|per se|post mortem|sine qua non|status quo|via|versus|vide|viz)\b',
            r'\b(A\.D\.|B\.C\.|c\.|ca\.|e\.g\.|i\.e\.|etc\.|vs\.|v\.)\b'
        ]
        
        # Patterns for automatic class application
        self.class_patterns = {
            'oldstyle': [
                r'\b(1[0-9]{3}|20[0-2][0-9])\b',  # Years (1000-2029)
                r'\b\d{1,2}(st|nd|rd|th)\b'       # Ordinal numbers
            ],
            'poetic': [
                r'^>\s*.+$',  # Blockquotes (often poetic)
                r'^\s*"[^"]+"\s*$',  # Standalone quotes
            ]
        }

    def analyze_content_type(self, text: str) -> str:
        """Analyze the dominant content type for contextual ornament selection."""
        scores = {content_type: 0 for content_type in self.content_patterns.keys()}
        
        text_lower = text.lower()
        
        for content_type, patterns in self.content_patterns.items():
            for pattern in patterns:
                matches = re.findall(pattern, text_lower, re.IGNORECASE)
                scores[content_type] += len(matches)
        
        # Return the content type with the highest score, or 'personal' as default
        max_type = max(scores.items(), key=lambda x: x[1])
        return max_type[0] if max_type[1] > 0 else 'personal'

    def detect_essay_content(self, text: str) -> bool:
        """Detect if content is substantial enough to warrant the .essay class."""
        # Count paragraphs (lines that aren't headers, lists, or empty)
        lines = text.split('\n')
        paragraph_count = 0
        word_count = 0
        
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('-') and not line.startswith('*'):
                paragraph_count += 1
                word_count += len(line.split())
        
        # Essay if more than 3 substantial paragraphs or 300+ words
        return paragraph_count >= 3 or word_count >= 300

    def apply_small_caps(self, text: str) -> str:
        """Apply small caps class to Latin phrases and abbreviations."""
        for pattern in self.latin_phrases:
            def replace_func(match):
                return f'<span class="small-caps">{match.group()}</span>'
            text = re.sub(pattern, replace_func, text, flags=re.IGNORECASE)
        return text

    def apply_oldstyle_figures(self, text: str) -> str:
        """Apply oldstyle class to years and ordinal numbers, excluding front matter."""
        # Split front matter from content to avoid processing YAML
        if text.startswith('---'):
            parts = text.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                content = parts[2]
                
                # Only process the content part
                for pattern in self.class_patterns['oldstyle']:
                    def replace_func(match):
                        return f'<span class="oldstyle">{match.group()}</span>'
                    content = re.sub(pattern, replace_func, content)
                
                return f'---{front_matter}---{content}'
        
        # No front matter, process entire text
        for pattern in self.class_patterns['oldstyle']:
            def replace_func(match):
                return f'<span class="oldstyle">{match.group()}</span>'
            text = re.sub(pattern, replace_func, text)
        return text

    def format_blockquotes(self, text: str) -> str:
        """Format blockquotes with poetic class when appropriate."""
        lines = text.split('\n')
        in_blockquote = False
        formatted_lines = []
        
        for line in lines:
            if line.strip().startswith('>'):
                if not in_blockquote:
                    # Start of blockquote - check if it's poetic
                    quote_content = line.strip()[1:].strip()
                    if len(quote_content.split()) <= 15:  # Short quotes are likely poetic
                        formatted_lines.append(f'<blockquote class="poetic">')
                        formatted_lines.append(f'  {quote_content}')
                    else:
                        formatted_lines.append(line)
                    in_blockquote = True
                else:
                    if 'class="poetic"' in formatted_lines[-2]:
                        formatted_lines.append(f'  {line.strip()[1:].strip()}')
                    else:
                        formatted_lines.append(line)
            elif in_blockquote and line.strip() == '':
                if 'class="poetic"' in ''.join(formatted_lines[-3:]):
                    formatted_lines.append('</blockquote>')
                formatted_lines.append(line)
                in_blockquote = False
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)

    def add_ornaments(self, text: str, content_type: str) -> str:
        """Replace horizontal rules with contextual ornaments, excluding front matter."""
        # Split front matter from content to avoid processing YAML delimiters
        if text.startswith('---'):
            parts = text.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1]
                content = parts[2]
                
                # Only process horizontal rules in content
                hr_pattern = r'^---+\s*$'
                def replace_hr(match):
                    return f'<div class="ornament {content_type}"></div>'
                
                content = re.sub(hr_pattern, replace_hr, content, flags=re.MULTILINE)
                return f'---{front_matter}---{content}'
        
        # No front matter, process entire text
        hr_pattern = r'^---+\s*$'
        def replace_hr(match):
            return f'<div class="ornament {content_type}"></div>'
        
        return re.sub(hr_pattern, replace_hr, text, flags=re.MULTILINE)

    def format_front_matter(self, text: str, is_essay: bool, content_type: str) -> str:
        """Add or modify front matter with appropriate classes and required fields."""
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        if text.startswith('---'):
            # Extract existing front matter
            parts = text.split('---', 2)
            if len(parts) >= 3:
                front_matter = parts[1].strip()
                content = parts[2].strip()
                
                # Ensure no indentation in front matter lines
                front_matter_lines = []
                for line in front_matter.split('\n'):
                    # Remove any leading whitespace from YAML lines
                    clean_line = line.lstrip()
                    if clean_line:  # Only add non-empty lines
                        front_matter_lines.append(clean_line)
                
                front_matter = '\n'.join(front_matter_lines)
                
                # Add essay class if detected
                if is_essay and 'class:' not in front_matter:
                    front_matter += '\nclass: essay'
                elif is_essay and 'class:' in front_matter:
                    front_matter = re.sub(r'class:\s*(.*)$', r'class: \1 essay', front_matter, flags=re.MULTILINE)
                
                # Add missing required fields
                if 'date:' not in front_matter:
                    front_matter += f'\ndate: {current_date}'
                if 'tags:' not in front_matter:
                    front_matter += f'\ntags: [{content_type}]'
                
                # Ensure content starts without indentation
                content = self.normalize_content_indentation(content)
                
                return f'---\n{front_matter}\n---\n\n{content}'
        else:
            # No front matter exists, create complete one
            title = self.extract_title(text)
            layout = 'post' if is_essay else 'page'
            
            # Create properly formatted front matter with no indentation
            front_matter_lines = [
                f'title: "{title}"',
                f'layout: {layout}',
                f'date: {current_date}',
                f'tags: [{content_type}]'
            ]
            
            if is_essay:
                front_matter_lines.append('class: essay')
                
            front_matter = '\n'.join(front_matter_lines)
            
            # Ensure content starts without indentation
            content = self.normalize_content_indentation(text)
            
            return f'---\n{front_matter}\n---\n\n{content}'
        
        return text
    
    def normalize_content_indentation(self, content: str) -> str:
        """Remove problematic leading whitespace that could break Jekyll parsing."""
        lines = content.split('\n')
        normalized_lines = []
        
        for line in lines:
            # Check if line is a heading, list item, or special Markdown syntax
            stripped = line.lstrip()
            
            if (stripped.startswith('#') or 
                stripped.startswith('-') or 
                stripped.startswith('*') or 
                stripped.startswith('>') or 
                stripped.startswith('1.') or
                stripped.startswith('![') or
                stripped.startswith('<') or
                stripped == '---'):
                # These should start at column 0 for proper Markdown parsing
                normalized_lines.append(stripped)
            elif stripped == '':
                # Empty lines
                normalized_lines.append('')
            else:
                # Regular content - remove any leading spaces that could cause code block interpretation
                normalized_lines.append(stripped)
        
        return '\n'.join(normalized_lines)
    
    def extract_title(self, text: str) -> str:
        """Extract title from the first heading or generate one."""
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if line.startswith('# '):
                return line[2:].strip()
        
        # Generate title from first paragraph or filename
        for line in lines:
            line = line.strip()
            if line and not line.startswith('#') and not line.startswith('---'):
                words = line.split()[:6]  # First 6 words
                return ' '.join(words) + ('...' if len(line.split()) > 6 else '')
        
        return "Untitled Document"

    def format_images(self, text: str) -> str:
        """Add appropriate image classes and format captions."""
        # Pattern for images with optional attributes
        img_pattern = r'!\[([^\]]*)\]\(([^)]+)\)(?:\{([^}]+)\})?'
        
        def replace_img(match):
            alt_text = match.group(1)
            src = match.group(2)
            attrs = match.group(3) if match.group(3) else ''
            
            # Determine size class based on content or alt text
            if 'large' in alt_text.lower() or 'wide' in alt_text.lower():
                size_class = 'image-large'
            elif 'small' in alt_text.lower() or 'portrait' in alt_text.lower():
                size_class = 'image-small'
            else:
                size_class = ''  # Standard size
            
            # Format the image
            if size_class and size_class not in attrs:
                if attrs:
                    attrs = f'{attrs} .{size_class}'
                else:
                    attrs = f'.{size_class}'
            
            result = f'![{alt_text}]({src})'
            if attrs:
                result += f'{{{attrs}}}'
            
            return result
        
        return re.sub(img_pattern, replace_img, text)

    def add_drop_cap_guidance(self, text: str, is_essay: bool) -> str:
        """Add comments for drop cap placement if essay class is used."""
        if is_essay:
            # Find the first substantial paragraph
            lines = text.split('\n')
            for i, line in enumerate(lines):
                line = line.strip()
                if (line and 
                    not line.startswith('#') and 
                    not line.startswith('---') and 
                    not line.startswith('<') and
                    len(line.split()) > 10):  # Substantial paragraph
                    
                    # Add comment before the paragraph
                    lines.insert(i, '<!-- Drop cap will be automatically applied to the first paragraph -->')
                    break
            
            return '\n'.join(lines)
        
        return text

    def validate_jekyll_format(self, text: str) -> List[str]:
        """Validate that the formatted text won't cause Jekyll parsing errors."""
        warnings = []
        lines = text.split('\n')
        
        # Check front matter
        if not text.startswith('---'):
            warnings.append("Missing YAML front matter delimiters")
        else:
            front_matter_end = -1
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    front_matter_end = i
                    break
            
            if front_matter_end == -1:
                warnings.append("YAML front matter not properly closed")
            else:
                # Check front matter lines for indentation
                for i in range(1, front_matter_end):
                    line = lines[i]
                    if line.strip() and line.startswith(' '):
                        warnings.append(f"YAML line {i+1} has leading spaces: '{line}'")
        
        # Check for problematic indentation in content
        in_code_block = False
        for i, line in enumerate(lines):
            if line.strip().startswith('```'):
                in_code_block = not in_code_block
                continue
                
            if not in_code_block and line.startswith('  ') and line.strip():
                # Check if this is intentional indentation (like in blockquotes or lists)
                stripped = line.strip()
                if not (stripped.startswith('>') or 
                       any(stripped.startswith(x) for x in ['- ', '* ', '+ ']) or
                       stripped.startswith('1.') or
                       stripped.startswith('<')):
                    warnings.append(f"Line {i+1} has problematic leading spaces: '{line[:20]}...'")
        
        return warnings
    
    def format_document(self, text: str) -> str:
        """Apply all typographic formatting to the document."""
        # Detect content characteristics
        content_type = self.analyze_content_type(text)
        is_essay = self.detect_essay_content(text)
        
        # Apply formatting in order
        text = self.format_front_matter(text, is_essay, content_type)
        text = self.apply_small_caps(text)
        text = self.apply_oldstyle_figures(text)
        text = self.format_blockquotes(text)
        text = self.add_ornaments(text, content_type)
        text = self.format_images(text)
        text = self.add_drop_cap_guidance(text, is_essay)
        
        # Validate the output
        warnings = self.validate_jekyll_format(text)
        if warnings:
            print("⚠️  Formatting warnings detected:")
            for warning in warnings:
                print(f"   - {warning}")
            print()
        
        # Add formatting comment at the end
        comment = f"""
<!-- 
Document formatted with Typographic Formatter for Animal Rationis Capax
Content type detected: {content_type}
Essay classification: {'Yes' if is_essay else 'No'}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-->"""
        
        text += comment
        
        return text

def main():
    if len(sys.argv) < 2:
        print("Usage: python typographic-formatter.py input.md [output.md]")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    
    # Determine output file
    if len(sys.argv) > 2:
        output_file = Path(sys.argv[2])
    else:
        output_file = input_file.parent / f"{input_file.stem}_formatted{input_file.suffix}"
    
    # Read input file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading input file: {e}")
        sys.exit(1)
    
    # Format the document
    formatter = TypographicFormatter()
    formatted_content = formatter.format_document(content)
    
    # Write output file
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
        print(f"Formatted document saved to: {output_file}")
        
        # Print summary
        content_type = formatter.analyze_content_type(content)
        is_essay = formatter.detect_essay_content(content)
        print(f"Content type detected: {content_type}")
        print(f"Essay classification: {'Yes' if is_essay else 'No'}")
        
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()