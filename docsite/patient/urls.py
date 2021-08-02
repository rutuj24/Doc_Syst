from django.urls import path, include
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('formB', views.formB, name='formB'),
    path('formC', views.formC, name='formC'),
    path('appointment', views.appointment, name='appointment'),
    path('schedule', views.schedule, name='schedule'),
]
