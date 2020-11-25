"""
This unit test file checks the base price for the items given the 
product type and associated options.

Testing Framework Used: pytest
"""

import sys, os
import json
sys.path.append('src')

from product import ProductInfo

BASE_PRICE = "sample_input/base-prices.json"

PRODUCT_TYPE = ["hoodie", "sticker", "hoodie", ""]

OPTIONS = [{'size': 'small', 'colour': 'white', 'print-location': 'front'}, 
            {"size": "small"}, 
            {"size": "xl", "colour": "dark", "print-location": "back"},
            {}]

BASE_PRICE_ITEMS = [3800, 221, 4368, 0]

def testBasePrice():
    
    with open(BASE_PRICE) as f:
        base_price_data = json.load(f)

    productInfo = ProductInfo(base_price_data)
    
    for i in range(4):
        base_price = productInfo.getBasePrice(PRODUCT_TYPE[i], OPTIONS[i])

    assert base_price == BASE_PRICE_ITEMS[i]


