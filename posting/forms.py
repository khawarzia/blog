from django import forms
from .models import *

class pictureform(forms.ModelForm):
    class Meta:
        model = post
        fields = ['picture']