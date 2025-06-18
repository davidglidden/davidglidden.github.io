#!/usr/bin/env python3
"""
Convert Chamber Priority Books
Convert the 68 identified Chamber voice books from the library analysis
"""

import csv
from pathlib import Path
from convert_epub import convert_epub_to_markdown
import time

def get_chamber_books_from_csv():
    """Extract Chamber books from the library CSV"""
    csv_file = Path("apple_books_library.csv")
    
    if not csv_file.exists():
        print("❌ Library CSV not found. Run extract_library_csv.py first")
        return []
    
    # Chamber voice search terms
    chamber_authors = [
        'gaston bachelard', 'bachelard',
        'christopher alexander', 'alexander',
        'walter benjamin', 'benjamin', 
        'hannah arendt', 'arendt',
        'simone weil', 'weil',
        'emmanuel levinas', 'levinas',
        'martin heidegger', 'heidegger',
        'robin wall kimmerer', 'kimmerer',
        'john berger', 'berger'
    ]
    
    chamber_books = []
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for book in reader:
            author_lower = book['author'].lower()
            
            # Check if author matches any Chamber voice
            for search_term in chamber_authors:
                if search_term in author_lower:
                    chamber_books.append({
                        'path': Path(book['path']),
                        'title': book['title'],
                        'author': book['author'],
                        'filename': book['filename']
                    })
                    break
    
    return chamber_books

def convert_chamber_priority():
    """Convert all identified Chamber priority books"""
    
    chamber_books = get_chamber_books_from_csv()
    
    if not chamber_books:
        print("❌ No Chamber books found")
        return
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print(f"🏛️ CONVERTING {len(chamber_books)} CHAMBER PRIORITY BOOKS")
    print("=" * 60)
    
    successful = 0
    failed = 0
    chamber_ready = []
    failed_books = []
    
    # Group by author for better reporting
    by_author = {}
    for book in chamber_books:
        author = book['author']
        if author not in by_author:
            by_author[author] = []
        by_author[author].append(book)
    
    print(f"📚 Chamber voices to convert:")
    for author, books in by_author.items():
        print(f"   • {author}: {len(books)} books")
    
    print(f"\n🚀 Starting conversion...\n")
    
    total_books = len(chamber_books)
    
    for i, book in enumerate(chamber_books, 1):
        epub_path = book['path']
        
        print(f"[{i:3d}/{total_books}] {book['author']}")
        print(f"           {book['title'][:60]}...")
        
        if not epub_path.exists():
            print(f"           ❌ File not found")
            failed += 1
            failed_books.append(f"{book['author']} - {book['title']} (file not found)")
            continue
        
        try:
            start_time = time.time()
            if convert_epub_to_markdown(epub_path, output_dir):
                conversion_time = time.time() - start_time
                successful += 1
                chamber_ready.append(f"{book['author']} - {book['title']}")
                print(f"           ✅ Success ({conversion_time:.1f}s)")
            else:
                failed += 1
                failed_books.append(f"{book['author']} - {book['title']} (conversion failed)")
                print(f"           ❌ Failed")
                
        except KeyboardInterrupt:
            print(f"\n⏸️  Conversion interrupted by user")
            print(f"📊 Progress: {successful} successful, {failed} failed")
            break
            
        except Exception as e:
            failed += 1
            failed_books.append(f"{book['author']} - {book['title']} (error: {str(e)[:50]})")
            print(f"           ❌ Error: {str(e)[:50]}")
        
        # Progress indicator every 10 books
        if i % 10 == 0:
            progress = (successful + failed) / total_books * 100
            print(f"\n📈 Progress: {progress:.1f}% ({successful} successful, {failed} failed)")
    
    # Final report
    print(f"\n📊 CONVERSION COMPLETE")
    print("=" * 60)
    print(f"✅ Successfully converted: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"🏛️ Chamber-ready texts: {len(chamber_ready)}")
    print(f"📈 Success rate: {successful/(successful+failed)*100:.1f}%")
    
    # Voice-specific results
    converted_by_voice = {}
    for book_entry in chamber_ready:
        author = book_entry.split(' - ')[0]
        if author not in converted_by_voice:
            converted_by_voice[author] = 0
        converted_by_voice[author] += 1
    
    print(f"\n🎭 CHAMBER VOICES READY FOR INTEGRATION:")
    for voice, count in sorted(converted_by_voice.items()):
        print(f"   ✅ {voice}: {count} books")
    
    if failed_books:
        print(f"\n❌ FAILED CONVERSIONS ({len(failed_books)}):")
        for failure in failed_books[:10]:  # Show first 10
            print(f"   • {failure}")
        if len(failed_books) > 10:
            print(f"   ... and {len(failed_books) - 10} more")
    
    # Create integration status report
    with open("chamber_conversion_report.txt", "w") as f:
        f.write("CHAMBER LIBRARY CONVERSION REPORT\n")
        f.write("=" * 40 + "\n\n")
        f.write(f"Conversion Date: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Total Chamber books found: {total_books}\n")
        f.write(f"Successfully converted: {successful}\n")
        f.write(f"Failed conversions: {failed}\n")
        f.write(f"Success rate: {successful/(successful+failed)*100:.1f}%\n\n")
        
        f.write("CHAMBER VOICES READY:\n")
        for voice, count in sorted(converted_by_voice.items()):
            f.write(f"  ✅ {voice}: {count} books\n")
        
        f.write(f"\nCONVERTED BOOKS:\n")
        for book in chamber_ready:
            f.write(f"  • {book}\n")
        
        if failed_books:
            f.write(f"\nFAILED CONVERSIONS:\n")
            for failure in failed_books:
                f.write(f"  ❌ {failure}\n")
    
    print(f"\n📄 Detailed report saved to: chamber_conversion_report.txt")
    
    if successful > 0:
        print(f"\n🎉 CHAMBER LIBRARY FOUNDATION ESTABLISHED!")
        print(f"🚀 Next steps:")
        print(f"   1. Run: python3 analyze_library.py")
        print(f"   2. Test Chamber integration with converted texts")
        print(f"   3. Begin dialectical routing system development")
    
    return successful, failed, chamber_ready

if __name__ == "__main__":
    successful, failed, chamber_ready = convert_chamber_priority()
    
    if chamber_ready:
        print(f"\n✨ {len(chamber_ready)} Chamber texts ready for integration")
        print(f"🏛️ The Chamber protocols can now be activated!")