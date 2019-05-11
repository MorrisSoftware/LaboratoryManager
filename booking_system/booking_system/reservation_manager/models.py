import uuid
from website import settings
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class CalenderSetting(models.Model):
    setting_name = models.CharField(max_length=50,help_text="Name of settings group")
    number_of_days = models.IntegerField(default=7,help_text="Number of days to be displayed in view")
    first_session_time = models.TimeField(default="00:00:00", help_text="Time of first session")
    time_interval = models.IntegerField(default=60, help_text="Number of minutes per session")
    number_of_sessions = models.IntegerField(default=24, help_text="Number of sessions per day")
    active = models.BooleanField(default=False,help_text="Set active to use this settings group")

    def __str__(self):
        return self.setting_name


class InstrumentCategory(models.Model):

    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=20, help_text='Type of instrument')

    class Meta:
        ordering = ['category']

    def __str__(self):
        return self.category

class Instrument(models.Model):
    instrument_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    manufacturer = models.CharField(max_length=50,help_text='The instrument manufacturer')
    model = models.CharField(max_length=50,help_text='The instrument model')
    instrument_name = models.CharField(max_length=50, help_text="The name that will be displayed to users")
    year = models.DateField(help_text='The year the instrument was obtained. Format: YYYY-MM-DD')
    location = models.CharField(max_length=50, help_text='Where the instrument can be found')
    image = models.ImageField(upload_to = "instrument",default="img/default.jpg")
    category = models.ForeignKey('InstrumentCategory', on_delete=models.CASCADE)
    under_maintenance = models.BooleanField(default=False)


    def __str__(self):
        return self.instrument_name

class Reservation(models.Model):
    reservation_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id = models.ForeignKey(User,to_field='username', on_delete=models.CASCADE)
    instrument_id = models.ForeignKey('Instrument', on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    time_start = models.TimeField(default="00:00:00")
    time_end = models.TimeField(default="00:00:00")
    
    def __str__(self):
        return str(self.reservation_id)
