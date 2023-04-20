from django.urls import path
from django.views.generic import TemplateView

from main_app import views

app_name = 'main_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('kitchen', views.kitchen_form, name='kitchen_form'),
]
urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="bingo/robots.txt", content_type='text/plain')),
]