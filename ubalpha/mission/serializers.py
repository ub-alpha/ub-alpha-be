from rest_framework import serializers

from .models import Mission, Log

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'

class LogSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required=False
    )
    
    class Meta:
        model = Log
        fields = '__all__'