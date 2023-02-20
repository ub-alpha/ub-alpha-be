from rest_framework import mixins, generics
from .models import Mission
from .serializers import MissionSerializer

class MissionListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MissionSerializer

    def get_queryset(self):
        return Mission.objects.all().order_by('id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)