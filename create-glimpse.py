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
    geolocator = Nominatim(user_agent="arc-photo-poster")
    location = geolocator.reverse((lat, lon), language='en')
    return location.address if location else "unknown-location"

def extract_camera_info(tags):
    """Extract camera and settings information from EXIF"""
    camera_make = tags.get("Image Make", "")
    camera_model = tags.get("Image Model", "")
    iso = tags.get("EXIF ISOSpeedRatings", "")
    aperture = tags.get("EXIF FNumber", "")
    shutter = tags.get("EXIF ExposureTime", "")
    
    camera_info = ""
    if camera_make and camera_model:
        camera_info = f"{camera_make} {camera_model}".strip()
    
    settings = []
    if aperture:
        f_val = float(aperture.values[0].num) / float(aperture.values[0].den)
        settings.append(f"f/{f_val:.1f}")
    if shutter:
        if shutter.values[0].den == 1:
            settings.append(f"{shutter.values[0].num}s")
        else:
            settings.append(f"{shutter.values[0].num}/{shutter.values[0].den}s")
    if iso:
        settings.append(f"ISO {iso}")
    
    if camera_info and settings:
        return f"{camera_info}, {', '.join(settings)}"
    elif camera_info:
        return camera_info
    elif settings:
        return ', '.join(settings)
    else:
        return ""

def extract_exif(image_path):
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f, details=False)

    # Extract date
    date_tag = tags.get("EXIF DateTimeOriginal", None)
    if date_tag:
        date_obj = datetime.strptime(str(date_tag), "%Y:%m:%d %H:%M:%S")
        date_str = date_obj.strftime("%Y-%m-%d")
        time_str = date_obj.strftime("%H:%M")
    else:
        date_str = input("Date (YYYY-MM-DD): ").strip()
        time_str = input("Time (HH:MM, optional): ").strip()

    # Extract GPS coordinates
    try:
        lat = convert_to_degrees(tags["GPS GPSLatitude"].values)
        if tags["GPS GPSLatitudeRef"].values != "N":
            lat = -lat
        lon = convert_to_degrees(tags["GPS GPSLongitude"].values)
        if tags["GPS GPSLongitudeRef"].values != "E":
            lon = -lon
        location_coords = f"{lat:.6f}, {lon:.6f}"
        location_name = reverse_geocode(lat, lon)
    except KeyError:
        location_coords = input("Location coordinates (lat,lon, optional): ").strip()
        location_name = input("Location name: ").strip()

    # Extract camera information
    camera_info = extract_camera_info(tags)
    if not camera_info:
        camera_info = input("Camera info (optional): ").strip()

    # Get human input
    suggested_title = location_name.split(",")[0] if location_name else "Untitled Glimpse"
    title = input(f"Title for {os.path.basename(image_path)} [{suggested_title}]: ").strip() or suggested_title
    
    # Suggest location for glimpse
    if location_name:
        # Extract city/country for glimpse location field
        parts = [part.strip() for part in location_name.split(",")]
        if len(parts) >= 2:
            suggested_location = f"{parts[0]}, {parts[-1]}"  # City, Country
        else:
            suggested_location = parts[0]
    else:
        suggested_location = ""
    
    location = input(f"Glimpse location [{suggested_location}]: ").strip() or suggested_location
    description = input("Brief description (1-2 sentences): ").strip()
    tags_input = input("Tags [en, travel, seen]: ").strip() or "en, travel, seen"

    # Create filenames
    filename = os.path.basename(image_path)
    extension = os.path.splitext(filename)[1].lower()
    slug = sanitize_slug(f"{date_str}-{title}")
    new_filename = f"{slug}{extension}"
    
    # Use _posts directory for glimpses (not _photos)
    output_md_path = f"_posts/{slug}.md"
    img_dest_path = f"assets/img/{new_filename}"

    # Copy image
    os.makedirs("assets/img", exist_ok=True)
    shutil.copy(image_path, img_dest_path)

    # Create glimpse post
    os.makedirs("_posts", exist_ok=True)
    with open(output_md_path, 'w') as f:
        f.write("---\n")
        f.write(f'title: "{title}"\n')
        
        # Add time if available
        if time_str:
            f.write(f"date: {date_str} {time_str}\n")
        else:
            f.write(f"date: {date_str}\n")
        
        if location:
            f.write(f'location: "{location}"\n')
        if location_coords:
            f.write(f"coordinates: {location_coords}\n")
        
        f.write(f"tags: [{tags_input}]\n")
        f.write("class: glimpse\n")
        f.write("ornament: glimpse\n")
        
        if camera_info:
            f.write(f'camera: "{camera_info}"\n')
        
        if description:
            f.write(f"description: {description}\n")
        else:
            f.write("description: \n")
        
        f.write("---\n\n")
        f.write(f'<img src="/assets/img/{new_filename}" alt="{title}">\n')

    print(f"✓ Created glimpse: {output_md_path}")
    print(f"✓ Image copied to: {img_dest_path}")

if __name__ == "__main__":
    folder_path = os.path.dirname(os.path.realpath(__file__))
    supported_extensions = [".jpg", ".jpeg", ".png", ".tiff", ".JPG", ".JPEG", ".PNG", ".TIFF"]
    images = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1] in supported_extensions]

    print(f"Found {len(images)} image(s) in folder.")
    print("Creating glimpse semantic type posts...\n")
    
    for image_file in images:
        print(f"→ Processing: {image_file}")
        extract_exif(os.path.join(folder_path, image_file))
        print()