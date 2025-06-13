#!/usr/bin/env python3
import os
import exifread
import shutil
import re
from datetime import datetime
from geopy.geocoders import Nominatim

def convert_to_degrees(value):
    d, m, s = [v.num / v.den for v in value]
    return d + (m / 60.0) + (s / 3600.0)

def sanitize_slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')

def reverse_geocode(lat, lon):
    geolocator = Nominatim(user_agent="arc-photo-essay-creator")
    location = geolocator.reverse((lat, lon), language='en')
    return location.address if location else "unknown-location"

def extract_date_from_exif(image_path):
    """Extract date from first image with EXIF data"""
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        date_tag = tags.get("EXIF DateTimeOriginal", None)
        if date_tag:
            return datetime.strptime(str(date_tag), "%Y:%m:%d %H:%M:%S").strftime("%Y-%m-%d")
    except:
        pass
    return None

def extract_gps_from_exif(image_path):
    """Extract GPS coordinates from image"""
    try:
        with open(image_path, 'rb') as f:
            tags = exifread.process_file(f, details=False)
        
        lat = convert_to_degrees(tags["GPS GPSLatitude"].values)
        if tags["GPS GPSLatitudeRef"].values != "N":
            lat = -lat
        lon = convert_to_degrees(tags["GPS GPSLongitude"].values)
        if tags["GPS GPSLongitudeRef"].values != "E":
            lon = -lon
        return lat, lon
    except:
        return None, None

