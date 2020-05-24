from django import forms
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator
import datetime
from .models import Reservation

class DateInput(forms.DateInput):
    input_type = 'date'

class NotesInput(forms.Textarea):
    input_type = 'textarea'

class PartySizeInput(forms.NumberInput):
    input_type='number'

#create form from reservation model
class ReservationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        self.fields['partySize'].validators.append(MinValueValidator(1, 'Party Size must be greater than 0'))
        self.fields['partySize'].validators.append(MaxValueValidator(20, 'Party Size must be less than 20'))
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

    class Meta:
        model = Reservation
        fields = []
        widgets = {
            'date': DateInput(attrs={'min':datetime.date.today(), 'max':datetime.date.today() + datetime.timedelta(365)}),
            'notes': NotesInput(attrs={'style':'max-height:100px'}),
            'partySize': PartySizeInput(attrs={'min':'1', 'max':'20'})
        }

    def clean(self):
        super().clean()
        if self.instance.expired:
            raise forms.ValidationError("This reservation is expired")

class MakeReservationForm(ReservationForm):
    def __init__(self, *args, **kwargs):
        super(MakeReservationForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(EmailValidator())

    class Meta(ReservationForm.Meta):
        fields = ['name', 'email', 'date', 'time', 'partySize', 'notes']
    

class EditReservationForm(ReservationForm):
    def __init__(self, *args, **kwargs):
        super(EditReservationForm, self).__init__(*args, **kwargs)

    class Meta(ReservationForm.Meta):
        fields = ['name', 'date', 'time', 'partySize', 'notes']