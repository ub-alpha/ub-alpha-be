from rest_framework import generics, mixins

from .models import Planet
from .serializers import PlanetSerializer

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