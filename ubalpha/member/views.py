from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Member
from .serializers import MemberSerializer

class MemberRegisterView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberDetailView(
    APIView
):
    serializer_class = MemberSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    
    def get(self, request, *args, **kwargs):
        member = request.user
        return Response({
            "spacename": member.spacename,
            "point": member.point,
        }, status=status.HTTP_200_OK)
    
    def put(self, request, *args, **kwargs):
        spacename = request.data.get('spacename')
        if len(spacename) > 10 or spacename == "":
            return Response({
                "detail": "space name should not be null and length of space name should be less than 11"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        member = request.user
        member.spacename = spacename

        return Response({
            "spacename": member.spacename
        }, status=status.HTTP_200_OK)