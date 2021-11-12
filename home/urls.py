from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("india", views.india, name='india'),
    path("switzerland", views.switzerland, name='switzerland'),
    path("uae", views.uae, name='uae'),
    path("australia", views.australia, name='australia'),
    path("france", views.france, name='france'),
    path("indonesia", views.indonesia, name='indonesia'),
    path('login', views.loginUser, name="login"),
    path('logout', views.logoutUser, name="logout"),
    path("profile", views.profile, name='profile'),
    path("blog", views.blog, name='blog'),
    path("booking", views.booking, name='booking'),
    path("dest", views.dest, name='dest')

]
