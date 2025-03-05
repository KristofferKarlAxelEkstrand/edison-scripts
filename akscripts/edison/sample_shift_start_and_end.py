""" This script sets the value of a variable to 0. """

# from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample
from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample


def sample_start_on_zero_crossing():
    """Check if the sample starts on a zero crossing."""
    if (
        EditorSample.GetSampleAt(EditorSample.Length - 1, 0)
        * EditorSample.GetSampleAt(0, 0)
        < 0
    ):
        return True

    return False


def find_zero_crossing(start, end, step):
    """Find the closest zero crossing between start and end positions."""
    for i in range(start, end, step):
        if EditorSample.GetSampleAt(i, 0) * EditorSample.GetSampleAt(i + step, 0) < 0:
            return i
    return None


def shift_sample_so_it_starts_on(new_start=0):
    """Shift the sample so it starts on given sample."""

    sample_length = EditorSample.Length

    shifted_sample = [0] * sample_length
    for i in range(sample_length):
        new_position = (i - new_start) % sample_length
        shifted_sample[new_position] = EditorSample.GetSampleAt(i, 0)

    for i in range(sample_length):
        EditorSample.SetSampleAt(i, 0, shifted_sample[i])


def sample_shift_start_and_end():
    """Find the closest zero crossing from the start and the end of the sample."""

    regions = EditorSample.RegionCount

    for index in range(regions):
        region_to_delete = regions - 1 - index

        EditorSample.DeleteRegion(region_to_delete)

    if EditorSample.NumChans > 1:
        Utils.ShowMessage("This script is only for mono samples.")
        return

    if sample_start_on_zero_crossing():
        return

    sample_length = EditorSample.Length

    start_zero_crossing = find_zero_crossing(0, sample_length - 1, 1)
    end_zero_crossing = find_zero_crossing(sample_length - 1, 0, -1)

    new_start = 0

    if start_zero_crossing < EditorSample.Length - end_zero_crossing:
        new_start = start_zero_crossing
    else:
        new_start = end_zero_crossing

    shift_sample_so_it_starts_on(new_start)
