from os import environ
import yaml

class Environments():
    def __init__(self, app=None, var_name=None, default_env=None):
        self.app = app
        self.var_name = var_name or 'FLASK_ENV'
        self.default_env = default_env or 'DEVELOPMENT'
        self.env = environ.get(self.var_name, self.default_env)

        if app:
            self.init_app(app)

    def init_app(self, app):
        app.config['ENVIRONMENT'] = self.env

        if app.extensions is None:
            app.extensions = {}

        app.extensions['environments'] = self

    def from_object(self, config_obj):
        for name in self._possible_names():
            try:
                obj = '%s.%s' % (config_obj, name)
                self.app.config.from_object(obj)
                return
            except:
                pass

        self.app.config.from_object(config_obj)

    def from_yaml(self, path):
        with open(path) as arquivo:
            arquivo = yaml.load(arquivo)

        try:
            conf = [arquivo[name] for name in self._possible_names() 
                    if name in arquivo][0]

            for key, value in conf.items():
                if key.isupper():
                    self.app.config[key] = value
        except:
            pass

    def _possible_names(self):
        return (self.env, self.env.upper(), self.env.lower())
