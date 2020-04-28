from django import forms
from .models import Reservation, TIME_ENUM


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'
        widgets = {
            'time': forms.Select(choices=TIME_ENUM)
        }
