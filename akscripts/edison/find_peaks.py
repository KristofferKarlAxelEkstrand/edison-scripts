# from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample
from enveditor import EditorSample


def find_peaks(peak_search_start, peak_search_end):
    """Find the largest positive peak over 0.5 and its position."""
    largest_peak = 0.0
    largest_peak_position = None

    for i in range(peak_search_start, peak_search_end):
        sample_value = EditorSample.GetSampleAt(i, 0)
        if sample_value > largest_peak:
            largest_peak = sample_value
            largest_peak_position = i

    return largest_peak, largest_peak_position


def find_peaks_sample(samples):
    """Find the largest positive peak and its position in the given array of samples."""
    largest_peak = 0.0
    largest_peak_position = None

    for i, sample_value in enumerate(samples):
        if sample_value > largest_peak:
            largest_peak = sample_value
            largest_peak_position = i

    return largest_peak, largest_peak_position
