import sys
import os

# Add the parent directory to sys.path to allow importing from the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import Config

def check_directory(path):
    """
    Checks if a directory exists and is writable.
    """
    if not os.path.exists(path):
        print(f"[FAIL] Directory does not exist: {path}")
        return False

    if not os.path.isdir(path):
        print(f"[FAIL] Path exists but is not a directory: {path}")
        return False

    if not os.access(path, os.W_OK):
        print(f"[FAIL] Directory is not writable: {path}")
        return False

    print(f"[OK] Directory exists and is writable: {path}")
    return True

def main():
    print("Checking system directories...")

    base_upload_folder = Config.UPLOAD_FOLDER

    # Check base upload folder first
    if not base_upload_folder:
        print("[FAIL] UPLOAD_FOLDER is not configured in Config.")
        sys.exit(1)

    # Resolve absolute path if it's relative
    if not os.path.isabs(base_upload_folder):
        # Assuming run from repo root if relative path is used in Config
        # Config.UPLOAD_FOLDER is usually constructed relative to __file__ in config/settings.py
        # which means it should already be absolute. Let's trust Config.
        pass

    directories_to_check = [
        base_upload_folder,
        os.path.join(base_upload_folder, 'logos'),
        os.path.join(base_upload_folder, 'resumes'),
        os.path.join(base_upload_folder, 'pitch_decks')
    ]

    all_good = True
    for directory in directories_to_check:
        if not check_directory(directory):
            all_good = False

    if all_good:
        print("\nSystem check passed: All directories are ready.")
        sys.exit(0)
    else:
        print("\nSystem check failed: Some directories are missing or invalid.")
        sys.exit(1)

if __name__ == "__main__":
    main()
