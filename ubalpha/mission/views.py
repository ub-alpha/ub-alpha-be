from rest_framework import mixins, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

import datetime

from .models import Mission, Log
from .serializers import MissionSerializer, LogSerializer

class MissionListView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MissionSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):
        return Mission.objects.all().order_by('id')

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)
    
    def get(self, request, *args, **kwargs):
        return self.list(request, args, kwargs)

class LogCreateView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = LogSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def post(self, request, *args, **kwargs):
        mission_id = request.data.get('mission')
        mission = Mission.objects.filter(id=mission_id)
        if mission[0].category == 'welcome':
            if len(Log.objects.filter(mission=mission_id)) != 0:
                return Response({
                    "detail": "Duplicated access"
                }, status=status.HTTP_400_BAD_REQUEST)
        
        if len(Log.objects.filter(mission=mission_id, created_at=datetime.datetime.now().date())) != 0:
            return Response({
                "detail": "Duplicated access"
            }, status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, args, kwargs)