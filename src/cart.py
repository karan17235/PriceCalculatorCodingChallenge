"""
cart.py contains two classes ItemPrice and Cart.
ItemPrice takes each cart item and the base price to calculate the
final price of the product.
"""

from product import ProductInfo

class ItemPrice:
    """
    The class Item represents individual item in the cart.
    """

    def __init__(self, cart_item, base_price=None):

        self.artist_markup = cart_item['artist-markup']
        self.quantity = cart_item['quantity']
        self.base_price = base_price
        self.price = 0

        if base_price is not None:
            # calculating the price of item in the cart
            self.price = (base_price + round((base_price * self.artist_markup) / 100)) * self.quantity


class Cart:
    """
    The class Cart takes a cart JSON object and calculates the price 
    of each individual item by fecthing the base price from ProductInfo
    class using product_type and options. 

    It saves the price of individual item in the list and finally calculates
    the total cart ammount using calculate_cart_total function.
    """
    def __init__(self, cart_data, productInfo=None):
        
        # creating an empty list to store the cart items
        self.cart_items = []

        for item in cart_data:

            product_type = item['product-type']
            options = item['options']
            # get the base_price of the product.
            base_price = productInfo.getBasePrice(product_type, options)
            item_total = ItemPrice(item, base_price)
            self.cart_items.append(item_total.price)

    def calculate_cart_total(self):
        """It calculates the total price of the cart
        by adding the price of each individual item in the 
        cart.

        Returns:
            int: The total price of the cart
        """
        return sum(self.cart_items)


