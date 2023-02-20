from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from .models import Planet, Detail
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
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = DetailSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        details = Detail.objects.all()

        if self.request.method == 'GET':
            details = details.filter(member_id=self.request.user.id)

        return details.order_by('id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def get(self, request, *args, **kwargs):
        print(request.method)
        return self.list(request, *args, **kwargs)