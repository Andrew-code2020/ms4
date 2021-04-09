from django.urls import path
from . import views

# url path for home app 
urlpatterns = [
    path('', views.index, name='home')
]
