"""
initialization.py - module for Database connections
"""

# import dependencies
import os
import mysql.connector

from lib import configs
from lib.borot_ai import *

def _local_db():
	"""
	_local_db - function to initialize connections to local MySQL
	Inputs: 
		- app : Flask aap
	Outputs: 
		- db : MySQL connection
	"""

	# initialize mysql connection
	try:
		db = mysql.connector.connect(
			user = os.environ['LOCAL_DB_USER'],
			password = os.environ['LOCAL_DB_PASSWORD'],
			host = configs.HOST,
			database = configs.DB)
		
		print("Connected to local MySQL") 
		return db
	except:
		print(error)

def _aws_db():
	"""
	aws_db - function to initalize connections to AWS RDS
	Inputs: None
	Outputs: None
	"""
	return None

def connect2db():
	"""
	connect2db - function to initialize connectino to db
	"""
	# connect to AWS RDS
	try:
		# local db
		if configs.HOST == 'localhost':
			return _local_db()
		# aws db
		else:
			print("Connected to AWS DS")
			return _aws_db()
	except Exception as error:
			print(error)

