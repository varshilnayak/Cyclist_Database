from multiprocessing import connection
from pyexpat.errors import messages
from subprocess import CompletedProcess
from urllib import request
from django.shortcuts import render
from cyclist.models import Cyclist
from cyclist.models import Organizer
from cyclist.models import Event
from django.contrib import messages
from cyclist.models import Sponsor
from cyclist.forms import cyclistform
from django.db import connection
from django.http import HttpResponse


def homepage(request):
    return render(request, 'homepage.html')


def showemp(request):
    showall = Cyclist.objects.all()
    print(showall)
    return render(request, 'show_cyclist.html', {"data": showall})


def insert_form(request):

    return render(request, 'insert.html')


def insert_organizer(request):
    return render(request, 'insert_organizer.html')


def insertemp(request):
    print("Inserting")
    saverecord = Cyclist()
    saverecord.cyclist_id = request.POST.get('cyclist_id')
    saverecord.cyclist_name = request.POST.get('cyclist_name')
    saverecord.age = request.POST.get('age')
    saverecord.country = request.POST.get('country')
    saverecord.gender = request.POST.get('gender')
    saverecord.email_id = request.POST.get('email_id')
    allval = Cyclist.objects.all()
    for i in allval:
        if int(i.cyclist_id) == int(request.POST.get('cyclist_id')):
            messages.warning(request, 'cycslist_id already exists....!')
            return render(request, 'insert.html')
    saverecord.save()
    messages.success(request, 'Cyclist ' +
                     saverecord.cyclist_name + ' is saved successfully..! ')
    return render(request, 'insert.html')


def editemp(request, cyclist_id):
    editempobj = Cyclist.objects.get(cyclist_id=cyclist_id)
    return render(request, 'edit.html', {"Cyclist": editempobj})


def updateemp(request, cyclist_id):
    updateemp = Cyclist.objects.get(cyclist_id=cyclist_id)
    cid = request.POST.get("cyclist_id")
    cname = request.POST.get("cyclist_name")
    age = request.POST.get("age")
    country = request.POST.get("country")
    gend = request.POST.get("gender")
    email = request.POST.get("email_id")

    original = Cyclist.objects.get(cyclist_id=cid)

    original.cyclist_name = cname
    original.age = age
    original.country = country
    original.gender = gend
    original.email_id = email
    original.save()
    # form=cyclistform(request.POST,instance=updateemp)
    # if form.is_valid():
    #     form.save()
    messages.success(request, 'record updated succesfully..!')
    return render(request, 'edit.html', {"Cyclist": original})


def delemp(request, cyclist_id):
    delecyclist = Cyclist.objects.get(cyclist_id=cyclist_id)
    delecyclist.delete()
    showall = Cyclist.objects.all()

    return render(request, 'show_cyclist.html', {"data": showall})


def showcyclist(request):
    showall = Cyclist.objects.all()
    print(showall)
    return render(request, 'show_cyclist.html', {"data": showall})


def showorganizer(request):
    showall = Organizer.objects.all()
    print(showall)
    return render(request, 'showorganizer.html', {"data": showall})


def organizer_temp(request):

    return render(request, 'insert_organizer.html')


def insert_organizer(request):
   # if request.method=="POST":
    # if request.POST.get('organizer_id') and request.POST.get('organizer_name') and request.POST.get('contact') and request.POST.get('address'):

    saverecord = Organizer()
    saverecord.organizer_id = request.POST.get('organizer_id')
    saverecord.organizer_name = request.POST.get('organizer_name')
    saverecord.contact = request.POST.get('contact')
    saverecord.address = request.POST.get('address')

    allval = Organizer.objects.all()
    for i in allval:
        if int(i.organizer_id) == int(request.POST.get('organizer_id')):
            messages.warning(request, 'organizer_id already exists....!')
            return render(request, 'insert_organizer.html')
    saverecord.save()
    messages.success(request, 'organizer ' +
                     saverecord.organizer_name + ' is saved successfully..! ')
    return render(request, 'insert_organizer.html')


def organizer_editemp(request, organizer_id):
    editempobj = Organizer.objects.get(organizer_id=organizer_id)
    return render(request, 'organizer_edit.html', {"Organizer": editempobj})


