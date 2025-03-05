""" Resample the current sample to a target sample length and return the new sample rate. """

from enveditor import EditorSample


def resample_get_sample_rate(target_sample_length=93952):
    """Get the sample rate of the current sample."""

    initial_sample_rate = EditorSample.SampleRate
    initial_sample_length = EditorSample.Length

    ratio = target_sample_length / initial_sample_length

    new_sample_rate = int(initial_sample_rate * ratio)

    if new_sample_rate < 0 and new_sample_rate > 100000000:
        new_sample_rate = False

    return new_sample_rate
