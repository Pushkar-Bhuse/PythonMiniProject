from django.shortcuts import render
from .forms import contactForm,ReservationForm
from django.core.mail import send_mail
from django.conf import settings
from reservation.models import Reservation,Branch
from delivery.models import *
# from twilio.rest import Client



def contact(request):
    title = "Contact"
    form = contactForm(request.POST or None)
    confirm_message = None
    if form.is_valid():
        # account_sid = "C7ad1b80e56e62edb18e0e58e298e201c"
        # auth_token  = "10a590b0628afd4908825c2a490bc18c"
        # client = Client(account_sid, auth_token)

        # message = client.messages.create(
        #     body= form.cleaned_data["comment"],
        #     to="+919820598411",
        #     from_="+919167498411",)
        # print(message.sid)

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
        return render(request,'reservation/booking.html',{'form':form, "place":place})



def choose_location(request):
    branches = Branch.objects.all()
    template = 'reservation/chooselocation.html'
    return render(request,template,{"branches":branches})


