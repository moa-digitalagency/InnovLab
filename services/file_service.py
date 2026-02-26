import os
from werkzeug.utils import secure_filename
from flask import current_app

def save_file(file_storage, subfolder=None):
    """
    Saves the file to the configured UPLOAD_FOLDER (with optional subfolder).
    Ensures the directory exists.
    Returns the secure filename.
    """
    if not file_storage or not file_storage.filename:
        return None

    filename = secure_filename(file_storage.filename)

    # Base upload folder from config
    base_folder = current_app.config.get('UPLOAD_FOLDER')

    # Fallback if not set (though it should be)
    if not base_folder:
        # Assuming standard structure relative to app root
        static_folder = current_app.static_folder if current_app.static_folder else 'statics'
        base_folder = os.path.join(current_app.root_path, static_folder, 'uploads')

    target_folder = base_folder
    if subfolder:
        target_folder = os.path.join(base_folder, subfolder)

    try:
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        destination = os.path.join(target_folder, filename)
        file_storage.save(destination)

        return filename
    except Exception as e:
        current_app.logger.error(f"File Save Error: {e}")
        return None