def create_photo_essay():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    supported_extensions = [".jpg", ".jpeg", ".png", ".tiff", ".JPG", ".JPEG", ".PNG", ".TIFF"]
    images = sorted([f for f in os.listdir(folder_path) if os.path.splitext(f)[1] in supported_extensions])
    
    if not images:
        print("No images found in current directory.")
        return
    
    print(f"Found {len(images)} image(s) for photo essay:")
    for i, img in enumerate(images, 1):
        print(f"  {i}. {img}")
    
    # Get essay metadata
    print("\n--- Photo Essay Details ---")
    title = input("Photo essay title: ").strip()
    if not title:
        print("Title is required for photo essays.")
        return
    
    # Try to extract date from first image
    auto_date = extract_date_from_exif(os.path.join(folder_path, images[0]))
    if auto_date:
        date_str = input(f"Date [{auto_date}]: ").strip() or auto_date
    else:
        date_str = input("Date (YYYY-MM-DD): ").strip()
    
    # Try to extract location from first image
    lat, lon = extract_gps_from_exif(os.path.join(folder_path, images[0]))
    if lat and lon:
        location_name = reverse_geocode(lat, lon)
        parts = [part.strip() for part in location_name.split(",")]
        if len(parts) >= 2:
            suggested_location = f"{parts[0]}, {parts[-1]}"  # City, Country
        else:
            suggested_location = parts[0]
        location = input(f"Location [{suggested_location}]: ").strip() or suggested_location
    else:
        location = input("Location: ").strip()
    
    series = input("Series name (optional): ").strip()
    description = input("Essay description: ").strip()
    tags_input = input("Tags [en, photography, essay]: ").strip() or "en, photography, essay"
    
    # Create essay intro
    print("\n--- Essay Content ---")
    print("Enter the opening text for your photo essay.")
    print("This will appear before the first image (with drop cap).")
    print("Press Enter twice when finished:")
    
    intro_lines = []
    empty_count = 0
    while empty_count < 2:
        line = input()
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0
        intro_lines.append(line)
    
    # Remove trailing empty lines
    while intro_lines and intro_lines[-1].strip() == "":
        intro_lines.pop()
    
    intro_text = "\n".join(intro_lines)
    
    # Create filenames and copy images
    slug = sanitize_slug(f"{date_str}-{title}")
    output_md_path = f"_posts/{slug}.md"
    
    os.makedirs("assets/img", exist_ok=True)
    image_info = []
    
    for i, image_file in enumerate(images, 1):
        filename = os.path.basename(image_file)
        extension = os.path.splitext(filename)[1].lower()
        new_filename = f"{slug}-{i:02d}{extension}"
        img_dest_path = f"assets/img/{new_filename}"
        
        # Copy image
        shutil.copy(os.path.join(folder_path, image_file), img_dest_path)
        
        # Get caption for this image
        caption = input(f"Caption for image {i} ({image_file}): ").strip()
        
        image_info.append({
            'filename': new_filename,
            'caption': caption,
            'alt': caption or f"{title} - Image {i}"
        })
        
        print(f"✓ Copied: {image_file} → {img_dest_path}")
    
    # Create photo essay post
    os.makedirs("_posts", exist_ok=True)
    with open(output_md_path, 'w') as f:
        # Frontmatter
        f.write("---\n")
        f.write(f'title: "{title}"\n')
        f.write(f"date: {date_str}\n")
        
        if location:
            f.write(f'location: "{location}"\n')
        if series:
            f.write(f'series: "{series}"\n')
        
        f.write(f"images: {len(images)}\n")
        f.write(f"tags: [{tags_input}]\n")
        f.write("class: photo-essay\n")
        f.write("ornament: photo-essay\n")
        
        if description:
            f.write(f"description: {description}\n")
        else:
            f.write("description: \n")
        
        f.write("---\n\n")
        
        # Essay content
        if intro_text.strip():
            # Add drop cap to first paragraph
            paragraphs = intro_text.split('\n\n')
            if paragraphs:
                f.write(f'<p class="drop-cap">{paragraphs[0]}</p>\n\n')
                # Add remaining paragraphs
                for para in paragraphs[1:]:
                    if para.strip():
                        f.write(f"{para}\n\n")
        
        # Add images with spacing for text between
        for i, img_info in enumerate(image_info):
            f.write("<figure>\n")
            f.write(f'  <img src="/assets/img/{img_info["filename"]}" alt="{img_info["alt"]}">\n')
            if img_info['caption']:
                f.write(f'  <figcaption>{img_info["caption"]}</figcaption>\n')
            f.write("</figure>\n\n")
            
            # Prompt for text after each image (except the last)
            if i < len(image_info) - 1:
                print(f"\n--- Text after image {i+1} ---")
                print("Enter text to appear after this image (optional).")
                print("Press Enter twice when finished (or just Enter twice to skip):")
                
                text_lines = []
                empty_count = 0
                while empty_count < 2:
                    line = input()
                    if line.strip() == "":
                        empty_count += 1
                    else:
                        empty_count = 0
                    text_lines.append(line)
                
                # Remove trailing empty lines
                while text_lines and text_lines[-1].strip() == "":
                    text_lines.pop()
                
                if text_lines and any(line.strip() for line in text_lines):
                    text_content = "\n".join(text_lines)
                    f.write(f"{text_content}\n\n")
        
        # Prompt for closing text
        print("\n--- Closing Text ---")
        print("Enter closing text for your photo essay (optional).")
        print("Press Enter twice when finished:")
        
        closing_lines = []
        empty_count = 0
        while empty_count < 2:
            line = input()
            if line.strip() == "":
                empty_count += 1
            else:
                empty_count = 0
            closing_lines.append(line)
        
        # Remove trailing empty lines
        while closing_lines and closing_lines[-1].strip() == "":
            closing_lines.pop()
        
        if closing_lines and any(line.strip() for line in closing_lines):
            closing_text = "\n".join(closing_lines)
            f.write(f"{closing_text}\n\n")
    
    print(f"\n✓ Created photo essay: {output_md_path}")
    print(f"✓ {len(images)} images copied to assets/img/")
    print(f"✓ Essay structure: intro + {len(images)} images + closing")

if __name__ == "__main__":
    print("Photo Essay Creator")
    print("==================")
    print("This script will create a photo essay from all images in the current directory.")
    print("Images will be processed in alphabetical order.\n")
    
    create_photo_essay()