
# 🛠 Angular HTML Backup & Replacement Script

A powerful and customizable Python script to **backup and replace HTML files in Angular projects**, especially useful when upgrading from **Bootstrap 4 to Bootstrap 5** or performing large-scale HTML refactoring.

---

## 🚀 Key Features

- 📦 **Backup HTML files** from your Angular project into a safe directory.
- 🔁 **Replace HTML files** with updated versions while preserving the original folder structure.
- 🔍 Automatically **excludes `node_modules`** to keep things clean.
- 🧩 Easy to **customize paths, logic, and file types**.
- 🛡 Prevents accidental loss during migration or refactoring.

---

## 📁 Folder Structure

project-root/
│
├── angular-project/         # Your original Angular project (source)
├── backup-html/             # Folder where backups of .html files are stored
├── bootstrap5-html/         # Folder where updated HTML files are placed
├── structure.json           # Map of original file paths for replacement
└── html_file_migrator.py    # This script
---

## ⚙️ Configuration

In `html_file_migrator.py`, you can configure these variables:


SOURCE_FOLDER = "./angular-project"
BACKUP_FOLDER = "./backup-html"
NEW_HTML_FOLDER = "./bootstrap5-html"
STRUCTURE_FILE = "./structure.json"


Customize as needed to match your project structure.

---

## ▶️ How to Use

### 1. Backup HTML Files

Backs up all `.html` files (excluding `node_modules`) and records their original locations.

```bash
python html_file_migrator.py
```

Select:  
`[1] Backup HTML files`

---

### 2. Replace HTML Files

Replaces the original `.html` files with their updated versions from `bootstrap5-html/`, based on the paths stored in `structure.json`.

```bash
python html_file_migrator.py
```

Select:  
`[2] Replace HTML files`

---

## 💡 Use Cases

- ✅ Bootstrap 4 → Bootstrap 5 migration  
- ✅ Large-scale HTML template updates  
- ✅ Angular project refactoring  
- ✅ Safe, reversible HTML file edits  
- ✅ Multi-page HTML cleanup  

---

## 🧠 Customization Ideas

- Add support for other file types like `.ts`, `.scss`, or `.css`.
- Modify `find_html_files()` to include/exclude folders.
- Automate inside a CI/CD pipeline or GitHub Action.

---

## 📈 SEO Keywords

**angular html migration**, **html file backup python**, **replace html angular project**,  
**bootstrap 5 migration tool**, **html file migrator script**, **python replace html in folder**,  
**safe html upgrade angular**

---

## 📄 License

This script is released under the **MIT License**.  
Feel free to use, customize, and share.
