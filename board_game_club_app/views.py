from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import random

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def login_now(request):
    if not request.POST['email']:
        return redirect('/login')

    errors=Users.objects.validator_login(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/login')
    
    user=Users.objects.get(email=request.POST['email'])
    request.session['user']=user.id
    return redirect('/')

def register(request):
    return render(request, 'register.html')

def register_now(request):
    errors=Users.objects.validator(request.POST)

    if errors:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/register')
    else:
        f=request.POST['first_name']
        l=request.POST['last_name']
        e=request.POST['email']
        p=request.POST['password']
        p_hash= bcrypt.hashpw(p.encode(), bcrypt.gensalt()).decode()
        Users.objects.create(first_name=f, last_name=l, email=e, password=p_hash)

        user=Users.objects.get(email=request.POST['email'])
        request.session['user']=user.id
    return redirect('/')

def logout(request):
    request.session['user']=None
    return redirect('/')

def events(request):
    context={
        "all_events": Events.objects.all(),
        "user": Users.objects.get(id=request.session['user']),
    }
    return render(request, 'events.html', context)

def create_event(request):
    if 'user' not in request.session or request.session['user'] == None:
        return redirect('/login')
    
    user=Users.objects.get(id=request.session['user'])
    n=request.POST['name']
    d=request.POST['date']
    l=request.POST['location']
    desc=request.POST['desc']
    Events.objects.create(name=n, date=d, location=l, desc=desc, created_by=user)
    return redirect('/events')

def join_event(request, id):
    user=Users.objects.get(id=request.session['user'])
    event=Events.objects.get(id=id)
    user.events_joined.add(event)
    user.save()
    return redirect('/events')

def leave_event(request, id):
    user=Users.objects.get(id=request.session['user'])
    event=Events.objects.get(id=id)
    user.events_joined.remove(event)
    user.save()
    return redirect('/events')

def werewolf(request):
    context={
        "all_characters": Werewolf_Characters.objects.all(),
    }
    return render(request, 'werewolf.html', context)

def avalon(request):
    context={
        "all_characters": Avalon_Characters.objects.all(),
    }
    return render(request, 'avalon.html', context)

def tools(request):
    if request.method == "GET":
        context = {
            'players': Players.objects.all().order_by("order_number")
        }
        return render(request, 'tools.html', context)
    if request.method == "POST":
        t = Players.objects.create(name=request.POST['name'])
        t.order_number = t.id
        t.save()
        return redirect("/tools")

def remove_player(request, id):
    Players.objects.get(id=id).delete()
    return redirect("/tools")

def shuffle(request):
    everybody = Players.objects.all()
    myList = []
    for i in everybody:
        myList.append(i)
    random.shuffle(myList)
    for i in range(len(myList)):
        myList[i].order_number = i+1
        myList[i].save()
    return redirect("/tools")

def cancel(request):
    return redirect('/')