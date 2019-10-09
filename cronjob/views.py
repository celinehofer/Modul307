from django.shortcuts import render
from django.http import HttpResponse
from .models import Cronjob


def index(request):
    if request.method == 'POST':
            cronjob = Cronjob()
            cronjob.title = request.POST.get("title")
            cronjob.url = request.POST.get("url")
            cronjob.userName = request.POST.get("userName")
            cronjob.password = request.POST.get("password")
            cronjob.saveResponse = request.POST.get("response1")
            cronjob.save()

            return render(request, "cronjob/base.html")
    else:
        return render(request, "cronjob/base.html")






# title=request.POST.get("title"),
    # url = request.POST.get("url"),
    #
    # userName = request.POST.get("userName"),
    # password = request.POST.get("password"),
    #
    # timeIntervalMinutes = request.POST.get("message"),
    # timeIntervalTime = request.POST.get("message"),
    # timeIntervalDay = request.POST.get("message"),
    # timeIntervalDayTime = request.POST.get("message"),
    # userDefined = request.POST.get("message"),
    #
    # messageFail = request.POST.get("title"),
    # messageSuccess = request.POST.get("title"),
    # messageToManyFailures = request.POST.get("title"),
    #
    # saveResponse = request.POST.get("title")

