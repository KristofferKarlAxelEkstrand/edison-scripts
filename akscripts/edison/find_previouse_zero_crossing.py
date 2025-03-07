"""Find the previous zero crossing."""

from enveditor import EditorSample


def find_previouse_zero_crossing(sample_start_point, search_area):
    """Find the previous zero crossing."""
    for i in range(sample_start_point, search_area, -1):
        if EditorSample.GetSampleAt(i, 0) < 0:
            return i
    return None
