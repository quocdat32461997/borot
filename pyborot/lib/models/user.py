"""
user.py - module to store User class
"""

# import dependencies
import os


class User:
	"""
	User class to store user/retrieve user information
	"""
	def __init__(self, user_id = None, first_name = None, last_name = None, email = None):
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.user_id = user_id
	
	def _save_user(self):
		"""
		Function to initialize new user and save to database
		"""
		return None

	def __call__(self):
		return None
