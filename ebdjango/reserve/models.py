from django.db import models
import datetime
from django.core.validators import EmailValidator
from random import choice
from string import ascii_letters

#Create list of possible reservation times
TIME_CHOICES = []
for h in range(11, 23):
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

# Create your models here.
class Reservation(models.Model):
    url = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date = models.DateField()
    time = models.TimeField(choices=TIME_CHOICES)
    partySize = models.IntegerField()
    notes = models.CharField(max_length=256, blank=True)
    expired = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(Reservation, self).__init__(*args, **kwargs)
        if not self.url:
            self.url = ''.join(choice(ascii_letters) for i in range(24))
        if not self.expired and self.date:
            self.is_expired()

    def __str__(self):
        return f"{self.url}: {self.name}, {self.email}, {self.date}, {self.time}, {self.partySize}, {self.notes}, {self.expired}"

    def is_expired(self):
        now = datetime.datetime.now()
        if self.date < now.date():
            self.expired = True
        elif self.date == now.date() and self.time < now.time():
            self.expired = True
