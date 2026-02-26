import sys
import os

# Add the parent directory to sys.path to allow importing from the app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.settings import Config

def ensure_directory(path):
    """
    Ensures that a directory exists and is writable.
    Creates it if it doesn't exist.
    """
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as e:
        print(f"[FAIL] Could not create directory: {path}. Error: {e}")
        return False

    if not os.path.isdir(path):
        print(f"[FAIL] Path exists but is not a directory: {path}")
        return False

    if not os.access(path, os.W_OK):
        print(f"[FAIL] Directory is not writable: {path}")
        return False

    print(f"[OK] Directory ready: {path}")
    return True

def main():
    print("Verifying and preparing system directories...")

    base_upload_folder = Config.UPLOAD_FOLDER

    # Check base upload folder first
    if not base_upload_folder:
        print("[FAIL] UPLOAD_FOLDER is not configured in Config.")
        sys.exit(1)

    directories_to_check = [
        base_upload_folder,
        os.path.join(base_upload_folder, 'logos'),
        os.path.join(base_upload_folder, 'resumes'),
        os.path.join(base_upload_folder, 'pitch_decks')
    ]

    all_good = True
    for directory in directories_to_check:
        if not ensure_directory(directory):
            all_good = False

    if all_good:
        print("\nSystem check passed: All directories are ready.")
        sys.exit(0)
    else:
        print("\nSystem check failed: Some directories could not be prepared.")
        sys.exit(1)

if __name__ == "__main__":
    main()
