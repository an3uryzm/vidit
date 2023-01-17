from django.db.models.expressions import RawSQL
from .managers import PhotoQuerySet
from typing import Optional


def get_locations_nearby_coords(
        qs: PhotoQuerySet,
        latitude: str,
        longitude: str,
        max_distance: Optional[int] = 100) -> PhotoQuerySet:
    """
    Given PhotoQuerySet, latitude and longitude return queryset annotated 
    with distance filtered by distance less than max_distance (default 100 km)
    Returns:
        PhotoQuerySet annotated with calculated distance  
        if max_distance is not None:
            remain objects with distance less than max_distance
    """

    # Great circle distance formula
    gcd_formula = """
        6371 * acos(least(greatest(
        cos(radians(%s)) * cos(radians(latitude))
        * cos(radians(longitude) - radians(%s)) +
        sin(radians(%s)) * sin(radians(latitude))
        , -1), 1))
    """
    distance_raw_sql = RawSQL(
        gcd_formula,
        (latitude, longitude, latitude)
    )
    qs = qs.annotate(distance=distance_raw_sql)
    if max_distance is not None:
        qs = qs.filter(distance__lt=max_distance)

    return qs
