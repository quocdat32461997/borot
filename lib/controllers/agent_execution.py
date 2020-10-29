"""
agent_execution.py - module for read/write execution
"""

# import dependencies
import os

from lib.borot_ai import ner, intent_detection

def question_answer(user, query):
	"""
	ask - function to provoke Borot agent given text input
	Inputs:
		- user : User class object
			User class object to store conversation logs
		- query : str
			Input text (question/query)
	Outputs:
		- output : str
			Output text (answer/response)
	"""

	# intent detection
	intent = intent_detection(query)


	return output
