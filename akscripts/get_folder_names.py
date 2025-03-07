"""Get all the folder names in a directory."""

import os


def get_folder_names(directory):
    """Get all the folder names in a directory."""
    return [
        name
        for name in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, name))
    ]
