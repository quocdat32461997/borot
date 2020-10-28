"""
app.py - start of borot server
"""

# import dependencies
import os
from flask import Flask, request, jsonify
import boto3
import logging

from lib import initialize

# initialize Flask app
app = Flask(__name__)

def main():
	connection = initialize()
	app.run()

@app.route('/')
def home():
	return 'Hellow, this is Borot'

@app.route('/ask', methods = ['POST'])
def ask():
	return jsonify({'response' : 'Hi from Borot'})

if __name__ == '__main__':
	main()
