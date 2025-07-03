import sys
import shutil

def backup_file():
    if len(sys.argv) > 1:
        original_file = sys.argv[1]
        backup_file = original_file + ".bak"
        try:
            shutil.copy(original_file, backup_file)
            print(f"Backup created: {backup_file}")
        except Exception as e:
            print(f"Error creating backup: {e}")
    else:
        print("No file name provided.")


backup_file()
