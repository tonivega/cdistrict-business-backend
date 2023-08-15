from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'friendly_name', 'salary', 'club']


class ManagerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'friendly_name', 'salary', 'club']


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Club
        fields = ['id', 'friendly_name', 'budget']
