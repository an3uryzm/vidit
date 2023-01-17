from rest_framework import serializers
from rest_framework.fields import ListField

from .models import Photo


class PhotoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image']


class StringArrayField(ListField):
    """
    String representation of an array field.
    """

    def to_internal_value(self, data):
        # Should be a better way to handle ArrayField than this
        data = data[0].split(",")
        return super().to_internal_value(data)


class PhotoDetailSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(
        min_value=-90, max_value=90, required=False)
    longitude = serializers.FloatField(
        min_value=-180, max_value=180, required=False)
    people_names = StringArrayField(required=False)

    class Meta:
        model = Photo
        exclude = ('user', )
