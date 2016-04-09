

class Order:
    def __init__(self, customer_name, order_no):
        from circular_references.fix1_customer import Customer
        self.customer = Customer(customer_name)
        self.order_no = order_no
