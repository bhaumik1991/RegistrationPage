import re
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.core.validators import validate_email

class userform(forms.ModelForm):
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required=True, max_length=50)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter email Id'}),required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter First Name'}),required=True, max_length=50)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Last Name'}),required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-Enter Password'}),required=True, max_length=50)

    class Meta():
        model = User
        fields = ['user_name','email','first_name','last_name', 'password']
    def clean_username(self):
        user = self.cleaned_data['user_name']
        try:
            match = User.objects.get(username = user)
        except:
            return self.cleaned_data['user_name']
        raise forms.ValidationError('Username already exist')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        if email and not re.match(EMAIL_REGEX, email):
            raise forms.ValidationError("Invalid Email")
        return email

    def clean_confirm_password(self):
        pas = self.cleaned_data['password']
        cpas = self.cleaned_data['confirm_password']
        MIN_LENGTH = 8
        if pas and cpas:
            if pas != cpas:
                raise forms.ValidationError('Password does not match')
            else:
                if len(pas) < MIN_LENGTH:
                    raise forms.ValidationError('Password must be %d character!' %MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError('Password should not contain all numeric')
class loginform(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Username'}),required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'}),required=True, max_length=50)

    class Meta():
        model = User
        fields = ['username', 'password']
