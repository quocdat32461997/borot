"""
app.py - start of borot server
"""

# import dependencies
import os
from flask import Flask, request, jsonify
import boto3
import logging

from lib import configs, initialize_db, initialize_borot_ai, insert_knowledge_base
from lib.controllers import parse_user, question_answer

# initialize Flask app and DB
app = Flask(__name__)
user = None
ner, ic, tags, intents = initialize_borot_ai()
kb, db = insert_knowledge_base()

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
		first_name = data['first_name'],
		last_name = data['last_name'],
		email = data['email'])
	return 'Welcome to Borot'

@app.route('/ask', methods = ['POST'])
def ask():
	# parase query and generate response
	response = question_answer(USERobj = user, NERobj = ner, ICobj = ic, query = request.json['query'], intents = intents, tags = tags, kb = kb, db = db)

	return {'status_code' : 200, 'response' : response}

if __name__ == '__main__':
	main()
