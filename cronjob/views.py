from django.apps import AppConfig
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Cronjob


def index(request):
    return render(request, "cronjob/home.html")


@login_required()
def cronjobs(request):
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

        printOK = "gut"
        if job.id:
            printOK = "Ihr Cron-Job wurde erfolgreich gespeichert."

        return render(request, "cronjob/cronsite.html", {"message": printOK})

    else:
        printNOK = "Ihr Cron-Job konnte nicht gespeichert werden."
        return render(request, "cronjob/cronsite.html", {"message2": printNOK})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registration.html', {'form': form})
