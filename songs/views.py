from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from rest_framework.pagination import PageNumberPagination
from .serializers import SongSerializer
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_list_or_404


class SongView(ListCreateAPIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Song.objects.all()
    serializer_class = SongSerializer

    def get_queryset(self):
        return get_list_or_404(Song, album_id=self.kwargs["pk"])

    def perform_create(self, serializer):
        return serializer.save(album_id=self.kwargs["pk"])
