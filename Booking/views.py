from django.shortcuts import render
from Booking.models import Room, Bookings

def home(request):
    rooms = Room.objects.all()
    return render(request, 'booking_room/home.html', context={'rooms': rooms})

