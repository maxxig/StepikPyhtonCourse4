from enum import Flag
class OrderStatus(Flag):
    ORDER_PLACED = 1
    PAYMENT_RECEIVED = 2
    SHIPPING_COMPLETE = 4


# TEST_3:
for order in OrderStatus:
    print(order)