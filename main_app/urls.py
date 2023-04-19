from django.urls import path

from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('kitchen', views.kitchen_form, name='kitchen_form'),
]