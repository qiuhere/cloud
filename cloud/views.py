from django.shortcuts import render
from cloud.model import Image
from cloud.forms import ImageForm


def showimage(request):
    lastimage = Image.objects.last()

    imagefile = lastimage.imagefile

    form = ImageForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    context = {'imagefile': imagefile,
               'form': form
               }

    return render(request, 'Blog/images.html', context)
