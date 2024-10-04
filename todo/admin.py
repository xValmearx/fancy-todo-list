# Comments at the top of each file that you add source code to with the following:
# Caleb Taylor
# CIS 218
# 10/4/2024

from django.contrib import admin

from .models import Todo

# Register your models here.

admin.site.register(Todo)
