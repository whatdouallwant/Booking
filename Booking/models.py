from turtle import mode
from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    room_description = models.TextField(blank=True, null=True)
    TYPE_CHOICES = [
        ('lux', 'Люкс'),
        ('std', 'Стандарт'),
        ('eco', 'Економ')
    ]
    room_type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    amount_of_beds = models.IntegerField(default=1)
    max_guests = models.IntegerField(default=1)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='room_pictures/', blank=True, null=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"
    
    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номери'
        ordering = ['room_number']

class Room_Image(models.Model):
    room_picture = models.ImageField(upload_to='room_pictures/', blank=True, null=True)
    related_room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    

class Bookings(models.Model):
    STATUS_CHOICES = [
        ('wtn', 'Очікує підтвердження'),
        ('cnf', 'Підтверджено'),
        ('clc', 'Скасовано')
    ]
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()
    email = models.EmailField(default='noname@example.com')
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='wtn')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.room.room_number} from {self.check_in_date} to {self.check_out_date} by {self.user.username}"

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['-created_at']