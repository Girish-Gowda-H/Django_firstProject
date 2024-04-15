from django.urls import path
from first_App import views

urlpatterns = [
    path("", views.home, name="home"),
]