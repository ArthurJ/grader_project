from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Organizer(User):
    class Meta:
        proxy = True


class Grade(models.Model):
    organizer = models.ForeignKey(Organizer)
    nome = models.CharField(max_length=200)


class Schedule(models.Model):
    grade = models.ForeignKey(Grade)


class Activity(models.Model):
    schedule = models.ForeignKey(Schedule)


class Agent(models.Model):
    organizer = models.ForeignKey(Organizer)


class AgentActivityPreference(models.Model):
    agent = models.ForeignKey(Agent)
    activity = models.ForeignKey(Activity)

    validators = [MinValueValidator(0), MaxValueValidator(10)]
    preference = models.FloatField(validators=validators)
