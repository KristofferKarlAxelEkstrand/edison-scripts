"""Crop sample."""

from enveditor import EditorSample


def crop_sample_around_region(region, padding=0):
    """Crop sample."""

    crop_start = region.SampleStart
    crop_end = region.SampleEnd

    crop_end_padded = int(crop_end + padding)

    EditorSample.DeleteFromTo(
        int(crop_end_padded),
        int(EditorSample.Length - 1),
    )

    crop_start_padded = int(crop_start - padding)

    region.SampleStart = region.SampleStart - crop_start_padded
    region.SampleEnd = region.SampleEnd - crop_start_padded

    EditorSample.DeleteFromTo(0, crop_start_padded)

    return
