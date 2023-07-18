from flask import Blueprint, render_template
from models.order_list import orders

orders_blueprint = Blueprint("orders", __name__)

@orders_blueprint.route("/orders")
def index():
    return render_template("index.html", customer_name="Order Details", order_list = orders)

# # a route to display one order
# def get_order(index):
#     order = order[index]
#     return order