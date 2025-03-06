""" This module generates a list of notes and their corresponding frequencies. """


def notes_dict_factory():
    """This function generates a list of notes and their corresponding frequencies."""

    def calculate_frequency(t, n):
        return t * (2 ** (n / 12.0))

    def calculate_nr_of_samples(note_frequency, sample_rate, cycles):
        sample_rate = sample_rate * cycles
        if note_frequency > 0:
            samples_per_cycle = (sample_rate) / note_frequency
        else:
            samples_per_cycle = float("inf")
        return samples_per_cycle

    # Settings
    tuning_note_index = 33
    tuning = 440.0
    sample_rate = 48000
    nr_of_octaves = 11
    nr_of_notes_in_one_octave = 12
    samples_per_cycle_cycles_list = [2**i for i in range(0, 33)]

    # Names of the notes
    note_names = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

    notes_dict = {}

    for note_index in range(0, nr_of_octaves * nr_of_notes_in_one_octave):
        current_octave = note_index // nr_of_notes_in_one_octave
        note = note_index % nr_of_notes_in_one_octave
        note_name = note_names[note] + str(current_octave)
        name_without_octave = note_names[note]
        note_frequency = calculate_frequency(tuning, note_index - tuning_note_index)

        samples_per_cycles = []
        for cycles in samples_per_cycle_cycles_list:
            samples_per_cycles.append(
                calculate_nr_of_samples(note_frequency, sample_rate, cycles)
            )

        prefered_samples_per_cycle = 0
        prefered_samples_per_cycle_x2 = 0
        prefered_samples_per_cycle_x4 = 0

        for samples_per_cycle in samples_per_cycles:
            if (
                samples_per_cycle > 512
                and prefered_samples_per_cycle > 0
                and samples_per_cycle > samples_per_cycles[0]
            ):
                prefered_samples_per_cycle_x2 = samples_per_cycle
                prefered_samples_per_cycle_x4 = samples_per_cycle * 2
                break
            if (
                samples_per_cycle > 512
                and prefered_samples_per_cycle <= 0
                and samples_per_cycle > samples_per_cycles[0]
            ):
                prefered_samples_per_cycle = samples_per_cycle

        notes_dict[note_name] = {
            "name": note_name,
            "name_without_octave": name_without_octave,
            "index": note_index,
            "frequency": note_frequency,
            "samples_per_cycles": samples_per_cycles,
            "prefered_samples_per_cycle": prefered_samples_per_cycle,
            "prefered_samples_per_cycle_x2": prefered_samples_per_cycle_x2,
            "prefered_samples_per_cycle_x4": prefered_samples_per_cycle_x4,
        }

    return notes_dict
