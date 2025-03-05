""" Find the closest zero crossing from the start and the end of the sample. """

# from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample
from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample


def sample_start_on_zero_crossing(region_sample):
    """Check if the sample starts on a zero crossing."""
    if region_sample[len(region_sample) - 1] * region_sample[0] < 0:
        return True

    return False


def find_zero_crossing(region_sample, start, end, step):
    """Find the closest zero crossing between start and end positions."""
    for i in range(start, end, step):
        if region_sample[i] * region_sample[i + step] < 0:
            return i
    return None


def shift_sample_so_it_starts_on(region_sample, new_start=0):
    """Shift the sample so it starts on given sample."""

    sample_length = len(region_sample)

    shifted_sample = [0] * sample_length

    for i in range(sample_length):
        new_position = (i - new_start) % sample_length
        shifted_sample[new_position] = region_sample[i]

    for i in range(sample_length):
        EditorSample.SetSampleAt(i, 0, shifted_sample[i])

    return shifted_sample


def get_regions_samples(region):
    """Get the samples of the region."""
    sample_length = region.SampleEnd - region.SampleStart
    sample_start = region.SampleStart

    regions_sample = [0] * sample_length
    for i in range(sample_length):
        new_position = (i + sample_start) % sample_length
        regions_sample[new_position] = EditorSample.GetSampleAt(i, 0)

    return regions_sample


def write_data(region, region_sample):

    sample_length = len(region_sample)
    sample_start = region.SampleStart

    for i in range(sample_length):
        EditorSample.SetSampleAt(i + sample_start, 0, 0)

    return


def region_sample_shift_start_and_end():
    """Find the closest zero crossing from the start and the end of the sample."""

    if EditorSample.NumChans > 1:
        Utils.ShowMessage("This script is only for mono samples.")
        return

    regions = EditorSample.RegionCount

    for index in range(regions):
        region = EditorSample.GetRegion(index)
        region_sample = get_regions_samples(region)
        sample_length = len(region_sample)

        region.Name = (
            "Region "
            + str(index + 1)
            + " (start: "
            + str(region.SampleStart)
            + ", end: "
            + str(region.SampleEnd)
            + ")"
        )

        if sample_start_on_zero_crossing(region_sample=region_sample):
            region.Name = region.Name + " (start on zero crossing)"

        start_zero_crossing = find_zero_crossing(region_sample, 0, sample_length - 1, 1)
        end_zero_crossing = find_zero_crossing(region_sample, sample_length - 1, 0, -1)

        new_start = 0

        if start_zero_crossing < sample_length - end_zero_crossing:
            new_start = start_zero_crossing
        else:
            new_start = end_zero_crossing

        # region_sample = shift_sample_so_it_starts_on(region_sample, new_start)

        write_data(region, region_sample)

        region_sample = []

    return
