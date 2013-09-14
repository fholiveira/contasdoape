import bottle
from app.views import despesa, sumario
from mongoengine import connect

@bottle.route('/assets/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='assets')

connect('contasdoape')

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8083, reloader=True)
