from django.shortcuts import render
from django.http import HttpResponse
from .models import Cronjob


def index(request):
    if request.method == 'POST':
        job = Cronjob()
        job.title = request.POST.get("title")
        job.url = request.POST.get("url")
        job.userName = request.POST['userName']
        job.password = request.POST["password"]
        intervalString = ''

        choice = request.POST['timeInterval']
        if choice == 'option1':
            minute = request.POST['option1MinuteInput']
            intervalString = minute + ' * * * *'
        elif choice == 'option2':
            minute = request.POST['option2MinuteInput']
            hour = request.POST['option2HourInput']
            intervalString = minute + ' ' + hour + ' * * *'
        elif choice == 'option3':
            minute = request.POST['option3MinuteInput']
            hour = request.POST['option3HourInput']
            day = request.POST['option3DayInput']
            intervalString = minute + ' ' + hour + ' ' + day + ' * *'
        elif choice == 'option4':
            customInput = request.POST['userDefinedInput']
            intervalString = customInput

        job.interval = intervalString
        job.messageFail = request.POST.get('messageFail', 0)
        job.messageSuccess = request.POST.get('messageSuccess', 0)
        job.messageToManyFailures = request.POST.get('messageTotalyFail', 0)
        job.saveResponse = request.POST.get('saveResponse', 0)

        job.save()

        return render(request, "cronjob/base.html")
    else:
        return render(request, "cronjob/base.html")
