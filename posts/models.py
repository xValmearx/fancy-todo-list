from django.db import models


# user name is Caleb_Taylor
# email calebs.phone2017@gmail.com
# password = password


# Create your models here.
class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
