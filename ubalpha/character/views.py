from rest_framework import generics, mixins

from .models import Character
from .serializers import CharacterSerializer

class CharacterListView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.all().order_by('max_origin')
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)