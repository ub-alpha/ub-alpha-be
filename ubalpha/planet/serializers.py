from rest_framework import serializers

from .models import Planet, Detail
from character.serializers import CharacterSerializer

class PlanetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'

class DetailSerializer(serializers.ModelSerializer):
    member = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), 
        required=False
    )
    
    planet_img = serializers.SerializerMethodField()
    max_point = serializers.SerializerMethodField()

    def get_planet_img(self, obj):
        return obj.planet.image
    
    def get_max_point(self, obj):
        return obj.character.max_point

    class Meta:
        model = Detail
        fields = '__all__'
