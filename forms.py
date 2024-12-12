from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import UserImage

class Registration(UserCreationForm):
    name = forms.CharField(max_length = 32)
    email = forms.EmailField()


class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserImage
        fields = ['image']
