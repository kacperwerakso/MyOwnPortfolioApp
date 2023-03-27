from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class Img(models.Model):
    tytul = models.CharField(max_length=20, blank=False, unique=False)
    opis = models.TextField(max_length= 100, default="", null=True, blank=True)
    photo = models.ImageField(upload_to="photos", null=True, blank=False)


    def __str__(self):
        return self.tytul_autor()

    def tytul_autor(self):
        return "{} ({})".format(self.tytul)

        