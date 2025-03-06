# from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample
from enveditor import EditorSample


def find_peaks(peak_search_start, peak_search_end):
    """Find largest and smallest peaks and their positions."""
    largest_peak = float("-inf")
    smallest_peak = float("inf")
    largest_peak_position = None
    smallest_peak_position = None

    for i in range(peak_search_start, peak_search_end):
        sample_value = EditorSample.GetSampleAt(i, 0)
        abs_sample_value = abs(sample_value)
        if abs_sample_value > largest_peak:
            largest_peak = abs_sample_value
            largest_peak_position = i
        if abs_sample_value < smallest_peak:
            smallest_peak = abs_sample_value
            smallest_peak_position = i

    return largest_peak, smallest_peak, largest_peak_position, smallest_peak_position
