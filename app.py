"""
app.py - start of borot server
"""

# import dependencies
import os
from flask import Flask, request, jsonify
import boto3
import logging

from lib import configs, initialize_db
from lib.controllers import parse_user, question_answer

# initialize Flask app and DB
app = Flask(__name__)

def main():
	# initialize database
	initialize_db()

	# run app
	app.run(debug = True)

@app.route('/')
def hi():
	return 'Hello, this is Borot. \n Did we meet before? If not, what is your first-last name and email?'

@app.route('/user', methods = ['POST'])
def user():
	_ = parse_user(
		first_name = 'dat', #request.form('first_name'),
		last_name = 'ngo', #request.form('last_name'),
		email = 'gmail') #request.form('email'))
	return 'Welcome to Borot'

@app.route('/ask', methods = ['POST'])
def ask():
	return question_answer(USER, request.form('query'))

if __name__ == '__main__':
	main()
