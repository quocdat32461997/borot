"""
app.py - start of borot server
"""

# import dependencies
import os
from flask import Flask, request, jsonify
import boto3
import logging

from lib import configs, initialize_db, NER
from lib.controllers import parse_user, question_answer

# initialize Flask app and DB
app = Flask(__name__)
user = None

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
	data = request.json
	user = parse_user(
		first_name = ['first_name'],
		last_name = data['last_name'],
		email = data['email'])
	return 'Welcome to Borot'

@app.route('/ask', methods = ['POST'])
def ask():
	return question_answer(user, request.json['query'])

if __name__ == '__main__':
	main()
