from django.contrib import admin

from Booking.models import Room, Bookings, Room_Image

admin.site.register(Room)
admin.site.register(Bookings)
admin.site.register(Room_Image)