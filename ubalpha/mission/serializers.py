from rest_framework import serializers

from .models import Mission, Log

import datetime

class MissionSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    log_id = serializers.SerializerMethodField()

    def get_status(self, obj):
        log = Log.objects.filter(member=self.context['request'].user, mission=obj.id)
        today = log.filter(member=self.context['request'].user, created_at = datetime.datetime.now().date(), mission=obj.id)
        if len(log) == 0 and obj.category!='welcome':
            return 'notready'
        if len(today) == 0 and obj.category == 'today':
            return 'notready'
        return log[len(log)-1].status
    
    def get_log_id(self, obj):
        log = Log.objects.filter(member=self.context['request'].user, mission=obj.id)
        today = log.filter(member=self.context['request'].user, created_at = datetime.datetime.now().date(), mission=obj.id)
        if (len(log) == 0 and obj.category!='welcome') or len(today) == 0:
            return 0
        if len(today) == 0 and obj.category == 'today':
            return 0
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