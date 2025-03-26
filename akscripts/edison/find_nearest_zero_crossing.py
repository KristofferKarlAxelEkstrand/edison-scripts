"""Find the previous zero crossing."""

from enveditor import EditorSample


def is_zero_crossing(sample_start_point):
    """Check if the sample at the sample_start_point is a zero crossing."""

    previous_sample = EditorSample.GetSampleAt(sample_start_point - 1, 0)
    current_sample = EditorSample.GetSampleAt(sample_start_point, 0)
    next_sample = EditorSample.GetSampleAt(sample_start_point + 1, 0)

    if current_sample == 0:
        return True

    if (
        current_sample < 0
        and previous_sample > 0
        or current_sample > 0
        and previous_sample < 0
    ):
        return True

    if current_sample < 0 and next_sample > 0 or current_sample > 0 and next_sample < 0:
        return True


def find_nearest_zero_crossing(sample_start_point, search_area):
    """Find the zero crossing closest to the sample_start_point."""
    closest_zero_crossing = None
    closest_distance = float("inf")

    if is_zero_crossing(sample_start_point):
        closest_distance = 0
        closest_zero_crossing = sample_start_point

    # Search backwards
    for i in range(sample_start_point - 1, sample_start_point - search_area, -1):
        if is_zero_crossing(i):
            distance = abs(sample_start_point - i)
            closest_distance = distance
            closest_zero_crossing = i

    # Search forwards
    for i in range(sample_start_point + 1, sample_start_point + search_area):
        if is_zero_crossing(i):
            distance = abs(sample_start_point - i)
            if distance < closest_distance:
                closest_distance = distance
                closest_zero_crossing = i

    return closest_zero_crossing
