from math import trunc

from rest_framework import serializers
from .models import *


class UserProfileSerializer(serializers.ModelSerializer):
    completed = serializers.SerializerMethodField(read_only=True)
    percent = serializers.SerializerMethodField(read_only=True)
    count = serializers.SerializerMethodField(read_only=True)
    user = serializers.CharField(source='user.username')

    class Meta:
        model = UserProfile
        fields = ('user', 'name', 'surname', 'photo', 'completed', 'count', 'percent')

    def get_completed(self, obj):
        return obj.number_completed()

    def get_count(self, obj):
        return obj.all_activity()

    def get_percent(self, obj):
        if obj.all_activity() == 0:
            return "0%"
        return str(round((obj.number_completed() / obj.all_activity()) * 100, 2)) + "%"


class CurrentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='current_detail')
    during_time = serializers.SerializerMethodField(read_only=True)
    subtitles = serializers.SerializerMethodField(read_only=True)

    def validate(self, data):
        if data['end'] < data['start']:
            raise serializers.ValidationError("Неправильная установка даты")
        return data

    class Meta:
        model = Current
        fields = ('pk', 'url', 'title', 'parent', 'subtitles', 'is_completed', 'start', 'end', 'during_time',)

    def get_during_time(self, obj):
        return obj.time_during()

    def get_subtitles(self, obj):
        return obj.subtitles()


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'
