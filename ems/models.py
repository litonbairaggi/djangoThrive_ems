from django.db import models
# from django.utils.timezone import now

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=120, unique=True, blank=False)

    def __str__(self):
        return self.name