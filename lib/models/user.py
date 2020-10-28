"""
user.py - module to store User class
"""

# import dependencies
import os


class User:
	"""
	User class to store user/retrieve user information
	"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def __call__(self):
		return None
