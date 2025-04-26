# Assignment_10/creational_patterns/builder.py
class Order:
    def __init__(self, order_id, customer_name):
        self.order_id = order_id
        self.customer_name = customer_name
        self.items = []
        self.discount = None
        self.delivery = None
    
    def __str__(self):
        return f"Order[ID={self.order_id}, Customer={self.customer_name}, Items={self.items}, Discount={self.discount}, Delivery={self.delivery}]"

class OrderBuilder:
    def __init__(self, order_id, customer_name):
        self.order = Order(order_id, customer_name)
    
    def add_item(self, name, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.order.items.append((name, quantity))
        return self
    
    def set_discount(self, discount):
        self.order.discount = discount
        return self
    
    def set_delivery(self, delivery):
        self.order.delivery = delivery
        return self
    
    def build(self):
        return self.order


