from django.db import models
from core.models import BaseModel
from django.utils import timezone
from datetime import time
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Room(BaseModel):
    room_name = models.CharField(max_length=10, default='room')
    room_no = models.IntegerField()
    floor = models.IntegerField()

    def __str__(self):
        return self.room_name



# class Meeting(BaseModel):
#     team_name = models.CharField(max_length=250)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
#     start_time = models.DateTimeField(default=timezone.make_aware(timezone.now()))
#     end_time = models.DateTimeField()

#     def __str__(self):
#         return self.team_name + " " + str(self.room) + ' ' + str(self.start_time) + "-" + str(self.end_time)

#     def clean(self):
#         if self.start_time.date() != self.end_time.date():
#             raise ValidationError("End time must be on the same day as the start time.")
#         if self.end_time.time() >= self.start_time.time() :
#             raise ValidationError("Start time and end time cannot be same or End time must be higher than start time")
#         if self.end_time.time() < timezone.time(9, 0) or self.end_time.time() > timezone.time(18, 0):
#             raise ValidationError("End time must be between 9:00 AM and 6:00 PM.")


#     class Meta:
#         constraints = [
#             models.UniqueConstraint(
#                 fields=['room', 'start_time'],
#                 name='unique_booking'
#             )
#         ]



class Meeting(models.Model):
    team_name = models.CharField(max_length=250)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='room')
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField()

    def __str__(self):
        return self.team_name + " " + str(self.room) + ' ' + str(self.start_time) + "-" + str(self.end_time)
    
    def clean (self):
        start_time = self.start_time.time()
        end_time = self.end_time.time()
        if start_time < time(9,0) or end_time < time(9,0) or end_time > time(18,0) or end_time <= start_time:
            raise ValidationError("time bounds are wrong")

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['room', 'start_time'],
                name='unique_booking'
            )
        ]
    
# """ "%Y-%m-%d %H:%M" """