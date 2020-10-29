"""
user_execution.py - module for User functioanlity
"""

# import dependencies
import os

from lib.controllers import connect2db
from lib.models import User

def parse_user(first_name, last_name, email):
	"""
	add_user - function to add/retrieve user to/from database
	Inputs:
		- first_name : str
		- last_name : str
		- email: str
	Outputs:
		- user : User class object
			Initialized/retrieved User class object
	"""

	# initialize DB connection
	db = connect2db()

	# function execution
	user = User(first_name = first_name, last_name = last_name, email = email)

	# check existing account
	existed, user_id = _existing_account(db, user)
	if not existed:
		user_id = _add_user(db, user)
		
	# update User object
	user.user_id = user_id

	# close db connection
	db.close()

	return user

def _add_user(db, user):
	"""
	_add_user - function to add a new user to databse
	Inputs:
		- db : mysql connection
		- user : User class object
	Outputs: None
	"""
	
	# initialize cursor
	cursor = db.cursor()

	# SQL execution
	query = 'INSERT INTO user (first_name, last_name, email) VALUES (%s, %s, %s)'
	values = (first_name, last_name, email)
	cursor.execute(query, values)
	db.commit()

def _existing_account(db, user):
	"""
	_existing_account - function to check existing account
	Inputs:
		- db : mysql connection
		- user : User class object
	Outputs:
		- existed : boolean
			Existing/Non-existing flag	
		- user_info : int
			User_id if account existed
	"""

	# initialize cursor
	cursor = db.cursor()

	# SQl execution
	query = 'SELECT EXISTS(SELECT * FROM users WHERE email={})'.format(user.email)
	cursor.execute(query)
	
	if cursor.rowcount == 1:
		return True, cursor.fetchall()[0][-1]
	else:
		return False