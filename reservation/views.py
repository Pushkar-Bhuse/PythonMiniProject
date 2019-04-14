from django.shortcuts import render
from .forms import contactForm,ReservationForm
from django.core.mail import send_mail
from django.conf import settings
from reservation.models import Reservation,Branch
from delivery.models import *
from reservation.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from twilio.rest import Client

app_name='reservation'

def index(request):
    template = "reservation/index.html"
    return render(request,template)

def register(request):
    template = "reservation/register.html"
    return render(request,template)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'reservation/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def contact(request):
    title = "Contact"
    form = contactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():

        subject = "Reservation"
        name = form.cleaned_data["name"]
        number = form.cleaned_data["number"]
        date = form.cleaned_data["date"]
        time = form.cleaned_data["time"]
        description = form.cleaned_data["description"]
        emailFrom = [settings.EMAIL_HOST_USER]#form.cleaned_data["email"]
        emailTo = request.user.email#[settings.EMAIL_HOST_USER]


        message = "%s %s" %(comment,name)
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        form = None
        confirm_message = "Thanks for reaching out to us. We will get back to you soon."
        title = "Thanks!"

    context = {"title":title, "confirm_message": confirm_message , "form":form}
    template = "contact.html"
    return render(request,template,context)


# def reservation(request):
#     title = "Contact"
#     form = ReservationForm(request.POST or None)
#     confirm_message = None
#     if form.is_valid():
#         subject = "The PB Store"
#         date = form.cleaned_data["date"]
#         details = form.cleaned_data["details"]
#         time = form.cleaned_data["time"]
#         emailFrom = form.cleaned_data["email"]
#         emailTo = [settings.EMAIL_HOST_USER]
#         message = "%s %s" %(date, time)
#         send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
#         reservation = form.save(commit = False)
#         reservation.user = request.user
#         reservation.place = Branch.objects.get(id = place)
#         reservation.save(commit = True)
#         #form = None
#         confirm_message = "Thanks for reaching out to us. We will get back to you soon."
#         title = "Thanks!"

#     context = {"title":title, "confirm_message": confirm_message}
#     template = 'reservation/confirmation.html'
#     return render(request,template,context)


def choose_and_book(request,place=1):
    # place = request.POST["place"]
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        subject = "The PB Store"
        date = form.cleaned_data["date"]
        details = form.cleaned_data["details"]
        time = form.cleaned_data["time"]
        emailFrom = settings.EMAIL_HOST_USER
        emailTo = [request.user.email]
        message = "%s %s" %(date, time)
        send_mail(subject, message, emailFrom, emailTo, fail_silently=False,)
        reservation = form.save(commit = False)
        reservation.user = request.user
        reservation.place = Branch.objects.get(id = place)
        reservation.save()
        #form = None
        confirm_message = "Thanks for reaching out to us. We will get back to you soon."
        title = "Thanks!"

        context = {"title":title, "confirm_message": confirm_message}
        template = 'reservation/confirmation.html'
        return render(request,template,context)

    else:
        # import pdb; pdb.set_trace()
        form = ReservationForm()
        return render(request,'reservation/bookin2.html',{'form':form, "place":place})



def choose_location(request):
    branches = Branch.objects.all()
    template = 'reservation/chooselocation.html'
    return render(request,template,{"branches":branches})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request,'reservation/register.html',
                          {'user_form':user_form,

                           'registered':registered})

