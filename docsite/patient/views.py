import math
import random
from datetime import datetime, timedelta, date

# import datetime
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from numpy.core.defchararray import isdigit

from .models import Pat, Schedule


# Create your views here.


def home(request):
    return render(request, 'form.html')


def form(request):
    patients = None
    params = {"patient": None}
    print(patients)

    if 'query' in request.GET:
        query = request.GET['query']
        print("length :", len(query))
        if len(query) == 0:
            error = "Enter a name to search"
            err = {'error': error}
            return render(request, 'index.html', err)
        if len(query) != 0:
            patients = Pat.objects.filter(name__icontains=query)
            print("patients = ", patients)
            print(len(patients))
            params = {"patient": patients[0]}
            return render(request, 'index.html', params)

    if request.method == "POST":
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        phone = request.POST.get('pno').strip()
        symptoms = request.POST.get('symptoms').strip()
        prescription = request.POST.get('prescription').strip()

        error_message = None
        if not prescription:
            error_message = "Enter Prescription"
        if not symptoms:
            error_message = "Enter Symptoms"

        if error_message is None:
            send_mail(
                "Dr. XYZ prescription mail",  # subject
                name + "\n" + phone + "\n" + "Symptoms : " + symptoms + "\n" + "Prescription : " + prescription,
                # message
                'rutuj.bafna19@vit.edu',  # from mail
                [email],  # to mail
            )
            pat = Pat.objects.get(name=name)
            pat.name = name
            pat.email = email
            pat.phone = phone
            pat.symptoms = symptoms
            pat.prescription = prescription
            pat.date = datetime.today()
            pat.save()
            return render(request, 'index.html', params)

        else:
            patient = {'error_message': error_message, 'name': name, 'email': email, 'phone': phone,
                       'symptom': symptoms, 'prescriptions': prescription}
            params = {'patient': patient}
            return render(request, 'index.html', params)
    return render(request, 'index.html')


def formB(request):
    if request.method == "POST":
        name = request.POST.get('name').strip()
        email = request.POST.get('email').strip()
        phone = request.POST.get('pno').strip()
        symptoms = request.POST.get('symptoms').strip()
        prescription = request.POST.get('prescription').strip()

        error_message = None
        if not prescription:
            error_message = "Enter Prescription"
        if not symptoms:
            error_message = "Enter Symptoms"
        if not name:
            error_message = "Enter Name"
        if not email:
            error_message = "Enter Email Address"
        if not phone:
            error_message = "Enter Phone Number"
        if phone:
            if len(phone) != 10:
                error_message = "Enter valid phone number"
            if not isdigit(phone):
                error_message = "Enter valid phone number"
        if email:
            if "@" not in email:
                error_message = "Enter valid email"
        if name:
            patients = Pat.objects.filter(name__icontains=name)
            if patients:
                error_message = "Username already present/ Name already used"

        if error_message is None:
            # Send mail
            send_mail(
                "Dr. XYZ prescription mail",  # subject
                name + "\n" + phone + "\n" + "Symptoms : " + symptoms + "\n" + "Prescription : " + prescription,
                'rutuj.bafna19@vit.edu',  # from mail
                [email],  # to mail
            )

            pat = Pat(name=name, email=email, phone=phone, symptoms=symptoms, prescription=prescription,
                      date=datetime.today())
            pat.save()
            return render(request, 'form_b.html')
        else:
            patient = {'error_message': error_message, 'name': name, 'email': email, 'phone': phone,
                       'symptom': symptoms, 'prescriptions': prescription}
            params = {'patient': patient}
            return render(request, 'form_b.html', params)
    return render(request, 'form_b.html')


def formC(request):
    return render(request, "formc.html")


def generateOTP():
    digits = "0123456789"
    OTP = ""
    for i in range(4):
        OTP += digits[math.floor(random.random() * 10)]
    return OTP


def send_otp(request):
    email = request.GET.get("email")
    print(email)
    o = generateOTP()
    htmlgen = '<p>Your OTP is <strong>o</strong></p>'
    send_mail('OTP request', o, 'rutuj.bafna19@vit.edu', [email], fail_silently=False, html_message=htmlgen)
    return HttpResponse(o)


def appointment(request):
    s = Schedule.objects.first()
    print(s)
    # print(date.today())
    if str(s) != str(date.today()):
        s.delete()
        s1 = Schedule.objects.last()
        s2 = Schedule(date=s1.date + timedelta(1))
        s2.save()
    #  print(s)

    schedule = Schedule.objects.all()
    # for i in schedule:
    # print(i.date)
    j = 0
    params = {"dates": schedule, 'j': j}
    slots = None

    if 'query' in request.GET:
        query = request.GET['query']
        print(query)
        if query is not None:
            slots = Schedule.objects.get(date__icontains=query)
            print("patients = ", slots)
            params = {"dates": schedule, 'j': j, "slots": slots}
            return render(request, 'appointment.html', params)

    if request.method == "POST":
        name = str(request.POST.get('name')).strip()
        email = str(request.POST.get('mail')).strip()
        time = request.POST.get('time')
        data = request.POST.get('date')
        print(name, email, time, data)

        appoint = Schedule.objects.get(date=data)
        if time == 'Slot1':
            appoint.Slot1 = name + "  ,   " + email
        if time == 'Slot2':
            appoint.Slot2 = name + "  ,   " + email
        if time == 'Slot3':
            appoint.Slot3 = name + "  ,   " + email
        if time == 'Slot4':
            appoint.Slot4 = name + "  ,   " + email
        if time == 'Slot5':
            appoint.Slot5 = name + "  ,   " + email
        if time == 'Slot6':
            appoint.Slot6 = name + "  ,   " + email
        if time == 'Slot7':
            appoint.Slot7 = name + "  ,   " + email
        if time == 'Slot8':
            appoint.Slot8 = name + "  ,   " + email
        if time == 'Slot9':
            appoint.Slot9 = name + "  ,   " + email
        if time == 'Slot10':
            appoint.Slot10 = name + "  ,   " + email
        appoint.save()

        send_mail(
            "Dr. XYZ appointment mail",  # subject
            name + "\n" + email + "\n" "Your appointment has been booked for:" + "\n" + "Date: " + data + "\n" +
            "Time: " + time,
            'rutuj.bafna19@vit.edu',  # from mail
            [email],  # to mail
        )

    return render(request, 'appointment.html', params)


def schedule(request):
    s = Schedule.objects.first()
    print(s)
    # print(date.today())
    if str(s) != str(date.today()):
        s.delete()
        s1 = Schedule.objects.last()
        s2 = Schedule(date=s1.date + timedelta(1))
        s2.save()
    scheduler = Schedule.objects.get(date=date.today())
    params = {'scheduler': scheduler}
    return render(request, 'schedule.html', params)
