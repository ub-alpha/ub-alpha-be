from rest_framework import mixins, generics, status
from rest_framework.views import APIView
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
        
        if mission[0].category == 'daily' and len(Log.objects.filter(member=request.user, mission=mission_id, created_at=datetime.datetime.now().date())) != 0:
            return Response({
                "detail": "Duplicated access"
            }, status=status.HTTP_400_BAD_REQUEST)

        return self.create(request, args, kwargs)

class LogUpdateView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def put(self, request, *args, **kwargs):
        member = request.user
        log = Log.objects.filter(pk=kwargs.get('pk'), member=member)\
                        .select_related('mission')

        if len(log) == 0:
            return Response({
                "detail": "You are trying to do wrong user's mission"
            },status=status.HTTP_400_BAD_REQUEST)
        
        log = log[0]

        if log.status != 'ready':
            return Response({
                "detail": "Duplicated access"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        log.status = 'done'
        log.save()

        member.point += log.mission.point
        member.save()

        return Response({
            "mission": log.mission_id,
            "status": log.status,
        }, status=status.HTTP_200_OK)