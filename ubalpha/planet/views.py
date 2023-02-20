from rest_framework import generics, mixins, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Planet, Detail
from character.models import Character

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
        return self.list(request, *args, **kwargs)

class DetailView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def put(self, request, *args, **kwargs):
        member = request.user
        detail = Detail.objects.filter(pk=kwargs.get('pk'), member=member)

        if member.point < 10:
            return Response({
                "detail": "You need more than 10 points to level up your planet"
            },status=status.HTTP_400_BAD_REQUEST)

        if len(detail) == 0:
            return Response({
                "detail": "You are trying to level up wrong user's planet"
            },status=status.HTTP_400_BAD_REQUEST)
        
        detail = detail[0]
        character = Character.objects.get(pk=detail.planet.id)

        if detail.point >= character.max_point:
            return Response({
                "detail": "It's already max level"
            },status=status.HTTP_400_BAD_REQUEST)
        
        detail.point += 10
        member.point -= 10

        if detail.point >= character.max_point:
            detail.status = "ununsed"
        
        detail.save()
        member.save()

        return Response({
            "remained_point": member.point,
            "planet_point": detail.point,
        })
    
    class DetailCouponView(APIView):
        def put(self, request, *args, **kwargs):
            pass