def organizer_updateemp(request, organizer_id):
    updateemp = Organizer.objects.get(organizer_id=organizer_id)
    cid = request.POST.get("organizer_id")
    cname = request.POST.get("organizer_name")
    age = request.POST.get("contact")
    country = request.POST.get("address")

    original = Organizer.objects.get(organizer_id=cid)

    original.organizer_name = cname
    original.contact = age
    original.address = country
    original.save()
    # form=cyclistform(request.POST,instance=updateemp)
    # if form.is_valid():
    #     form.save()
    messages.success(request, 'record updated succesfully..!')
    return render(request, 'organizer_edit.html', {"Organizer": original})


def organizer_delemp(request, organizer_id):
    delecyclist = Organizer.objects.get(organizer_id=organizer_id)
    delecyclist.delete()
    showall = Organizer.objects.all()

    return render(request, 'showorganizer.html', {"data": showall})


def showevent(request):
    showall = Event.objects.all()
    print(showall)
    return render(request, 'showevent.html', {"data": showall})


def event_temp(request):

    return render(request, 'insert_event.html')


def insert_event(request):
    print("Inserting")
    saverecord = Event()
    saverecord.event_id = request.POST.get('event_id')
    saverecord.event_name = request.POST.get('event_name')
    saverecord.event_type = request.POST.get('event_type')
    saverecord.location = request.POST.get('location')
    saverecord.date = request.POST.get('date')
    saverecord.time = request.POST.get('time')
    saverecord.organizer = request.POST.get('organizer_id')

    saverecord.save()
    messages.success(request, 'event ' +
                     saverecord.event_name + ' is saved successfully..! ')
    return render(request, 'insert_event.html')


def showsponsor(request):
    showall = Sponsor.objects.all()
    print(showall)
    return render(request, 'showsponsor.html', {"data": showall})


def event_editemp(request, event_id):
    editempobj = Event.objects.get(event_id=event_id)
    return render(request, 'event_edit.html', {"Event": editempobj})


def event_updateemp(request, event_id):
    updateemp = Event.objects.get(event_id=event_id)
    cid = request.POST.get("event_id")
    cname = request.POST.get("event_name")
    age = request.POST.get("event_type")
    country = request.POST.get("location")
    dat = request.POST.get("date")
    tim = request.POST.get("time")
    org = request.POST.get("organizer_id")

    original = Event.objects.get(event_id=cid)

    original.event_name = cname
    original.event_type = age
    original.location = country
    original.date = dat
    original.time = tim
    original.organizer_id = org

    original.save()
    # form=cyclistform(request.POST,instance=updateemp)
    # if form.is_valid():
    #     form.save()
    messages.success(request, 'record updated succesfully..!')
    return render(request, 'event_edit.html', {"Event": original})


def event_delemp(request, event_id):
    delecyclist = Event.objects.get(event_id=event_id)
    delecyclist.delete()
    showall = Event.objects.all()

    return render(request, 'showevent.html', {"data": showall})


def sortCyclist(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = Cyclist.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'sortcyclist.html', context)
        else:
            return render(request, 'sortcyclist.html')


def sortOrganizer(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = Organizer.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'sortorganizer.html', context)
        else:
            return render(request, 'sortorganizer.html')


def sortevent(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = Event.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'sortevent.html', context)
        else:
            return render(request, 'sortevent.html')


def runQuerycyclist(request):
    raw_query = 'select "Cyclist_name" from public."Cyclist" where "Age" >= 40; '

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'runQuerycyclist.html', {'data': alldata})


def runQuery2(request):
    raw_query = 'SELECT * FROM "Organizer" WHERE "Organizer_id"=(SELECT "Organizer_id" FROM "Event" GROUP BY "Organizer_id" ORDER BY COUNT("Organizer_id")  DESC LIMIT 1);'

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'runquery2.html', {'data': alldata})


def runQuery3(request):
    raw_query = 'SELECT * FROM "Cyclist" P1 NATURAL JOIN "Cyclist_performance" WHERE "Cyclist_id"=(SELECT "Cyclist_id" FROM "Cyclist_performance" GROUP BY "Cyclist_id"  ORDER BY COUNT("Cyclist_id") DESC LIMIT 1);'

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'runquery3.html', {'data': alldata})


def custom_query(request):
    custom_query = request.POST.get("custom_query")
    print(custom_query)
    #raw_query = "select * from \"Organization\" where org_rating=1;"

    cursor = connection.cursor()
    cursor.execute(custom_query)
    alldata = cursor.fetchall()

    return render(request, 'runquery2.html', {'data': alldata})


def run_query(request):

    return render(request, 'search.html', {})
