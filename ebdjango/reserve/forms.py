from django import forms
from .models import Reservation, TIME_ENUM
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class NotesInput(forms.Textarea):
    input_type = 'textarea'

#create form from reservation model
class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(EmailValidator())
        self.fields['partySize'].validators.append(MinValueValidator(1, 'Party Size must be greater than 0'))
        self.fields['partySize'].validators.append(MaxValueValidator(20, 'Party Size must be less than 20'))
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Reservation
        fields = ['name', 'email', 'date', 'time', 'partySize', 'notes']
        #use dropdown box widget for time
        widgets = {
            'date': DateInput(attrs={'min':datetime.date.today(), 'max':datetime.date.today() + datetime.timedelta(365)}),
            'time': TimeInput(attrs={'min':'12:30', 'max':'22:00', 'step':'1800'}),
            'notes': NotesInput(attrs={'style':'max-height:100px'})
        }