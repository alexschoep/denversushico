from django.db import models
import datetime
from django.core.validators import EmailValidator
from random import choice
from string import ascii_letters

#Create list of possible reservation times
TIME_CHOICES = []
for h in range(11, 22):
    for m in [0, 30]:
        t = datetime.time(h, m, 0, 0)
        if m == 0:
            m_s = '00'
        elif m == 30:
            m_s = '30'
        if h < 12:
            p_s = 'am'
            h_s = str(h)
        elif h == 12:
            p_s = 'pm'
            h_s = str(h)
        else:
            p_s = 'pm'
            h_s = str(h - 12)
        s = h_s + ':' + m_s + p_s
        TIME_CHOICES.append((t, s))


def is_expired(date, time):
    now = datetime.datetime.now()
    if date < now.date():
        return True
    elif date == now.date() and time < now.time():
        return True
    else:
        return False


# Create your models here.
class Reservation(models.Model):
    url = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date = models.DateField(default=datetime.datetime.now().date())
    time = models.TimeField(choices=TIME_CHOICES, default=TIME_CHOICES[0][0])
    partySize = models.IntegerField(default=1)
    notes = models.CharField(max_length=256, blank=True)
    expired = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Reservation, self).__init__(*args, **kwargs)
        if not self.url:
            self.url = ''.join(choice(ascii_letters) for i in range(24))
        elif not self.expired:
            self.is_expired()

    def __str__(self):
        return f"{self.url}: {self.name}, {self.email}, {self.date}, {self.time}, {self.partySize}, {self.notes}, {self.expired}"

    def is_expired(self):
        if is_expired(self.date, self.time):
            self.expired = True