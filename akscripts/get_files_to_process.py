"""Get the files to process."""

import os
import re

from akscripts.get_folders_under_path import get_folders_under_path


def get_files_to_process(path, regex_pattern):
    """Get the files to process."""
    folders = get_folders_under_path(path)
    files_to_process = []

    for folder in folders:
        current_folders_files = os.listdir(path + folder)
        # regex_pattern = r" - \d{2}.wav"
        current_folders_files_process = [
            f"{path}{folder}\\{file}"
            for file in current_folders_files
            if re.search(regex_pattern, file)
        ]

        files_to_process += current_folders_files_process

    return files_to_process
