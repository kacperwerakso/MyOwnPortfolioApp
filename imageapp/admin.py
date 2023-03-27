from django.contrib import admin
from .models import Img


@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ["tytul"]
    list_filter = ("tytul",)
    search_fields = ("tytul",)
