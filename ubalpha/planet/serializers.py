from rest_framework import serializers

from .models import Planet, Detail

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required=False
    )
    
    class Meta:
        model = Detail
        fields = '__all__'
