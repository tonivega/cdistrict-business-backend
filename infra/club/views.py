from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from django.utils.translation import gettext_lazy as ugettext_lazy
from django_ufilter.integrations.drf import DRFFilterBackend as DjangoFilterBackend


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all().order_by('-friendly_name')
    serializer_class = ClubSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['friendly_name']


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('-friendly_name')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['friendly_name']


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all().order_by('-friendly_name')
    serializer_class = ManagerSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['friendly_name']
