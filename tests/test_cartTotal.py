"""
This unit test file checks the toal cart amount given different cart files.

Testing Framework Used: pytest
"""

import sys, os
import json
sys.path.append('src')

from product import ProductInfo
from cart import Cart

BASE_PRICE = "sample_input/base-prices.json"

CART_INPUT = ["sample_input/cart-4560.json", "sample_input/cart-9363.json", "sample_input/empty-cart.json"]

CART_TOTAL_OUTPUT = [4560, 9363, 0]

def testCartTotal():
    with open(BASE_PRICE) as f:
        base_price_data = json.load(f)

    productInfo = ProductInfo(base_price_data)
    
    for i in range(3):
        with open(CART_INPUT[i]) as f:
            cart_data = json.load(f)
        
        cart = Cart(cart_data, productInfo)

        total = cart.calculate_cart_total()
        assert total == CART_TOTAL_OUTPUT[i]


