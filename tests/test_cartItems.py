"""
This unit test file checks the total number of items in the cart.

Testing Framework Used: pytest
"""

import sys, os
import json
sys.path.append('src')

from product import ProductInfo
from cart import Cart

BASE_PRICE = "sample_input/base-prices.json"

CART_INPUT = ["sample_input/cart-4560.json", "sample_input/cart-9363.json", "sample_input/empty-cart.json"]

CART_ITEMS = [1, 2, 0]

def testCartItems():
    
    with open(BASE_PRICE) as f:
        base_price_data = json.load(f)

    productInfo = ProductInfo(base_price_data)
    
    for i in range(3):
        with open(CART_INPUT[i]) as f:
            cart_data = json.load(f)
        
        cart = Cart(cart_data, productInfo)

        total_cart_items = len(cart.cart_items)
        assert total_cart_items == CART_ITEMS[i]


