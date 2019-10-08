from django.db import models


class Cronjob(models.Model):
    title = models.CharField(max_length=30)
    url = models.CharField(max_length=30)