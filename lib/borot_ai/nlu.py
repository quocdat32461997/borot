"""
nlu.py - module for Natuarl Language Understanding tasks
"""

# import dependencies
import os

def ner(ner, input):
	"""
	ner - fucntion for Name Entity Recognition
	Inputs:
		- ner : NameEntityRecognizer class object
		- input: str
			Raw query input
	Outputs:
		- outputs: dict
			Name entities
	"""

	# preprocess to accepted NER model input
	input = ner.preprocess(input)

	# model predictions
	predictions = ner.predict(input)
	
	# convert to tags
	tags = ner.pred_to_tags(predictions)

	return tags

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

def response_generator(user, input):
	"""
	response_generator - function to generate response
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
