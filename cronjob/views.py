from django.apps import AppConfig
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import Cronjob
from django.contrib import messages


# transfer to startsite
def index(request):
    return render(request, "cronjob/home.html")


# get the informations from the template and save them to the database
# render to the mention site
# logic for the messages (template send ok/nok)
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
            if minute == '':
                messages.error(request, 'Bitte überprüfen Sie Ihre Eingabe')
                return render(request, "cronjob/cronsite.html")
            intervalString = minute + ' * * * *'
        elif choice == 'option2':
            minute = request.POST['option2MinuteInput']
            hour = request.POST['option2HourInput']
            if minute or hour == '':
                messages.error(request, 'Bitte überprüfen Sie Ihre Eingabe')
                return render(request, "cronjob/cronsite.html")
            intervalString = minute + ' ' + hour + ' * * *'
        elif choice == 'option3':
            minute = request.POST['option3MinuteInput']
            hour = request.POST['option3HourInput']
            day = request.POST['option3DayInput']
            if minute or hour or day == '':
                messages.error(request, 'Bitte überprüfen Sie Ihre Eingabe')
                return render(request, "cronjob/cronsite.html")
            intervalString = minute + ' ' + hour + ' ' + day + ' * *'
        elif choice == 'option4':
            customInput = request.POST['userDefinedInput']
            if customInput == '':
                messages.error(request, 'Bitte überprüfen Sie Ihre Eingabe')
                return render(request, "cronjob/cronsite.html")
            intervalString = customInput

        job.interval = intervalString
        job.messageFail = request.POST.get('messageFail', 0)
        job.messageSuccess = request.POST.get('messageSuccess', 0)
        job.messageToManyFailures = request.POST.get('messageTotalyFail', 0)
        job.saveResponse = request.POST.get('saveResponse', 0)

        job.save()

        messages.success(request, 'Ihr Cron-Job wurde erfolgreich gespeichert.')
        return render(request, "cronjob/cronsite.html")

    else:
        return render(request, "cronjob/cronsite.html")


# logic for the restistration, saves the new users
# render to the mention site
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
