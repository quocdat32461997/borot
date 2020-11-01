"""
agent_execution.py - module for read/write execution
"""

# import dependencies
import os

from lib.controllers import connect2db
from lib.borot_ai import ner, intent_detection, response_generator

def question_answer(USERobj, NERobj, ICobj, query, intents, tags):
	"""
	ask - function to provoke Borot agent given text input
	Inputs:
		- user : User class object
			User class object to store conversation logs
		- NERobj : NameEntityRecognizer class object
			Class object for Name Entity Recognition
		- ICobj : IntentClassifier class object
			Class object for Intent Classification
		- query : str
			Input text (question/query)
		- intents : list
			List of intents
		- tags : list
			List of tags
	Outputs:
		- output : str
			Output text (answer/response)
	"""

	# initialize database
	db = connect2db()

	# intent detection
	intent = intent_detection(ICobj, query)

	# identify name-entities
	ner_output = ner(NERobj, query)
	text = ner_output['text'].tolist()[0]
	tags = ner_output['tags'].tolist()[0]

	# generate response
	response = response_generator(intent, tags, query)

	print(response, intent, text, tags)

	# close db connection
	db.close()

	return intent, text, tags
