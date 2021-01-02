from django import forms
from cloud.model import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
