
from django.urls import path
from . import views



urlpatterns = [
    path('', views.hotel, name='hotel'),
    path('/', views.hotel),
    path('house_big', views.house_big, name='house_big'),
    path('house_small', views.house_small, name='house_small'),
    path('intertaiment', views.intertaiment, name='intertaiment'),
    path('about_us', views.about_us, name='about_us'),
    path('contact', views.contact, name='contact'),


]
