from django.shortcuts import render
from . import models


def all_rooms(request):
    page = int(request.GET.get("page", 1))
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    return render(request, "rooms/home.html", {"potato": all_rooms})
