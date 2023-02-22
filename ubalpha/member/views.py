from rest_framework import mixins, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import MemberSerializer
from .models import Member

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
        member.save()

        return Response({
            "spacename": member.spacename
        }, status=status.HTTP_200_OK)
    
class MemberPointView(
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.all()
    
    def put(self, request, *args, **kwargs):
        return self.partial_update(request, args, kwargs)