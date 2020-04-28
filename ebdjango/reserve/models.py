from django.db import models
import datetime

# Create your models here.
TIME_ENUM = [
]
for h in range(4, 9):
    for m in [0, 15, 30, 45]:
        t = datetime.time(h+12, m, 0, 0)
        TIME_ENUM.append((t, t.isoformat()))


class Reservation(models.Model):
    name = models.CharField(max_length=128)
    phoneNum = models.CharField(max_length=10)
    email = models.CharField(max_length=128)
    date = models.DateField()
    time = models.TimeField(choices=TIME_ENUM)
    partySize = models.IntegerField()
    notes = models.CharField(max_length=256, blank=True)

    def __str__(self):
        return f"{self.id}: {self.name}, {self.phoneNum}, {self.email}, {self.date}, {self.time}, {self.partySize}, {self.notes}"

    def is_today(self):
        return self.date == datetime.date.today()
