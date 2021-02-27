from pathlib import Path

import google.oauth2.credentials
import google_auth_oauthlib.flow

BASE_DIR = Path(__file__).resolve().parent


class GoogleOauth:

    INSTANCE = None

    def __new__(cls, *args, **kwargs):
        if GoogleOauth.INSTANCE:
            return GoogleOauth.INSTANCE

        GoogleOauth.INSTANCE = object.__new__(cls)
        return GoogleOauth.INSTANCE

    @property
    def flow(self):
        return self._flow

    def setup(self, state=''):
        try:
            self._flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
                Path.joinpath(BASE_DIR, 'google_oauth.json'),
                scopes=[
                    'https://www.googleapis.com/auth/userinfo.email',
                    'https://www.googleapis.com/auth/userinfo.profile',
                    'openid'
                ],
                state=state
            )

            self._flow.redirect_uri = 'http://localhost/oauth-callback'
        except Exception as excp:
            print(excp)

    def get_authorization_url(self):
        if self._flow is None:
            return ('', '')

        authorization_url, state = self._flow.authorization_url(
            access_type='offline',
            include_granted_scopes='true'
        )

        self.setup(state)

        return authorization_url

    def exchange_code(self, code):
        if self._flow is None:
            return ('', '')

        self._flow.fetch_token(code=code)
