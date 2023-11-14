from django.urls import path
from . import views

urlpatterns = [
    path("members/", views.members, name = "members"),
    path("sample/", views.sample, name = "sample")
]