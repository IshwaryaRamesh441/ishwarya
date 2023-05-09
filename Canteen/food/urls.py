from django.urls import path, include
from food.views import *

from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    path('',foodmenu, name="home"),
    path('contactus',contactus, name="contactus"),
    path('signup', signup, name="signup"),
    path('foodmenu', foodmenu, name="foodmenu"),
    path('breakfast', breakfast, name="breakfast"),
    path('chatitems', chatitems, name="chatitems"),
    path('combo', combo, name="combo"),
    path('dailyspecial', dailyspecial, name="dailyspecial"),
    path('fastfood', fastfood, name="fastfood"),
    path('freshjuice', freshjuice, name="freshjuice"),
    path('lunch', lunch, name="lunch"),
    path('login',login,name="login"),
]

urlpatterns= urlpatterns+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)