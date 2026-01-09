import time
import json
import requests
from bs4 import BeautifulSoup

def clean_text(html_text):
    if not html_text:
        return ""
    soup = BeautifulSoup(html_text, "html.parser")
    text = soup.get_text()
    return ' '.join(text.split())

# Total chapters in Sahih al-Bukhari
TOTAL_CHAPTERS = 97

# Base URLs (chapter number will be appended)
base_urls = {
    'arabic': 'https://sunnah.com/ajax/arabic/bukhari/',
    'english': 'https://sunnah.com/ajax/english/bukhari/',
    'bangla': 'https://sunnah.com/ajax/bangla/bukhari/'
}

all_hadiths = []

print(f"Starting scrape of {TOTAL_CHAPTERS} chapters of Sahih al-Bukhari...")
print("Delay: 30 seconds between chapters\n")

for chapter in range(1, TOTAL_CHAPTERS + 1):
    print(f"챕️ Chapter {chapter}/{TOTAL_CHAPTERS}")
    
    lang_data = {}
    skip_chapter = False

    for lang, base_url in base_urls.items():
        url = f"{base_url}{chapter}"
        print(f"  → Fetching {lang}...")
        try:
            resp = requests.get(url, timeout=20)
            resp.raise_for_status()
            data = resp.json()
            if not isinstance(data, list):
                print(f"    ⚠ Unexpected response format in {lang}, skipping chapter.")
                skip_chapter = True
                break
            indexed = {}
            for item in data:
                key = str(item.get('ourHadithNumber'))
                if key:
                    indexed[key] = clean_text(item.get('hadithText', ''))
            lang_data[lang] = indexed
            print(f"    ✓ Got {len(indexed)} hadiths")
        except Exception as e:
            print(f"    ✗ Error fetching {lang} (Chapter {chapter}): {e}")
            skip_chapter = True
            break

    if skip_chapter:
        print(f"  ❌ Skipping chapter {chapter} due to error.\n")
        continue

    # Merge hadiths using ourHadithNumber
    all_keys = set()
    for d in lang_data.values():
        all_keys.update(d.keys())
    
    sorted_keys = sorted(all_keys, key=int)

    for key in sorted_keys:
        entry = {
            "book_id": 1,
            "chapter_id": chapter,
            "hadith_id": int(key),
            "arabic": lang_data['arabic'].get(key, ""),
            "english": lang_data['english'].get(key, ""),
            "bangla": lang_data['bangla'].get(key, "")
        }
        all_hadiths.append(entry)

    print(f"  ✅ Merged {len(sorted_keys)} hadiths from chapter {chapter}\n")

    # Delay 30 seconds before next chapter (except after last)
    if chapter < TOTAL_CHAPTERS:
        print("⏳ Waiting 30 seconds before next chapter...\n")
        time.sleep(30)

# Save final output
output_file = "bukhari_all_chapters_clean.json"
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(all_hadiths, f, ensure_ascii=False, indent=2)

print(f"🎉 Done! Total hadiths scraped: {len(all_hadiths)}")
print(f"💾 Saved to: {output_file}")