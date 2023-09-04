from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import ListView, DetailView

from .models import Room

class RoomsView(View):
    def get(self, request):
        rooms = Room.objects.all()
        return render(request, "rooms/rooms.html", {'rooms': rooms})

class RoomDetailView(DetailView):
    model = Room
    slug_field = "url"