from django.shortcuts import redirect, render, get_object_or_404
from Booking.models import *
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

@login_required
def book_room(request, room_id):
    if request.method == "POST":
        room = Room.objects.get(id=room_id)
        booking = Bookings.objects.create(
            room=room,
            user=request.user if request.user.is_authenticated else None,
            check_in_date=request.POST["check_in_date"],
            check_out_date=request.POST["check_out_date"],
            email=request.POST["email"],
        )
        return render(request, "booking_room/room.html", {
            "room": room,
            "success": "Бронювання пройшло успішно! 🎉"
        })

def home(request):
    rooms = Room.objects.all()

    user_bookings = None
    if request.user.is_authenticated:
        user_bookings = Bookings.objects.filter(user=request.user).select_related("room")

    return render(request, "booking_room/home.html", {
        "rooms": rooms,
        "user_bookings": user_bookings
    })


def room_page(request, pk):

    room = Room.objects.get(pk=pk)
    return render(request, 'booking_room/room.html', {'room': room})
