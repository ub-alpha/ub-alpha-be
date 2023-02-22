from rest_framework import serializers

from .models import Mission, Log

import datetime

class MissionSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    log_id = serializers.SerializerMethodField()

    def get_status(self, obj):
        log = Log.objects.filter(member=self.context['request'].user, mission=obj.id)
        if len(log) == 0:
            return 'notready'
        if obj.category == 'welcome':
            return log[0].status
        if log[len(log)-1].created_at != datetime.datetime.now().date():
            return 'notready'
        return 'ready'
    
    def get_log_id(self, obj):
        log = Log.objects.filter(member=self.context['request'].user, mission=obj.id)
        if len(log) == 0:
            return 0
        if obj.category == 'welcome':
            return log[0].id
        return log[len(log)-1].id

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