"""Waveform pixelator"""

import random
from enveditor import EditorSample, Utils
from akscripts.edison.set_sample_to_mono_sum_stereo import set_sample_to_mono_sum_stereo


def wf_division_factory(
    wf_horizontal_values=32,
    wf_length=1024,
):
    """Create a list of frame lengths for the waveforms"""

    wf_division = [0] * wf_horizontal_values

    wf_frame_length = wf_length // wf_horizontal_values

    for i in range(wf_horizontal_values):
        wf_division[i] = wf_frame_length

    wf_frame_length_remainder = wf_length % wf_horizontal_values

    for i in range(wf_frame_length_remainder):
        wf_division[i] += 1

    random.seed(42)
    random.shuffle(wf_division)

    return wf_division


def wf_pixelator(
    wt_nr_of_waveforms=256, wf_horizontal_values=32, wf_vertical_values=64
):
    """Main function"""
    # Settings

    if EditorSample.Length < 1:
        Utils.ShowMessage("No sample loaded")
        return

    # Wavetable settings

    wt_waveforms = [0] * wt_nr_of_waveforms

    # Waveform settings

    wf_division = [0] * wf_horizontal_values
    wf_length = int(EditorSample.Length / wt_nr_of_waveforms)

    # Preprocessing
    set_sample_to_mono_sum_stereo()

    wf_division = wf_division_factory(
        wf_horizontal_values=wf_horizontal_values,
        wf_length=wf_length,
    )

    for idy, frame in enumerate(wt_waveforms):

        wf_start = idy * wf_length

        for idx, frame in enumerate(wf_division):

            start = sum(wf_division[:idx]) + wf_start
            end = sum(wf_division[: idx + 1]) + wf_start

            frame_value = 0.0

            for j in range(start, end, 1):
                sample = EditorSample.GetSampleAt(j, 0)
                frame_value += sample

            frame_value = frame_value / frame
            frame_value = max(min(frame_value, 1), -1)
            frame_value = round(frame_value * wf_vertical_values) / wf_vertical_values

            for j in range(start, end, 1):
                EditorSample.SetSampleAt(j, 0, frame_value)
