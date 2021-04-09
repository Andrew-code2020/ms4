from django.urls import path
from . import views


#url path for facilities app

urlpatterns = [
    path('', views.free_weights, name='facilities')
]
