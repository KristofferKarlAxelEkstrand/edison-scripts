"""Convert the sample to mono using only the left channel."""

from enveditor import EditorSample


def set_sample_to_mono_left():
    """Convert the sample to mono using only the left channel."""
    num_channels = EditorSample.NumChans
    sample_length = EditorSample.Length

    if num_channels > 1:
        for i in range(sample_length):
            left_channel_value = EditorSample.GetSampleAt(i, 0)
            for channel in range(num_channels):
                EditorSample.SetSampleAt(i, channel, left_channel_value)

        EditorSample.NumChans = 1  # Set the number of channels to 1 (mono)
