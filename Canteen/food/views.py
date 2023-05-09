from django.shortcuts import  render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from .models import * 
from django.contrib.auth.models import User

                             
def Home(request):
    return render(request,"Home.html")   
def contactus(request):
    return render(request,"contactus.html")
def signup(request):
    if request.method=="POST":
        Obj = Signup()
        Name = request.POST["Username"]
        Obj.username = Name
        password = request.POST["Password"]
        Obj.password = password
        user = User.objects.create_user(username=Name,password=password)
        user.save()
        Obj.save()
        print(Name)
        print(password)
        return render(request,"foodmenu.html",{"name":Name})
    else:
        return render(request,"signup.html")
def login(request):
        return render(request,"login.html")   

 

def foodmenu(request):
    return render(request,"foodmenu.html")

def breakfast(request):
    breakfasts= Breakfast.objects.all()
    context ={'breakfasts' : breakfasts}
    print(breakfasts)
    return render(request,"breakfast.html",context)

def chatitems(request):
    chatitems= ChatItems.objects.all()
    context ={'chatitems' : chatitems}
    print(chatitems)
    return render(request,"chatitems.html",context)

def combo(request):
    return render(request,"combo.html")

def dailyspecial(request):
    return render(request,"dailyspecial.html")

def fastfood(request):
    fastfoods= FastFood.objects.all()
    context={'fastfoods' : fastfoods}
    print(fastfoods)
    return render(request,"fastfood.html", context)

def freshjuice(request):
    freshjuices= FreshJuice.objects.all()
    context ={'freshjuices' : freshjuices}
    print(freshjuices)
    return render(request,"freshjuice.html",context)

def lunch(request):
    lunches= Lunch.objects.all()
    context ={'lunches' : lunches}
    print(lunches)
    return render(request,"lunch.html",context)



