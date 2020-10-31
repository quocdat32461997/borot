"""
nlu.py - module for Natuarl Language Understanding tasks
"""

# import dependencies
import os

def ner(user, input):
	"""
	ner - fucntion for Name Entity Recognition
	Inputs:
		- user: User class object
		- input: str
			Raw query input
	Outputs:
		- outputs: dict
			Name entities
	"""

	output = {} # output dict of entities : values

	return outputs

def intent_detection(user, input):
	"""
	intent_detection - function for Intent Detection
	Inputs:
		- user: User class object
		- input: str
			Raw query input
	Outputs:
		- output: str
			Detected intent
	"""

	return None

def generate_response(user, input):
	"""
	generate_response - function to generate response
	Inputs:
		- user: User class object
		- input: str
			Raw query input
	Outputs:
		- output: str
			Generated request
	"""

	output = None
	return output
