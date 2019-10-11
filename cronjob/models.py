from django.db import models


class Cronjob(models.Model):
    # title, adress
    title = models.CharField(max_length=255, null=True, default='')
    url = models.URLField(max_length=255, null=True, default='')

    # login
    userName = models.CharField(max_length=255, null=False, default='')
    password = models.CharField(max_length=255, null=False, default='')

    # set time and date for interval
    interval = models.CharField(max_length=255, null=True, default='default')

    # messages
    messageFail = models.BooleanField(default=False)
    messageSuccess = models.BooleanField(default=False)
    messageToManyFailures = models.BooleanField(default=False)

    # save response
    saveResponse = models.BooleanField(default=False)

    # show title, url and user in admin-login
    def __str__(self):
        return f"{self.title}, {self.url}, {self.userName}"
