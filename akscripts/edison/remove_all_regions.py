""" Remove all regions from the current sample. """

from enveditor import EditorSample


def remove_all_regions():
    """Remove all regions from the current sample"""
    regions = EditorSample.RegionCount

    for index in range(regions):
        region_to_delete = regions - 1 - index

        EditorSample.DeleteRegion(region_to_delete)
