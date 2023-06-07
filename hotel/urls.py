from django.urls import path

from . import views

urlpatterns = [
    path("", views.RoomsView.as_view(), name='home'), 
    path("<slug:slug>/", views.RoomDetailView.as_view(), name="room_detail"),
]
