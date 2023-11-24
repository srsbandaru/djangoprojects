from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name = "members"),
    path("sample/", views.sample, name = "sample"),
    path("worksheet13/", views.worksheet13, name = "worksheet13"),
    path("members/details/<int:id>", views.details, name = "details")
]