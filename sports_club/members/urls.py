from django.urls import path
from . import views

app_name = "members"

urlpatterns = [
    path("", views.main, name = "main"),
    path("members/", views.members, name = "members"),
    path("members/details/<int:id>", views.details, name = "details"),
    path("test/", views.test, name = "test"),
    path("members/create", views.create_member.as_view(), name = "create_member"),
    path("members/update/<int:pk>", views.update_member.as_view(), name = "update_member")
]