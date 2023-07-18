class Order():

    def __init__(self, customer_name, item, quantity, order_date, additional_request):
        self.customer_name = customer_name
        self.item = item
        self.quantity = quantity
        self.order_date = order_date
        self.additional_request = additional_request