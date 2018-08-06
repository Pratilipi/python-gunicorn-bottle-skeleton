from src import controller

def app_routes(app):
    # health calls
    app.route('/health', ['OPTIONS', 'GET'], controller.health)

    # ping db
    app.route('/pingdb', ['OPTIONS', 'GET'], controller.pingdb)
