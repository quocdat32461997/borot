"""
agent_execution.py - module for read/write execution
"""

# import dependencies
import os

from lib.borot_ai import ner, intent_detection, response_generator

def question_answer(user, NERobj,  query):
	"""
	ask - function to provoke Borot agent given text input
	Inputs:
		- user : User class object
			User class object to store conversation logs
		- NERobj : NameEntityRecognizer class object
			Class object for Name Entity Recognition
		- query : str
			Input text (question/query)
	Outputs:
		- output : str
			Output text (answer/response)
	"""

	# intent detection
	intent = intent_detection(query)

	# identify name-entities
	tags = ner(NERobj, query)

	# generate response
	response = response_generator(user, input)

	return response
