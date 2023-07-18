from flask import Blueprint, render_template, request
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", title="Order Details", order_list = orders)

# a route to display one order
@orders_blueprint.route("/orders/<index>", methods=["GET"])
def order():
    return render_template("order.html", title="Customer Order", order_list = orders[index])