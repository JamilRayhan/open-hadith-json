# Contributing to Open Hadith JSON Dataset

Thank you for your interest in contributing 🌱
This project is a **community-driven, open Hadith dataset** intended for developers, researchers, and educational use.

Contributions help improve:

* Accuracy
* Language coverage
* Data completeness
* Long-term sustainability

---

## 🧭 Guiding Principles

Before contributing, please understand these core principles:

1. **Faithfulness over interpretation**
   Translations must reflect the original text, not personal explanations.

2. **Transparency over authority**
   Grading and metadata must always include references.

3. **Consistency over convenience**
   Follow existing structure and naming strictly.

---

## 🤝 Ways to Contribute

You can contribute in the following ways:

### 🌍 Add a New Language

* Add translations in a new language (e.g. `urdu`, `hindi`)
* Language keys must be:

  * lowercase
  * English names
  * consistent across files

### ✏️ Correct Errors

* Typographical mistakes
* Formatting issues
* Incorrect or incomplete translations

### 🐞 Report Issues

* Missing Hadiths
* Incorrect metadata
* Structural problems

### 📖 Add Missing Content

* Missing chapters
* Missing Hadith entries
* Incomplete book metadata

---

## 📁 Repository Structure (Important)

```text
books/
├── bukhari/
│   ├── book.json
│   ├── chapters.json
│   └── hadiths/
│       ├── 001.json
│       ├── 002.json
│       └── ...
```

* Each **Hadith file** contains an **array of Hadith objects**
* Each file represents **one chapter**

---

## 📄 Hadith Data Format

Every Hadith object **must** follow this structure:

```json
{
  "book_id": 1,
  "chapter_id": 1,
  "hadith_id": 1,
  "arabic": "…",
  "english": "…",
  "bangla": "…"
}
```

### ✅ Rules

* All IDs must be **integers**
* `arabic` text is **mandatory**
* Other languages are **optional**
* No HTML tags
* No formatting markup
* No commentary or explanation

---

## 🌍 Adding a New Language

1. Choose a valid language key:

   * `urdu`
   * `hindi`
   * `indonesian`

2. Add the language field to the Hadith object:

```json
"urdu": "حضرت عمر بن خطابؓ سے روایت ہے..."
```

3. Ensure:

* Unicode text
* Faithful translation
* No transliteration unless part of the original translation

---

## 🏷️ Tags (Future Feature)

Tags are optional and **topic-based**.

```json
"tags": ["intention", "niyyah", "actions"]
```

Rules:

* Lowercase
* English only
* No spaces (use hyphen if needed)
* Topics only (not interpretation)

> ⚠️ Tags should be added carefully and sparingly.

---

## 📚 Hadith Grades & References (Future Feature)

Grades must **always include authority and reference**.

```json
"grades": [
  {
    "grade": "sahih",
    "authority": "al-Albani",
    "reference": "Sahih al-Jami 1/1"
  }
]
```

Rules:

* Multiple grades allowed
* No grading without reference
* No claim of absolute authority

---

## 🧾 Metadata (`meta`)

Metadata appears at the root level of book or chapter files.

```json
"meta": {
  "source": "sunnah.com (text reference)",
  "languages": ["arabic", "english", "bangla"],
  "last_updated": "YYYY-MM-DD",
  "version": "x.y.z"
}
```

---

## 🐞 Reporting Issues

Please open a GitHub Issue and include:

* Book name
* Chapter ID
* Hadith ID
* Description of the issue
* Reference source (if available)

**Example title:**

```
[Bukhari 1:1] English translation typo
```

---

## 🔄 Pull Request Guidelines

Before submitting a Pull Request:

* ✅ Validate JSON locally if possible
* ✅ Keep changes focused
* ❌ Do not reformat unrelated files
* ❌ Do not reorder Hadiths unnecessarily
* ❌ Do not add personal opinions

Small, focused PRs are reviewed and merged faster.

---

## 🤖 CI Validation

All Pull Requests are automatically checked:

* JSON validity
* Schema compliance
* Structural consistency

PRs that fail validation **cannot be merged**.

---

## ⚠️ Disclaimer

This dataset is provided for **educational and research purposes only**.

* This is not a religious authority
* Always verify Hadiths with trusted scholarly sources
* Grading opinions may differ among scholars

---

## 🤲 Final Note

Your contribution helps make Islamic knowledge more accessible to the world.

May Allah reward you for your effort and intention.

---