import bottle
from app.views import Home

@bottle.route('/assets/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root='assets')

bottle.debug(True)
bottle.run(host='0.0.0.0', port=8080)
