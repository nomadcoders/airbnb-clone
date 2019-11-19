from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [path("add/<int:room_pk>", views.save_room, name="save-room")]
