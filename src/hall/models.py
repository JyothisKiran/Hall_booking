from django.db import models
from core.models import BaseModel
from datetime import time,date
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Room(BaseModel):
    room_name = models.CharField(max_length=10, default='room')
    room_no = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return self.room_name


class Meeting(BaseModel):
    team_name = models.CharField(max_length=250)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    date = models.DateField(default=date.today )
    start_time = models.TimeField(default=time(9,0))
    end_time = models.TimeField(validators=[MinValueValidator(time(9,0)), MaxValueValidator(time(18,0))])

    def __str__(self):
        return (self.team_name + " " + str(self.room)+' ' + str(self.start_time) + "-" + str(self.end_time))