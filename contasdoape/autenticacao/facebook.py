from contasdoape.models import ControleDeAcesso
from rauth.service import OAuth2Service


class FacebookProvider:
    graph_url = 'https://graph.facebook.com/'

    def __init__(self, autorizado_url, client_id, client_secret, token = None):
        self.autorizado_url = autorizado_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.token = token

        self.facebook = OAuth2Service(name='facebook',
                        authorize_url='https://www.facebook.com/dialog/oauth',
                        access_token_url=self.graph_url + 'oauth/access_token',
                        client_id=client_id,
                        client_secret=client_secret,
                        base_url=self.graph_url)

    def login_url(self):
        params = {'redirect_uri': self.autorizado_url}
        return self.facebook.get_authorize_url(**params)

    def logout_url(self, redirect_url):
        url = 'https://www.facebook.com/logout.php?'
        url += 'access_token=' + session['fb_token']
        url += '&confirm=1'
        url += '&next=' + redirect_url

        return url

    def logar(self, request_args):
        if not 'code' in request_args:
            return None

        data = {'code': request_args['code'],
                'redirect_uri': self.autorizado_url}

        fb_session = self.facebook.get_auth_session(data=data)
        me = fb_session.get('me').json()
        usuario = ControleDeAcesso().obter_usuario(me['id'], me['name'])

        self.token = fb_session.access_token
        return usuario

    def get_descriptor(self):
        return (self.autorizado_url,
                self.client_id,
                self.client_secret,
                self.token)

    @classmethod
    def from_descriptor(cls, descriptor):
        auth, id, secret, token = descriptor
        return cls(auth, id, descriptor, token=token)
