from flask import url_for
from rauth.service import OAuth2Service
from contasdoape.models.ControleDeAcesso import ControleDeAcesso
from contasdoape.web import app

class Facebook:
    graph_url = 'https://graph.facebook.com/'

    _facebook = OAuth2Service(name='facebook',
                              authorize_url='https://www.facebook.com/dialog/oauth',
                              access_token_url=graph_url + 'oauth/access_token',
                              client_id=app.config['FB_CLIENT_ID'],
                              client_secret=app.config['FB_CLIENT_SECRET'],
                              base_url=graph_url)
    
    def __init__(self, autorizado_url):
        self.autorizado_url = autorizado_url

    def login_url(self):
        params = {'redirect_uri': self.autorizado_url}
        return self._facebook.get_authorize_url(**params)
    
    def logar(self, request_args):
        if not 'code' in request_args:
            return None

        data = {'code' : request_args['code'], 
                'redirect_uri' : url_for('authorized', _external = True)}

        me = self._facebook.get_auth_session(data = data).get('me').json()
        usuario = ControleDeAcesso().obter_usuario(me['id'], 
                                                   me['username'], 
                                                   me['name'])
    
        return usuario
