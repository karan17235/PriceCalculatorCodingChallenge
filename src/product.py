"""
product.py contains ine class ProductInfo which accepts the 
base price Json object, creates a dictionary of product-type 
with a unique product type as the key and different options
and their corresponding base prices as the values.
"""

from itertools import groupby

class ProductInfo:
	"""ProductInfo class initializes a dictionary to group
	infomration for each product.

	Attributes: A Json object of base price file.

	Returns: The base price of each item obtained by filtering 
	all the values from the pruduct info dictionary using the 
	product_type and options.
	"""
	
	def __init__(self, base_price_data):
		"""
		Initialize a dictionary to store each product-typoe such as 
		'Hoodie' as a key and the different options available and 
		their base price as the values.
		"""
		self.product_info = {}

		key = lambda item: item["product-type"]
		for product_type, product_data in groupby(base_price_data, key):
			self.product_info[product_type] = list(product_data)

	def getBasePrice(self, product_type, options):
		"""This function returns base price of the product given
		the product_type and options.

		Args:
			product_type (string): information of the product type.
			options (object): key-value pairs of strings.
		"""

		# get the information for the current product type, returns None
		# if the key is not present
		curr_product_info = self.product_info.get(product_type)
		# print(product_type)
		# print(options)
		base_price = 0

		if curr_product_info is None: # there is no such product_type in the base_price file
			return 0

		for item in curr_product_info:
			item_present = True
			item_options = item["options"]

			for option_name, values in item_options.items():
				# check if all the options are present in the curr_product_info
				if options[option_name] not in values:
					item_present = False

			if item_present==True:
				base_price = item["base-price"]
				return base_price
		
		return base_price
					
			


		