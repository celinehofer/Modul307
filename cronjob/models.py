from django.db import models
from django.conf import settings
from django.utils import timezone


class Cronjob(models.Model):
    #title, adress
    title = models.CharField(max_length=255, null=False, default='')
    url = models.CharField(max_length=255, null=False, default='')

    #login
    userName = models.CharField(max_length=255, null=False, default='')
    password = models.CharField(max_length=255, null=False, default='')

    #set time and date for interval
    interval = models.CharField(max_length=255, null=False, default='default')
    # timeIntervalMinutes = models.CharField(max_length=30, null=True, default='')
    # timeIntervalTime = models.CharField(max_length=30, null=True, default='')
    # timeIntervalDay = models.CharField(max_length=30, null=True, default='')
    # timeIntervalDayTime = models.CharField(max_length=30, null=True, default='')
    # userDefined = models.BooleanField(default=False)

    #messages
    messageFail = models.BooleanField(default=False)
    messageSuccess = models.BooleanField(default=False)
    messageToManyFailures = models.BooleanField(default=False)

    #save response
    saveResponse = models.BooleanField(default=False)