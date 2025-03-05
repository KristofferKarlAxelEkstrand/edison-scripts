""" Set the waveform markers in Edison. """

from enveditor import EditorSample


def set_waveform_regions(nr_of_waveforms=64, waveform_sample_length=1024):
    """Set the waveform markers."""

    number_of_regions = nr_of_waveforms

    for i in range(number_of_regions):

        region_start = waveform_sample_length * i
        region_end = (waveform_sample_length * (i + 1)) - 1

        region_name = f"{i}"
        if number_of_regions >= 10000:
            region_name = f"{i + 1:05}"
        elif number_of_regions >= 1000:
            region_name = f"{i + 1:04}"
        elif number_of_regions >= 100:
            region_name = f"{i + 1:03}"
        elif number_of_regions >= 10:
            region_name = f"{i + 1:02}"

        EditorSample.AddRegion(region_name, region_start, region_end)
