import re
from enveditor import EditorSample


def get_note_name_from_regions():
    """Get note name."""
    found_note_matches = []
    region_count = EditorSample.RegionCount
    note_name = "error"
    pattern = re.compile(r"^[A-G]#?\d{1,2}$")

    if region_count == 0:
        return note_name

    for i in range(region_count - 1, -1, -1):
        current_region_name = EditorSample.GetRegion(i).Name.strip()
        if pattern.match(current_region_name) is None:
            continue
        found_note_matches.append(current_region_name)

    note_name = max(found_note_matches, key=len) if found_note_matches else "error"

    return note_name
