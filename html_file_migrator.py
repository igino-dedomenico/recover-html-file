import os
import shutil
import json

# Configure folders
SOURCE_FOLDER = "./angular-project"     # Change this to the Angular project path
BACKUP_FOLDER = "./backup-html"         # Where to store original HTML files
NEW_HTML_FOLDER = "./bootstrap5-html"   # Folder containing updated HTML files
STRUCTURE_FILE = "./structure.json"     # File to store original file structure

def find_html_files(directory):
    """Find all HTML files recursively in the directory, excluding node_modules."""
    html_files = []
    for root, _, files in os.walk(directory):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))
    return html_files

def backup_html_files():
    """Copy all HTML files from the source project to the backup folder and save the file structure."""
    if not os.path.exists(BACKUP_FOLDER):
        os.makedirs(BACKUP_FOLDER)
    
    html_files = find_html_files(SOURCE_FOLDER)
    structure = {}
    
    for file in html_files:
        relative_path = os.path.relpath(file, SOURCE_FOLDER)
        structure[relative_path] = file
        destination = os.path.join(BACKUP_FOLDER, os.path.basename(file))  # Save without folder structure
        shutil.copy2(file, destination)
        print(f"Copied: {file} -> {destination}")
    
    # Save the file structure
    with open(STRUCTURE_FILE, "w") as f:
        json.dump(structure, f, indent=4)
    print(f"Structure saved to {STRUCTURE_FILE}")

def replace_html_files():
    """Replace original HTML files with updated ones based on the saved structure."""
    if not os.path.exists(STRUCTURE_FILE):
        print("Error: Structure file not found! Run the backup first.")
        return
    
    with open(STRUCTURE_FILE, "r") as f:
        structure = json.load(f)
    
    for relative_path, original_path in structure.items():
        updated_file = os.path.join(NEW_HTML_FOLDER, os.path.basename(original_path))
        destination = os.path.join(SOURCE_FOLDER, relative_path)
        
        if os.path.exists(updated_file):
            shutil.copy2(updated_file, destination)
            print(f"Replaced: {updated_file} -> {destination}")
        else:
            print(f"Warning: Updated file {updated_file} not found!")

if __name__ == "__main__":
    choice = input("Choose an operation: [1] Backup HTML files, [2] Replace HTML files: ")
    if choice == "1":
        backup_html_files()
    elif choice == "2":
        replace_html_files()
    else:
        print("Invalid choice.")
