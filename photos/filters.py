from wsgiref.validate import validator
from django_filters.rest_framework import FilterSet, DateFilter, CharFilter

from photos.models import Photo
from django.forms import CharField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

from .utils import get_locations_nearby_coords


class GeoCoordinatesField(CharField):
    """
    Custom field to process geo coordinates (latitude and longitude) 
    via CharField in django-filter
    """

    def validate(self, value):
        try:
            lat, lon = value.split(',')
        except ValueError:
            raise ValidationError(
                _('Please specify both Lat and Lon in the following format: lat,lon'),
                code='invalid'
            )

        try:
            assert -90 <= float(lat) <= 90
            assert -180 <= float(lon) <= 180
        except AssertionError:
            raise ValidationError(
                _('Lat and Lon should be an integer or float'), code='invalid')

    def clean(self, value):
        if not value:
            return
        value = super().clean(value)
        return value.split(',')


class GeoFilter(CharFilter):
    field_class = GeoCoordinatesField


class PhotoFilter(FilterSet):
    """
    Implementation of filter for photo objects
    """

    date = DateFilter(field_name='user_date')
    name = CharFilter(
        field_name='people_names',
        lookup_expr='icontains'
    )
    geo = GeoFilter(method='filter_by_geo', required=False,
                    label='Geo coordinates',
                    help_text=_(
                        """Example: 90,180. 
                        Should be in range -90 <= Lat <= 90 and -180 <= Lon <= 180
                        """
                    ))

    class Meta:
        model = Photo
        fields = ('date', 'name', 'geo')

    def filter_by_geo(self, qs, name, value):
        lat, lon = value
        near_by_locations = get_locations_nearby_coords(qs, lat, lon)
        return near_by_locations
