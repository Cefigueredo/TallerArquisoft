from django.db import models
from measurements.models import Measurement


class Alarm(models.Model):
    measurement = models.ManyToManyField(Measurement)

    def __str__(self):
        return '{}'.format(self.name)
# Create your models here.
