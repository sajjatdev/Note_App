from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .API import NoteSerializer
from .models import Note
# Create your views here.


class NoteViewSet(ModelViewSet):
               queryset=Note.objects.all()
               serializer_class=NoteSerializer
