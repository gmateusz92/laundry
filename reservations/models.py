from django.db import models
from django.contrib.auth.models import User

class WashingMachine(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    washing_machine = models.ForeignKey(WashingMachine, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.user} - {self.washing_machine} - {self.date} {self.start_time}-{self.end_time}"

