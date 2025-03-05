""" This script converts the current sample to mono by averaging the channels. """

# from enveditor import Editor, EditorSample, Utils, MEEditor, ScriptDialog, Sample
from enveditor import EditorSample


def set_sample_to_mono_sum_stereo():
    """Convert the sample to mono by averaging the channels."""
    num_channels = EditorSample.NumChans
    sample_length = EditorSample.Length

    if num_channels > 1:
        for i in range(sample_length):
            sample_sum = 0.0
            for channel in range(num_channels):
                sample_sum += EditorSample.GetSampleAt(i, channel)
            mono_sample_value = sample_sum / num_channels
            for channel in range(num_channels):
                EditorSample.SetSampleAt(i, channel, mono_sample_value)

        EditorSample.NumChans = 1
