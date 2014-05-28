from contasdoape.models import ControleDeAcesso
from rauth.service import OAuth2Service


class FacebookProvider:
    ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'
    OAUTH_URL = 'https://www.facebook.com/dialog/oauth'
    LOGOUT_URL = 'https://www.facebook.com/logout.php'
    GRAPH_URL = 'https://graph.facebook.com/'

    def __init__(self, autorizado_url, client_id, client_secret, token=None):
        self.autorizado_url = autorizado_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

        self.facebook = OAuth2Service(name='facebook',
                                      authorize_url=self.OAUTH_URL,
                                      access_token_url=self.ACCESS_TOKEN_URL,
                                      client_id=client_id,
                                      client_secret=client_secret,
                                      base_url=self.GRAPH_URL)

    def login_url(self):
        params = {'redirect_uri': self.autorizado_url}
        return self.facebook.get_authorize_url(**params)

    def logout_url(self, redirect_url):
        url = self.LOGOUT_URL
        url += '?access_token=' + self.token
        url += '&confirm=1'
        url += '&next=' + redirect_url

        return url

    def logar(self, request_args):
        if 'code' not in request_args:
            return None

        data = {'code': request_args['code'],
                'redirect_uri': self.autorizado_url}

        fb_session = self.facebook.get_auth_session(data=data)
        perfil = fb_session.get('me').json()

        usuario = ControleDeAcesso() \
            .obter_usuario(perfil['id'], perfil['name'])

        self.token = fb_session.access_token
        return usuario

    def get_descriptor(self):
        return (self.autorizado_url,
                self.client_id,
                self.client_secret,
                self.token)

    @classmethod
    def from_descriptor(cls, descriptor):
        auth, fb_id, secret, token = descriptor
        return cls(auth, fb_id, secret, token=token)
