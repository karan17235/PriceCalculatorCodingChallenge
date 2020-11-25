"""
The main.py file is the driving file for running the program. It accepts two
command line JSON arguments, first - the path of the cart file and second - the 
path of the base prices file.
It returns the total price of the cart.
"""

import sys
import os
from product import ProductInfo
from cart import Cart
from readJson import readJson


def main():
    """
    It  takes two command line arguments. Read and converts the file
    to Json objects, builds a price dictionary and calculates the total
    price of the cart.

    Usage: python3 main.py <cart.json> <base_prices.json>

    Arguments:
        cart.json - A Json formatted cart file
        base_prices.json - A Json formatted base prices file

    Returns: The total price of the cart
    """

    args = sys.argv
    base_price_schema = "json_schema/base-prices.schema.json"
    cart_schema = "json_schema/cart.schema.json"

    # Check for the number of arguments
    if len(args) != 3:
        print("The program expects only three command line arguments")
        print("Usage: python3 main.py <path_to_cart_file> <path_to_base_price_file>")
    else:
        cart_file = args[1]
        base_price_file = args[2]

        # read the base price file
        try:
            price_data = readJson(base_price_file)
        except Exception as e:
            raise OSError("Please check the base price file path and file name")

        # read the cart file.
        try:
            cart_data = readJson(cart_file)
        except Exception as e:
            raise OSError("Please check the cart price file path and file name")

        # Create a dictionary for product type.
        productInfo = ProductInfo(price_data)

        # Cart object to calculate price for each item and calculate the total cart amount.
        cart = Cart(cart_data, productInfo)
        print("Total Amount: ", cart.calculate_cart_total())

if __name__ == "__main__":
	main()

