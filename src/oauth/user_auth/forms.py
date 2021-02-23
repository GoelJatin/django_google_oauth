from django import forms

from uuid import uuid4

from .models import User
from .encrypt import encrypt


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', max_length=250, widget=forms.PasswordInput)


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        exclude = ('salt',)

    password = forms.CharField(label='Password', max_length=250, widget=forms.PasswordInput)

    def save(self):
        password = self.cleaned_data['password']
        del self.cleaned_data['password']

        self.cleaned_data['salt'] = uuid4().bytes
        user = User.objects.create(**self.cleaned_data)
        user.save()

        self.cleaned_data['password'] = password
