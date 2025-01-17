from multiprocessing import AuthenticationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Contact, User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


class ItemForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name1', 'name']
class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput(), label='Password')




class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()

