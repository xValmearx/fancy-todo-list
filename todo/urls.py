# Comments at the top of each file that you add source code to with the following:
# Caleb Taylor
# CIS 218
# 10/4/2024
from django.urls import path
from .views import TodoListView

urlpatterns = [
    path("", TodoListView.as_view(), name="home"),
]
