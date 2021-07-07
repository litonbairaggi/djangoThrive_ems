from django.db import models
from django.db.models.fields import CharField
from django.utils.timezone import now

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=120, unique=True, blank=False)
    def __str__(self):
        return self.team_name

class Designation(models.Model):
    designation_name = models.CharField(max_length=120, unique=True, blank=False)
    created_date = models.DateTimeField(default=now)
    def __str__(self):
        return self.designation_name
