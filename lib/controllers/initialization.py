"""
initialization.py - module for Database connections
"""

# import dependencies
import os
import pymysql

from lib import configs
from lib.borot_ai import *

def local_db():
	"""
	local_db - function to initialize connections to local MySQL
	Inputs: None
	Outputs: None
	"""

	connetion = pymysql.connect(host = configs.HOST, user = os.environ['LOCAL_DB_USER'], passwore = os.environ['LOCAL_DB_PASSWORD'], db = configs.DB)
	return connection


def aws_db():
	"""
	aws_db - function to initalize connections to AWS RDS
	Inputs: None
	Outputs: None
	"""
	return None

def main(mode = 'local'):
	# connect to AWS RDS
	try:
		# local db
		if mode == 'local':
			print("Connected to local MySQL")
			return local_db()
		# aws db
		else:
			print("Connected to AWS DS")
	except Exception as error:
			print(error)
