from . import views
from django.urls import path

app_name = 'job'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact',views.contact,name='contact'),
    path('thank',views.thank,name='thank')
]