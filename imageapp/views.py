from django.shortcuts import render, get_object_or_404, redirect
from .models import Img
from .forms import ImgsForm
from django.contrib.auth.decorators import login_required

def strona_image(request):
    wszystkie = Img.objects.all()
    return render(request, 'image.html', {'images': wszystkie})

@login_required
def nowy_image(request):
    form = ImgsForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()

    return render(request, 'nowy_image.html', {'form': form})
    
@login_required
def usun_image(request, id):
    image = get_object_or_404(Img, pk=id)
    if request.method == "POST":
        image.delete()
        return redirect(strona_image)

    return render(request, 'usun.html', {'form': image})

