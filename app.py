"""
app.py - start of borot server
"""

# import dependencies
import os
from flask import Flask, request, jsonify
import boto3
import logging

from lib import configs
from lib.controllers import  question_answer

# initialize Flask app and DB
USER = None

def main():
	APP.run(debug = True)

@APP.route('/')
def hi():
	return 'Hello, this is Borot. \n Did we meet before? If not, what is your name?'

@APP.route('/ask', methods = ['POST'])
def ask():
	return question_answer(USER, request.form('query'))

if __name__ == '__main__':
	main()
