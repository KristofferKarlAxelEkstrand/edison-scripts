""" Get all the file names in a directory. """

import os


def get_file_names(directory):
    """Get all the file names in a directory."""
    return [
        name
        for name in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, name))
    ]
