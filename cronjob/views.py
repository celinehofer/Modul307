from django.shortcuts import render, redirect
from cronjob.models import Cronjob

# def index(request):
# return render(request, 'cronjob/base.html', {})


def index(request):
    if request.method == "POST":
        Cronjob.objects.create(

            title=request.POST.get("title"),
            url=request.POST.get("url"),

            userName=request.POST.get("userName"),
            password=request.POST.get("password"),

            timeIntervalMinutes=request.POST.get("timeIntervalMinutes"),
            timeIntervalTime=request.POST.get("timeIntervalTime"),
            timeIntervalDay=request.POST.get("timeIntervalDay"),
            timeInvervalDayTime=request.POST.get("timeIntervalDayTime"),
            userDefined=request.POST.get("userDefined"),

            messageFail=request.POST.get("title"),
            messageSuccess=request.POST.get("title"),
            messageToManyFailures=request.POST.get("title"),

            saveResponse=request.POST.get("title"),
        )

        return render(request, 'cronjob/base.html', {}),
    else:
        return render(request, 'cronjob/base.html', {})

