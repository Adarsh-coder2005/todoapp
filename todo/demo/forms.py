from django.core import validators
from django import forms
from .models import User,Todo

class Users(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','email','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }
        

class Login(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','password']
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }
        

      

class Task(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task','info','author']
        widgets = {
            'task': forms.TextInput(attrs={'class':'form-control'}),
            'info': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'})
        }