from rauth.service import OAuth2Service
from contasdoape.models.ControleDeAcesso import ControleDeAcesso
from contasdoape.web import app
from flask import session

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
   
    def logout(self, redirect_url):
        url = 'https://www.facebook.com/logout.php?'
        url += 'access_token=' + session['fb_token']
        url += '&confirm=1'
        url += '&next=' + redirect_url 
        
        return url

    def logar(self, request_args):
        if not 'code' in request_args:
            return None

        data = {'code' : request_args['code'], 
                'redirect_uri' : self.autorizado_url} 
        
        fb_session = self._facebook.get_auth_session(data = data)
        session['fb_token'] = fb_session.access_token

        me = fb_session.get('me').json()
        usuario = ControleDeAcesso().obter_usuario(me['id'], 
                                                   me['name'])
    
        return usuario
