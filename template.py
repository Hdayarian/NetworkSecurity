from pathlib import Path
import os
import logging

# Configure logging (add this if not already done)
logging.basicConfig(level=logging.INFO)

list_of_files = [
    ".github/workflows/main.yaml",      # FILE
    "Network_Data/",                    # DIRECTORY (trailing / indicates dir)
    "notebooks/",                       # DIRECTORY (fixed typo: noteboks -> notebooks)
    "networksecurity/__init__.py",      # FILE
    "networksecurity/components/",      # DIRECTORY (add / to make it directory)
    "networksecurity/constants/",       # DIRECTORY
    "networksecurity/entity/",          # DIRECTORY
    "networksecurity/logging/",         # DIRECTORY
    "networksecurity/exception/",       # DIRECTORY
    "networksecurity/pipeline/",        # DIRECTORY
    "networksecurity/utils/",           # DIRECTORY
    "networksecurity/cloud/",           # DIRECTORY
    "README.md",                        # FILE
    "requirements.txt",                 # FILE
    "setup.py",                         # FILE
    ".gitignore",                       # FILE
    "Dockerfile",                       # FILE
    ".env",                             # FILE
]

for item_path in list_of_files:
    filepath = Path(item_path)
    
    # STEP 1: Normalize path (remove trailing / for file checks)
    clean_path = filepath if not str(filepath).endswith('/') else Path(str(filepath).rstrip('/'))
    
    # STEP 2: Check if it's a DIRECTORY (trailing / OR no extension)
    is_directory = (
        str(filepath).endswith('/') or 
        ('.' not in clean_path.name) or  # No dot = likely directory (components, utils, etc.)
        clean_path.name.startswith('__') # __init__.py is file, but others without . are dirs
    )
    
    # STEP 3: CREATE DIRECTORY if needed
    if is_directory:
        filepath.parent.mkdir(parents=True, exist_ok=True)  # Create parent dirs
        filepath.mkdir(exist_ok=True)  # Create this directory
        logging.info(f"✅ Directory created: {filepath}")
    
    # STEP 4: CREATE FILE if it's a file
    else:
        filepath.parent.mkdir(parents=True, exist_ok=True)  # Ensure parent exists
        
        if not filepath.exists() or filepath.stat().st_size == 0:
            filepath.touch()  # Clean way to create empty file
            logging.info(f"📄 Empty file created: {filepath}")
        else:
            logging.info(f"📄 File already exists: {filepath}")

print("🎉 All directories and files created successfully!")