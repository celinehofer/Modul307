# Generated by Django 2.2.6 on 2019-10-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cronjob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('url', models.TextField(max_length=256)),
                ('userName', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=30)),
                ('timeIntervalMinutes', models.TimeField(default='')),
                ('timeIntervalTime', models.TimeField(default='')),
                ('timeIntervalDay', models.TimeField(default='')),
                ('timeIntervalDayTime', models.TimeField(default='')),
                ('userDefined', models.BooleanField(default='')),
                ('messageFail', models.BooleanField(default='')),
                ('messageSuccess', models.BooleanField(default='')),
                ('messageToManyFailures', models.BooleanField(default='')),
                ('saveResponse', models.BooleanField(default='')),
            ],
        ),
    ]
