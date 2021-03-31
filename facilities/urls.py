from django.urls import path
from . import views

urlpatterns = [
    path('', views.free_weights, name='facilities')
]
