from django.db import models
from django.utils import timezone


class Simulation(models.Model):
  attacking_armies_starting = models.IntegerField()
  defending_armies_starting = models.IntegerField()
  attacking_armies_remaining = models.IntegerField()
  defending_armies_remaining = models.IntegerField()
  result_statement = models.CharField(max_length=20)
  timestamp = models.DateTimeField(null=True, blank=True)