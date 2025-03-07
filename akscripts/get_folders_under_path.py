"""Get the folders under the path."""

import os


def get_folders_under_path(path):
    """Get the folders under the path."""
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    return folders
