from django.shortcuts import render, redirect

from .models import Blog

from user_auth.models import User


def index(request):
    if 'username' in request.session:
        user = User.objects.filter(username=request.session['username']).first()
        blogs = Blog.objects.filter(creator=user)

        return render(
            request,
            'index.html',
            {
                'user': user,
                'blogs': blogs
            }
        )

    return redirect('/login')
