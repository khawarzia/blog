from django import forms
from .models import *

class profilepicform(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_pic']