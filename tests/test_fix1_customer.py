from nose.tools import assert_equal, assert_is_instance

import circular_references.fix1_customer as customer
import circular_references.fix1_order as order

Customer = customer.Customer
Order = order.Order

def test_get_orders():
    cust = Customer('Fred')
    orders = cust.get_orders()
    assert_equal(len(orders), 2)
    assert_is_instance(orders[0], Order)
