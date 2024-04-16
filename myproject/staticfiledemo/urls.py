from django.urls import path
from staticfiledemo import views

urlpatterns = [
    path("", views.index, name="index")
]