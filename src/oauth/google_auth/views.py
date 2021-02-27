from django.shortcuts import render, redirect

from googleapiclient.discovery import build

from google_auth.auth_helper import GoogleOauth


GOOGLE_OAUTH = GoogleOauth()
GOOGLE_OAUTH.setup()


def callback(request):
    return render(
        request,
        'callback.html',
        {
            'callback_url': request.path,
            'code': request.GET['code']
        }
    )


def exchange(request):
    GOOGLE_OAUTH.get_authorization_url()
    GOOGLE_OAUTH.exchange_code(request.GET['code'])

    return render(
        request,
        'exchange.html',
        {
            'access_token': GOOGLE_OAUTH.flow.credentials.token
        }
    )


def user_info(request):
    service = build('people', 'v1', credentials=GOOGLE_OAUTH.flow.credentials)
    user = service.people().get(resourceName='people/me', personFields='names,emailAddresses').execute()

    return render(
        request,
        'user_info.html',
        {
            'name': user['names'][0]['displayName'],
            'email': user['emailAddresses'][0]['value']
        }
    )
