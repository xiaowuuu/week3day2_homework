from flask import Flask
from controllers.orders_controller import orders_blueprint

app = Flask(__name__)
app.register_blueprint(orders_blueprint)

@app.route("/")
def index():
    return "Welcome to the order list"



@app.route("/<int:id>", methods=["GET"])
def get_id(id):
    return f"the id is {id}"