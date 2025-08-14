
from django import views
from django.urls import path
from Booking.views import home, room_page

urlpatterns = [
    path('', home, name='home'),
    path('room/<int:pk>/', room_page, name='room_page'),

]