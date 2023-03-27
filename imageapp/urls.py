from django.urls import path
from imageapp.views import strona_image, nowy_image, usun_image

urlpatterns = [
    path('image/', strona_image, name="strona_image"),
    path('nowy/', nowy_image, name="nowy_image"),
    path('usun/<int:id>/', usun_image, name="usun_image")
]