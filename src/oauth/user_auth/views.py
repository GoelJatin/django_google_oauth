from django.contrib import messages

from django.shortcuts import render, redirect

from django.views import View

from .models import User, UserAuth
from .forms import LoginForm, SignupForm

from .encrypt import encrypt

from google_auth.auth_helper import GoogleOauth


GOOGLE_OAUTH = GoogleOauth()
GOOGLE_OAUTH.setup()


class LoginView(View):
    template = 'login.html'

    def get(self, request):
        username = request.session.get('username')

        if username:
            return redirect('/blogs/')

        print(GOOGLE_OAUTH.get_authorization_url())

        return render(
            request,
            self.template,
            {
                'login_form': LoginForm(),
                'google_auth_url': GOOGLE_OAUTH.get_authorization_url()
            }
        )

    def post(self, request):
        data = request.POST.copy()
        login_form = LoginForm(data)
        error = False

        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            try:
                user = User.objects.get(username=username)
                user_auth = UserAuth.objects.get(user=user)
            except (User.DoesNotExist, UserAuth.DoesNotExist):
                messages.error(request, 'No user found with given username. Check the username or signup now')
                error = True
            else:
                if encrypt(user.salt, login_form.cleaned_data['password']) != user_auth.password.tobytes():
                    messages.error(request, 'Password does not match')
                    error = True

            if error:
                return render(
                    request,
                    self.template,
                    {
                        'login_form': LoginForm(data),
                        'google_auth_url': GOOGLE_OAUTH.get_authorization_url()
                    }
                )

            request.session['username'] = user.username
            return redirect('/blogs/')


class SignupView(View):
    template = 'signup.html'

    def get(self, request):
        username = request.session.get('username')

        if username:
            return redirect('/blogs/')

        return render(
            request,
            self.template,
            {
                'signup_form': SignupForm()
            }
        )

    def post(self, request):
        data = request.POST.copy()
        signup_form = SignupForm(data)

        if signup_form.is_valid():
            signup_form.save()

            user = User.objects.get(username=signup_form.cleaned_data['username'])
            user_auth = {
                'user': user,
                'password': encrypt(user.salt, signup_form.cleaned_data['password'])
            }
            print(user_auth)
            user_auth = UserAuth.objects.create(**user_auth)
            user_auth.save()

            request.session['username'] = user.username
            return redirect('/blogs/')

        return render(
            request,
            self.template,
            {
                'signup_form': SignupForm()
            }
        )


def logout(request):
    if 'username' in request.session:
        del request.session['username']

    return redirect('/login')
