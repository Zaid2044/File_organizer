<h1 align="center">🗂️ File Organizer</h1>
<p align="center">
  A Python script that automatically organizes files in a directory by categorizing them into folders based on file type.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/CLI-Tool-4CAF50?style=flat"/>
  <img src="https://img.shields.io/badge/Automation-%F0%9F%94%8C-blue?style=flat"/>
</p>

---

## 🧠 Overview

**File Organizer** is a simple but powerful Python automation script that helps you clean up messy folders (like Downloads or Desktop) by moving files into subfolders based on their file extensions.

For example:

* `.jpg`, `.png` → moved to `Images/`
* `.pdf`, `.docx` → moved to `Documents/`
* `.mp4`, `.mkv` → moved to `Videos/`
* and so on...

---

## ✨ Features

* 📂 Automatically creates and populates folders by file type
* ⚙️ Customizable file type mappings
* 🔁 Can be re-run multiple times (non-destructive)
* 📦 Supports all major file formats

---

## 🔍 File Categories (Default)

| Folder    | Extensions                                |
| --------- | ----------------------------------------- |
| Images    | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`   |
| Documents | `.pdf`, `.docx`, `.txt`, `.pptx`, `.xlsx` |
| Videos    | `.mp4`, `.mkv`, `.mov`, `.avi`            |
| Audio     | `.mp3`, `.wav`, `.aac`, `.flac`           |
| Archives  | `.zip`, `.rar`, `.tar`, `.gz`, `.7z`      |
| Scripts   | `.py`, `.js`, `.sh`, `.bat`               |
| Others    | Everything else                           |

> You can easily customize or extend these in the code.

---

## ⚙️ Setup Instructions

### ✅ Prerequisites

* Python 3.9 or above
* Git or direct download of `.py` script

### 📦 Installation

```bash
git clone https://github.com/Zaid2044/File_organizer.git
cd File_organizer
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt  # (Optional, if using additional libraries)
```

---

