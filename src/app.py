from flask import Flask
from controllers.menu_controller import menu_bp
from controllers.order_controller import order_bp
from controllers.table_controller import table_bp

app = Flask(__name__)

# Đăng ký route
app.register_blueprint(menu_bp, url_prefix="/menu")
app.register_blueprint(order_bp, url_prefix="/orders")
app.register_blueprint(table_bp, url_prefix="/tables")

@app.route("/")
def home():
    return {"message": "Welcome to Sushi Restaurant Management System"}

if __name__ == "__main__":
    app.run(debug=True)
