# Comments at the top of each file that you add source code to with the following:
# Caleb Taylor
# CIS 218
# 10/4/2024

from django.views.generic import ListView

from .models import Todo


class TodoListView(ListView):
    model = Todo

    template_name = "home.html"
