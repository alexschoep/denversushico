from django import forms
from .models import Reservation, TIME_ENUM
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
import datetime

#create form from reservation model
class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(EmailValidator())
        self.fields['partySize'].validators.append(MinValueValidator(1, 'Party Sizes must be greater than 0'))
        self.fields['partySize'].validators.append(MaxValueValidator(20, 'Party Sizes must be less than 20'))

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'partySize', 'notes']
        #use dropdown box widget for time
        widgets = {
            'time': forms.Select(choices=TIME_ENUM)
        }

    def clean_date(self):
        data = self.cleaned_data.get('date')
        if data < datetime.date.today():
            raise forms.ValidationError('Date cannot be before today')
        if data > datetime.date.today() + datetime.timedelta(365):
            raise forms.ValidationError('Reservations cannot be made more than a year out')
        return data