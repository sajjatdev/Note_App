

from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from note.views import NoteViewSet
route=DefaultRouter()
route.register("note",NoteViewSet,basename="note")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(route.urls))
]
