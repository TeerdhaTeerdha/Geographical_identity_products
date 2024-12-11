from django.shortcuts import render
from app1.models import Users
from django.db.models import Q
# Create your views here.
def home(request):
    response=render(request,"app1/index.html")
    return response 
def signup_temp(request):
    response=render(request,"app1/signup_temp.html")
    return response 
def signup(request):
    name=request.GET['name']
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    qs=Users.objects.filter(uname=uname)
    if len(qs)==0:
            user=Users(name=name,uname=uname,password=pwd)
            user.save()
            msg="UserRegistered"
            response=render(request,"app1/signin_temp.html",context={'msg':msg})
            return response
    else:
            msg="User Exists"
    
    response=render(request,"app1/signup_temp.html",context={'msg':msg})
    return response 

def signin_temp(request):
    response=render(request,"app1/signin_temp.html")
    return response

def signin(request):
    uname=request.GET['uname']
    pwd=request.GET['pwd']
    qs=Users.objects.filter(Q(uname=uname) & Q(password=pwd))
    if len(qs)==0:
        msg="Invalid UserName or Password"
        response=render(request,"app1/signin_temp.html",context={'msg':msg})
        return response 
    else:
        response=render(request,"app1/Andhra_food_menu.html",context={'uname':uname})        
        return response 
def changepwd_temp(request):
    response=render(request,"app1/changepwd.html")
    return response
def changepwd(request):
    uname=request.GET['uname']
    opwd=request.GET['opwd']
    npwd=request.GET['npwd']
    c=Users.objects.filter(Q(uname=uname) & Q(password=opwd)).update(password=npwd)
    if c==0:
       msg="Invalid Username or Password" 
       response=render(request,"app1/Andhra_grocery_menu.html",context={'msg':msg})
    else:
        response=render(request,"app1/signin_temp.html")
    return response

def andhra_grocery(request):
    response=render(request,"app1/Andhra_grocery_menu.html")
    return response

def andhra_handloom(request):
    response=render(request,"app1/Andhra_handloom_menu.html")
    return response
    
def andhra_food(request):
    response=render(request,"app1/Andhra_food_menu.html")
    return response
