#!/bin/bash
# Download Essential Eastern Texts for Chamber Integration
# Using curl to avoid Python dependency issues

echo "🌏 DOWNLOADING ESSENTIAL EASTERN PHILOSOPHICAL TEXTS"
echo "======================================================"
echo "Using curl to download public domain texts directly"
echo

# Create directories
mkdir -p public_domain_texts
mkdir -p converted_texts

cd public_domain_texts

echo "📚 [1/6] Laozi: Tao Te Ching (James Legge translation)"
if curl -L -o "Laozi_Tao_Te_Ching.epub" "https://www.gutenberg.org/ebooks/216.epub.noimages"; then
    echo "  ✅ Downloaded successfully"
else
    echo "  ❌ Download failed"
fi

echo
echo "📚 [2/6] Confucius: The Analects"
if curl -L -o "Confucius_Analects.epub" "https://www.gutenberg.org/ebooks/3330.epub.noimages"; then
    echo "  ✅ Downloaded successfully"
else
    echo "  ❌ Download failed"
fi

echo
echo "📚 [3/6] Mencius: Works"
if curl -L -o "Mencius_Works.epub" "https://www.gutenberg.org/ebooks/2895.epub.noimages"; then
    echo "  ✅ Downloaded successfully"
else
    echo "  ❌ Download failed"
fi

echo
echo "📚 [4/6] The Dhammapada (Buddhist text)"
if curl -L -o "Buddha_Dhammapada.epub" "https://www.gutenberg.org/ebooks/2017.epub.noimages"; then
    echo "  ✅ Downloaded successfully"
else
    echo "  ❌ Download failed"
fi

echo
echo "📚 [5/6] The I Ching (Book of Changes)"
if curl -L -o "I_Ching_Book_of_Changes.epub" "https://www.gutenberg.org/ebooks/16888.epub.noimages"; then
    echo "  ✅ Downloaded successfully"
else
    echo "  ❌ Download failed"
fi

echo
echo "📚 [6/6] Alternative Tao Te Ching translation"
if curl -L -o "Laozi_Tao_Te_Ching_Alt.txt" "https://www.gutenberg.org/ebooks/10945.txt.utf-8"; then
    echo "  ✅ Downloaded successfully"
else
    echo "  ❌ Download failed"
fi

echo
echo "📊 DOWNLOAD SUMMARY:"
echo "Files downloaded to: $(pwd)"
ls -la *.epub *.txt 2>/dev/null | wc -l | xargs echo "   Total files:"

echo
echo "🔄 CONVERTING TO CHAMBER FORMAT..."
echo "Attempting pandoc conversion for EPUB files..."

cd ../converted_texts

# Function to convert EPUB to Markdown with Chamber frontmatter
convert_epub_to_chamber() {
    local epub_file="$1"
    local title="$2" 
    local author="$3"
    local voice="$4"
    
    echo "  🔄 Converting: $title"
    
    # Base filename for output
    local base_name=$(basename "$epub_file" .epub)
    local md_file="${base_name}.md"
    
    # Try pandoc conversion
    if command -v pandoc >/dev/null 2>&1; then
        if pandoc "../public_domain_texts/$epub_file" -f epub -t markdown -o "$md_file" 2>/dev/null; then
            echo "    ✅ Pandoc conversion successful"
            
            # Add Chamber YAML frontmatter
            local temp_file="${md_file}.tmp"
            cat > "$temp_file" << EOF
---
title: "$title"
author: "$author"
voice: "$voice"
canonical: true
source_format: "public_domain_epub"
date_converted: "$(date '+%Y-%m-%d')"
segment_strategy: "chapter"
file: "$md_file"
tags: ["public_domain", "eastern_philosophy"]
quote_style: "aphoristic"
acquisition_source: "project_gutenberg"
copyright_status: "public_domain"
---

EOF
            cat "$md_file" >> "$temp_file"
            mv "$temp_file" "$md_file"
            echo "    🎭 Chamber YAML frontmatter added"
            echo "    ✅ $voice voice ACTIVATED"
            return 0
        else
            echo "    ❌ Pandoc conversion failed"
            return 1
        fi
    else
        echo "    ⚠️  Pandoc not available - install with: brew install pandoc"
        return 1
    fi
}

# Convert each downloaded EPUB
convert_epub_to_chamber "Laozi_Tao_Te_Ching.epub" "Tao Te Ching" "Laozi" "Laozi"
convert_epub_to_chamber "Confucius_Analects.epub" "The Analects" "Confucius" "Confucius"  
convert_epub_to_chamber "Mencius_Works.epub" "Mencius" "Mencius" "Mencius"
convert_epub_to_chamber "Buddha_Dhammapada.epub" "The Dhammapada" "Buddha" "Buddha"
convert_epub_to_chamber "I_Ching_Book_of_Changes.epub" "The I Ching" "Ancient Chinese" "I Ching Oracle"

echo
echo "🏛️ CHAMBER STATUS UPDATE:"
activated_voices=$(ls -1 *.md 2>/dev/null | wc -l)
echo "   🎭 Voices activated: $activated_voices"
echo "   🌏 Eastern foundation: Established"
echo "   📚 Source-aware capacity: Enhanced"

echo
echo "📋 NEXT STEPS:"
echo "   1. Run: python3 chamber_amphitheater_status.py"
echo "   2. Test Eastern-Western voice dialogues"
echo "   3. Continue with contemporary Eastern acquisitions"

echo
echo "✨ PUBLIC DOMAIN EASTERN INTEGRATION COMPLETE!"
echo "🎭 The Chamber now has ancient Eastern wisdom voices available for philosophical dialogue"