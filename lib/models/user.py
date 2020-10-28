"""
user.py - module to store User class
"""

# import dependencies
import os


class User:
	"""
	User class to store user/retrieve user information
	"""
	def __init__(self, first_name = None, last_name = None):
		self.first_name = first_name
		self.last_name = last_name
	
	def _save_user(self):
		"""
		Function to initialize new user and save to database
		"""
		return None

	def __call__(self):
		return None
