# 📜 Open Hadith JSON Dataset

A **clean, structured, multilingual Hadith dataset** in JSON format, organized **by book**, designed for **developers, researchers, and Islamic applications**.

This repository is **community-driven** and aims to provide an **open, verifiable, and extensible** Hadith dataset that anyone can use and improve.

---

## 🌍 Supported Languages

Currently included:

* **Arabic**
* **English**
* **Bangla**

Planned / welcome:

* Urdu
* Hindi
* Indonesian
* Turkish
* French
* Malay
* Any other language

Contributors are encouraged to add new languages via Pull Requests.

---

## 📁 Repository Structure

```text
hadith-json/
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── schema.json
├── books/
│   ├── bukhari/
│   │   ├── book.json
│   │   ├── chapters.json
│   │   └── hadiths/
│   │       ├── 001.json
│   │       ├── 002.json
│   │       └── ...
│   ├── muslim/
│   └── abu_dawood/
```

### 📌 Design Philosophy

* **One book per directory**
* **One chapter per Hadith file**
* **One Hadith = One JSON object**
* Multilingual text stored in a **single object**

---

## 📘 Book Metadata (`book.json`)

```json
{
  "book_id": 1,
  "book_data": {
    "hadith_count": 7277,
    "arabic": {
      "title": "صحيح البخاري",
      "author": "الإمام محمد بن إسماعيل البخاري",
      "introduction": ""
    },
    "english": {
      "title": "Sahih al-Bukhari",
      "author": "Imam Muhammad ibn Ismail al-Bukhari",
      "introduction": ""
    },
    "bangla": {
      "title": "সহিহ বুখারী",
      "author": "ইমাম মুহাম্মদ ইবনে ইসমাইল আল-বুখারী",
      "introduction": ""
    }
  }
}
```

---

## 📂 Chapters (`chapters.json`)

```json
[
  {
    "chapter_id": 1,
    "book_id": 1,
    "arabic": "كتاب بدء الوحى",
    "english": "Revelation",
    "bangla": "ওহীর সূচনা"
  }
]
```

---

## 📄 Hadith Format

Each Hadith object follows this structure:

```json
{
  "book_id": 1,
  "chapter_id": 1,
  "hadith_id": 1,
  "arabic": "حَدَّثَنَا الْحُمَيْدِيُّ...",
  "english": "Narrated Umar bin Al-Khattab...",
  "bangla": "উমর ইবনুল খাত্তাব (রা.) থেকে বর্ণিত..."
}
```

### ✅ Rules

* All IDs are **integers**
* `arabic` text is **mandatory**
* Other languages are **optional**
* No HTML or formatting tags
* No commentary or interpretation

---
## 🔮 Future Improvements

The following enhancements are planned and will be introduced in a backward-compatible way.

### 🏷️ Hadith Tags (Topics)
Hadiths may include an optional `tags` field to enable topic-based classification.

Example:
```json
"tags": ["intention", "niyyah", "actions"]
````

Tags will:

* Be lowercase
* Use English for consistency
* Represent topics, not interpretation

---

### 📚 Hadith Grading & References

Hadiths may include an optional `grades` array to store scholarly grading with references.

Example:

```json
"grades": [
  {
    "grade": "sahih",
    "authority": "al-Albani",
    "reference": "Sahih al-Jami 1/1"
  }
]
```

⚠️ Hadith grading can differ among scholars.
This dataset records grading opinions with references and does not claim absolute authority.

### 📄 Extended Hadith Object

```json
{
  "book_id": 1,
  "chapter_id": 1,
  "hadith_id": 1,

  "arabic": "…",
  "english": "…",
  "bangla": "…",

  "tags": ["intention", "niyyah", "actions"],

  "grades": [
    {
      "grade": "sahih",
      "authority": "al-Bukhari",
      "reference": "Sahih al-Bukhari, Hadith 1"
    },
    {
      "grade": "sahih",
      "authority": "Muslim",
      "reference": "Sahih Muslim 1907"
    }
  ]
}
```

## 🧾 Metadata (`meta`)

Each dataset includes a metadata block:
The meta object is included at the root level of book and chapter JSON files where applicable
```json
"meta": {
  "source": "sunnah.com (text reference)",
  "languages": ["arabic", "english", "bangla"],
  "last_updated": "2026-01-09",
  "version": "1.0.0",
  "generated_by": "open-hadith-json community",
  "license": "see LICENSE file"
}
```

---

## 📐 JSON Schema Validation

All Hadith files must conform to `schema.json`.

* CI automatically validates JSON on every PR
* Invalid structure = PR blocked
* New languages are allowed without schema changes

---

## 🤝 How to Contribute

We welcome:

* 🌍 New language translations
* ✏️ Text corrections
* 🐞 Error reports
* 📖 Missing Hadith entries

Please read **[CONTRIBUTING.md](CONTRIBUTING.md)** before submitting a Pull Request.

---

## 🐞 Reporting Issues

If you find an issue, please include:

* Book name
* Chapter ID
* Hadith ID
* Description of the problem
* Reference source (if available)

Example issue title:

```
[Bukhari 1:1] Bangla translation typo
```

---

## 🧠 Use Cases

* Islamic mobile apps
* Ramadan planners
* Search engines
* Academic research
* NLP & AI training
* Educational platforms

---

## ⚠️ Disclaimer

This dataset is provided for **educational and research purposes only**.

* This is **not** an official religious authority
* Always verify Hadith with trusted scholarly sources
* Texts are compiled from **public references**

---

## 🚫 Non-Goals

This project does not aim to:
- Provide religious rulings (fatwa)
- Replace scholarly study
- Enforce a single grading opinion


## 📜 License

This project is open-source.

Please see the `LICENSE` file for details.
Attribution is appreciated.


## 📖 Citation

If you use this dataset in research or applications, please cite the repository.

---

## 🌱 Vision

> To build the most **accessible, clean, and community-maintained Hadith dataset** on the web.

If you believe in **open knowledge**, you’re welcome to contribute.

---

## 🤲 Duʿāʾ

May Allah accept this effort and make it beneficial for the Ummah.
