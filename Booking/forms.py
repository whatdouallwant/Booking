from django import forms
from .models import Bookings

class BookingForm(forms.ModelForm):
    class Meta:
        model = Bookings
        fields = ['check_in_date', 'check_out_date', 'email']
        widgets = {
            'check_in_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'check_out_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'check_in_date': 'Дата заїзду',
            'check_out_date': 'Дата виїзду',
            'email': 'Ваш Email',
        }
