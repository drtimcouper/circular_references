from bad_customer import Customer

class Order:
    def __init__(self, customer_name, order_no):
        self.customer = Customer(customer_name)
        self.order_no = order_no
