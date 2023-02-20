from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Planet
from .serializers import PlanetSerializer, DetailSerializer

class PlanetListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = PlanetSerializer

    def get_queryset(self):
        return Planet.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class DetailCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = DetailSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)