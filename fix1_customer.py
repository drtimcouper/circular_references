from circular_references.fix1_order import Order

DATABASE_ORDER_NUMBERS = [1022, 1243]


class Customer:

    def __init__(self, name):
        self.name = name

    def get_orders(self):
        orders = []
        for order_no in DATABASE_ORDER_NUMBERS:
            orders.append(Order(self.name, order_no))

        return orders
