"""
database.py - module to initialize MySQL database.
"""

# import dependencies
import os
import mysql.connector

from lib import configs

def _initialize_db(cursor):
	"""
	_initailize_db - function to intialize database
	Inputs: 
		- cursor : MySQL cursor
	Outputs: None
	"""

	try:
		query = 'CREATE DATABASE {}'.format(configs.DB)
		cursor.execute(query)
	except:
		print("Database {} exists".format(configs.DB))
	return None

def _initialize_tables(cursor):
	"""
	_initialize_tables - function to initialize tables as described
	Inputs: 
		- cursor : MySQL cursor
	Outputs: None
	"""

	# initialize User table
	query = 'CREATE TABLE IF NOT EXISTS users (user_id INT(255),first_name VARCHAR(100),last_name VARCHAR(100),email VARCHAR(100))'
	cursor.execute(query)

	# initialize Conversation table
	query = "CREATE TABLE IF NOT EXISTS conversations (user_id INT(255),log_id INT(255),query TEXT(65535),response TEXT(65535),status INT(1))"
	cursor.execute(query)

	# initialize Information table
	query = 'CREATE TABLE IF NOT EXISTS information (id INT(255),, content TEXT(65535))'
	cursor.execute(query)

	return None

def initialize_db():
	"""
	initialize_db - function to initalize database and tables in MySQL
	Inputs: None
	Outputs: None
	"""

	# initialize MySQL connection
	db = mysql.connector.connect(
		user = os.environ[configs.USER],
		password = os.environ[configs.PASSWORD],
		host = configs.HOST)
	cursor = db.cursor()

	# initialize database
	_initialize_db(cursor)

	# reinitialize MySQL connection after creating database
	db  = mysql.connector.connect(
		user = os.environ[configs.USER],
		password = os.environ[configs.PASSWORD],
		host = configs.HOST,
		database = configs.DB)
	cursor = db.cursor()

	# initialize tables
	_initialize_tables(cursor)

	# commit to Database changes
	db.commit()

	# close database connection
	db.close()
