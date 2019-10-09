from django.db import models


class Cronjob(models.Model):
    #title, adress
    title = models.CharField(max_length=30)
    url = models.TextField(max_length=256)

    #login
    userName = models.CharField(max_length=30, null=False, default='')
    password = models.CharField(max_length=30, null=False, default='')

    #set time and date for interval
    timeIntervalMinutes = models.TimeField(default='')
    timeIntervalTime = models.TimeField(default='')
    timeIntervalDay = models.TimeField(default='')
    timeInvervalDayTime = models.TimeField(default='')
    userDefined = models.BooleanField(default='')

    #messages
    messageFail = models.BooleanField(default='')
    messageSuccess = models.BooleanField(default='')
    messageToManyFailures = models.BooleanField(default='')

    #save response
    saveResponse = models.BooleanField(default='')
