from flask import Flask

def register_blueprints(app: Flask):
    from .menu_routes import bp as menu_bp
    from .order_routes import bp as order_bp
    app.register_blueprint(menu_bp, url_prefix='/api/menu')
    app.register_blueprint(order_bp, url_prefix='/api/orders')
