from rest_framework import mixins, generics
from .models import Member
from .serializers import MemberSerializer

class MemberView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MemberSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, args, kwargs)

class MemberDetailView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    generics.GenericAPIView,
):
    serializer_class = MemberSerializer

    def get_queryset(self):
        return Member.objects.all().order_by('id')
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)