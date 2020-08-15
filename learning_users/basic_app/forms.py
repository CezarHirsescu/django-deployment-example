from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


# form for the builtin "user" model
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


# form for the "UserInfo" model
class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
