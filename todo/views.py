from django.shortcuts import render
from rest_framework import viewsets
from . import serializers, models

# CRUD support
class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = serializers.TodoSerializer