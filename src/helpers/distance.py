import haversine as hs
from haversine import Unit

""" Measure distances between two GPS coordinates
"""


def get_distance(location_one: tuple, location_two: tuple) -> float:
    """ Measure distances between two GPS coordinates

    Parameters
    ----------
    location_one

    location_two

    Returns
    -------
    float
        distance between two locations in meters

    """
    try:
        distance = hs.haversine(location_one, location_two, unit=Unit.METERS)
        return distance
    except Exception as e:
        print(str(e))
