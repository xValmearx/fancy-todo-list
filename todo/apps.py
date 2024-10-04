# Comments at the top of each file that you add source code to with the following:
# Caleb Taylor
# CIS 218
# 10/4/2024

from django.apps import AppConfig


class TodoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "todo"
