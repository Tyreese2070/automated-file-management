import os
import shutil
from pathlib import Path

# File Types
FILE_CATEGORIES = {
    'Documents': ['.doc', '.docx', '.pdf', '.txt', '.xls', '.xlsx', '.csv', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.sh', '.bat', '.js'],
    'Executables': ['.exe', '.bin', '.dll'],
    'Others': ['.iso', '.log', '.cfg', '.ini']
}

# Create folders if they don't exist
def create_folders(base_path):
    for category in FILE_CATEGORIES:
        folder_path =  os.path.join(base_path, category)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

# Move files to the correct folder
def move_files(base_path):
    for item in os.listdir(base_path):
        item_path = os.path.join(base_path, item)

        if os.path.isdir(item_path):
            continue

        file_ext = Path(item).suffix.lower()
        moved = False

        for category, extensions in FILE_CATEGORIES.item():
            if file_ext in extensions:
                shutil.move(item_path, os.path.join(base_path, category, item))
                print(f"Moved: {item} to {category}")
                moved = True
                break
        
        if not moved:
            shutil.move(item_path, os.path.join(base_path, 'Others', item))
            print(f"Moved: {item} to Others")

def organise_files(base_path):
    create_folders(base_path)
    move_files(base_path)

if __name__ == "__main__":
    folder_to_organise = input("Enter path to a folder you want to organise: ")
    organise_files(folder_to_organise)