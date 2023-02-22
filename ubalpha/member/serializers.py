from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Too short password')
        return make_password(value)
    
    class Meta:
        model = Member
        fields = ('id', 'username', 'password', 'point')
        extra_kwargs = {
            "id":{
                "read_only": True,
            },
            "password": {
                "write_only": True,
            },
        }