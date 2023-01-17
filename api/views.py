from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser
from django_filters.rest_framework import DjangoFilterBackend
from photos.models import Photo
from photos.filters import PhotoFilter
from photos.serializers import PhotoDetailSerializer, PhotoListSerializer

User = get_user_model()


class PhotoViewSet(viewsets.ModelViewSet):
    """
    create: Add new photo
    retrieve: Get photo by id
    list: Retrieve list of photos (with ability to filter by params)
    update: Update photo by id
    delete: Delete photo by id
    """

    queryset = Photo.objects.all()
    serializer_class = PhotoListSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]
    parser_classes = [MultiPartParser]
    filterset_class = PhotoFilter
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        if self.action in ["create", "retrieve"]:
            return PhotoDetailSerializer
        return PhotoListSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED,
            headers=headers
        )
