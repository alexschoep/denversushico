from django.db import models
import datetime
from django.core.validators import EmailValidator
from random import choice
from string import ascii_letters

#Create list of possible reservation times
TIME_ENUM = [
]
for h in range(4, 9):
    for m in [0, 15, 30, 45]:
        t = datetime.time(h+12, m, 0, 0)
        TIME_ENUM.append((t, t.isoformat()))

# Create your models here.
class Reservation(models.Model):
    url = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    date = models.DateField()
    time = models.TimeField(choices=TIME_ENUM)
    partySize = models.IntegerField()
    notes = models.CharField(max_length=256, blank=True)

    def __init__(self, *args, **kwargs):
        super(Reservation, self).__init__(*args, **kwargs)
        self.url = ''.join(choice(ascii_letters) for i in range(24))

    def __str__(self):
        return f"{self.url}: {self.name}, {self.email}, {self.date}, {self.time}, {self.partySize}, {self.notes}"

    #return whether reservation date is today
    def is_today(self):
        return self.date == datetime.date.today()
