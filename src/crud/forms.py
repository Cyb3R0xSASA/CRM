from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Records


class CreateUserForm(UserCreationForm):
    class Meta:
        # When form successful submit create new user
        model = User # This refer to the model name in database, in user model username and password1 are required other fields optional
        fields = ['username', 'password1', 'password2'] # This refer to the columns that you need to use it in this model

class LoginFrom(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'UserName'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

class RecordsForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name', 'last_name', 'category', 'phone', 'tall', 'weight']