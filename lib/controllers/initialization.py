"""
initialization.py - module for Database connections
"""

# import dependencies
import os
import pymysql

def main(mode = 'local'):
	# connect to AWS RDS
	try:
		# local db
		if mode == 'local':
			print("Connected to local MySQL")
		# aws db
		else:
			print("Connected to AWS DS")
	except Error as error:
			print(error)
			

