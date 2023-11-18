from django.urls import path
from Calculator import views


urlpatterns = [
    path(route='',view=views.Home,name="Home"),
]
