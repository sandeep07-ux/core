from django import forms
from django.db.models import fields
from .models import Core

class PostForm(forms.ModelForm):
    class Meta:
        model = Core
        fields = '__all__'