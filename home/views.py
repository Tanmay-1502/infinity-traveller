from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
# Create your views here.
def index(request):
    return render(request, 'index.html')
   # return HttpResponse("this is homepage")
def india(request):
    return render(request, 'india.html')
def france(request):
    return render(request, 'france.html')  
def australia(request):
    return render(request, 'australia.html')
def switzerland(request):
    return render(request, 'switzerland.html')
def indonesia(request):
    return render(request, 'indonesia.html') 
def uae(request):
    return render(request, 'uae.html') 
def about(request):
    return render(request, 'about.html')
   # return HttpResponse("this is about page")
def booking(request):
    return render(request, 'booking.html')
def dest(request):
    return render(request, 'dest.html')
def blog(request):
    return render(request, 'blog.html')

def services(request):
    return render(request, 'services.html')
  #  return HttpResponse("this is services page")
    
def contact(request):
    if request.method == "POST":
      name= request.POST.get('name')
      email= request.POST.get('email')
      phone= request.POST.get('phone')
      desc= request.POST.get('desc')
      contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
      contact.save()
      messages.success(request, 'Your message has been sent!')

    return render(request, 'contact.html')

def profile(request):
    print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'profile.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/profile")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")
  