
from django import views
from django.urls import path
from Booking.views import home, room_page, book_room

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:pk>/', room_page, name='room_page'),
    path('room/<int:room_id>/book/', book_room, name='book_room'),

]