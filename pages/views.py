from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
import csv
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
import datetime
from django.db.models import Q
import string
import random

# Create your views here.
def home(request):
    context = {}
    return render(request, 'pages/home.html', context=context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('login')

def register_users(request):
    response = HttpResponse()
    response['Content-Disposition'] = f'attachment; filename=emp_password_{datetime.datetime.now()}.csv'
    writer = csv.writer(response)
    header = ['EMP ID', 'PASSWORD']
    writer.writerow(header)
    with open('faculty_list.csv') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            username = row[0]
            name = row[1]
            category = row[2]

            user = User()
            random_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))

            user.username = username
            user.set_password(random_password)

            user.save()

            uc = UserCategory()
            uc.user = user
            uc.category = int(category)

            uc.save()

            writer.writerow([user.username, random_password])
    return response

def vacation_form(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == "POST":
        cat = UserCategory.objects.get(user=request.user).category
        slots = VacationSlot.objects.all()    

        select_slot = request.POST['slot']

        user_vacation = UserVacation()    
        user_vacation.user = request.user
        user_vacation.slots = select_slot

        user_vacation.save()
        return redirect('thanks_page')

    cat = UserCategory.objects.get(user=request.user).category
    slots = VacationSlot.objects.all()
    if cat == 1:
        ss = slots.filter(slot_type=1)
        info = ''
        context = {'slots': ss}
        return render(request, 'pages/vacation_form1.html', context=context)
    elif cat == 2:
        ss = slots.filter(slot_type=2)
        context = {'slots': ss}
        return render(request, 'pages/vacation_form2.html', context=context)
    elif cat == 3:
        ss = slots.filter(slot_type=1)
        context = {'slots': ss}
        return render(request, 'pages/vacation_form3.html', context=context)
    elif cat == 4:
        context = {}
        return render(request, 'pages/vacation_form4.html', context=context)

    context = {}
    return render(request, 'pages/vacation_form.html', context=context)

def thanks_page(request):
    context = {}
    return render(request, 'pages/thanks_page.html', context=context)