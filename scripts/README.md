# Scripts Directory

This directory contains utility scripts for managing the Open Hadith JSON dataset.

## Available Scripts

### 1. `separate_chapters.py`

Separates hadiths from a single JSON file into individual chapter files.

**Purpose:** Convert a complete hadith collection (e.g., `bukhari.json`) into numbered chapter files (`001.json`, `002.json`, etc.), where each file contains all hadiths for that chapter.

**Usage:**

```bash
# Interactive mode (prompts for input/output paths)
python scripts/separate_chapters.py

# With command-line arguments
python scripts/separate_chapters.py <input_file> <output_directory>

# Example
python scripts/separate_chapters.py bukhari.json books/bukhari/hadiths
```

**Input Format:**
- A JSON file containing an array of hadith objects
- Each hadith must have a `chapter_id` field

**Output:**
- Creates numbered files: `001.json`, `002.json`, ..., `097.json`
- Each file contains an array of all hadiths for that chapter
- Files are saved in the specified output directory

**Example:**
```bash
python scripts/separate_chapters.py bukhari.json books/bukhari/hadiths
```
This will create files like:
- `books/bukhari/hadiths/001.json` (all hadiths from chapter 1)
- `books/bukhari/hadiths/002.json` (all hadiths from chapter 2)
- etc.

---

### 2. `create_hadith_files.py`

Creates empty/template hadith files for manual entry.

**Purpose:** Generate numbered placeholder files for entering hadiths manually.

**Usage:**
```bash
python scripts/create_hadith_files.py
# Prompts: "How many hadith files do you want to create?"
```

**Note:** This script creates individual hadith objects per file, which differs from the recommended structure in the README (arrays of hadiths per chapter). Use `separate_chapters.py` instead for proper structure.

---

### 3. `scraping_script.py`

Automated web scraper for collecting hadith data from sunnah.com.

**Purpose:** Scrape Sahih al-Bukhari hadiths in Arabic, English, and Bangla from sunnah.com.

**⚠️ Important Notes:**
- Uses a 30-second delay between chapters to be respectful to the source website
- Scrapes 97 chapters of Sahih al-Bukhari
- Outputs to `bukhari_all_chapters_clean.json`
- **Use responsibly** and respect website terms of service

**Usage:**
```bash
python scripts/scraping_script.py
```

**Output:**
- Creates `bukhari_all_chapters_clean.json` in the current directory
- Contains all hadiths in a single array
- Use `separate_chapters.py` to split into chapter files

**Dependencies:**
```bash
pip install requests beautifulsoup4
```

---

## Workflow for Adding New Hadiths

### Recommended Workflow:

1. **Scrape data** (if using scraping_script.py):
   ```bash
   python scripts/scraping_script.py
   ```

2. **Separate into chapters**:
   ```bash
   python scripts/separate_chapters.py bukhari_all_chapters_clean.json books/bukhari/hadiths
   ```

3. **Review and validate** the generated files

4. **Commit changes** following the contribution guidelines

---

## Script Maintenance

- All scripts use UTF-8 encoding for proper multilingual support
- Scripts follow Python 3 standards
- Error handling included for common issues
- Progress indicators included for long-running operations

---

## Contributing

When adding new scripts:
1. Follow the existing code style
2. Include proper documentation
3. Add error handling
4. Update this README
5. Test thoroughly before committing

---

## License

These scripts are part of the Open Hadith JSON Dataset project.
See the main LICENSE file for details.
