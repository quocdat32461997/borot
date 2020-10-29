"""
initialization.py - module for Database connections
"""

# import dependencies
import os
import mysql.connector
from flask_sqlalchemy import SQLAlchemy

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
		print(db)
		
		print("Connected to local MySQL") 
		return db
	except:
		try:
			# initialize db connection without databse
			db = mysql.connector.connect(
				user = os.environ['LOCAL_DB_USER'],
				password = os.environ['LOCAL_DB_PASSWORD'],
				host = configs.HOST)
			# create databse
			cursor = db.cursor()
			cursor.execute('CREATE DATABASE {}'.format(configs.DB))
			db.commit()

			print("Connected to local MySQL") 
			return db

		except Exception as error:
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

