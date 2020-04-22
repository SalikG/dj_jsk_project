

class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self, products, deals):
        self.products = products
        self.deals = deals
