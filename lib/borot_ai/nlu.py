"""
nlu.py - module for Natuarl Language Understanding tasks
"""

# import dependencies
import os

from .BiLSTM_CRF.bilstm_crf.inference import NameEntityRecognizer as NER
from .intent_classifier.inference import IntentClassifier as IC
from . import borotai_configs as configs

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

def intent_detection(ic, input):
	"""
	intent_detection - function for Intent Detection
	Inputs:
		- ic: IntentClassifier object
		- input: str
			Raw query input
	Outputs:
		- output: str
			Detected intent
	"""

	output = ic.predict(input)

	return output

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

def initialize_borot_ai():
	# initialize BiLSTM-CRF model
	ner = NER(configs.BILSTM_CRF_MODEL, tag_table = configs.BILSTM_CRF_TAG_PATH, word_table = configs.BISLTM_CRF_WORD_PATH)


	return ner
