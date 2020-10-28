"""
app.py - start of borot server
"""

# import dependencies
import os
from flask import Flask, request, jsonify
import boto3
import logging

# initialize Flask app
app = Flask(__name__)
app.debug = True

@app.route('/')
def hi():
	return jsonfiy({'response' : 'Hellow, this is Borot'})

@app.route('/heyborot', methods = ['POST'])
def hey_borot():
	return jsonify({'response' : 'Hi from Borot'})
