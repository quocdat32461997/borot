"""
nlu.py - module for Natuarl Language Understanding tasks """

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
		- output: dict
			Name entities
	"""

	# model predictions
	output = ner.predict(input)
	
	return output

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
	print(ic)

	output = ic.predict(input)

	return output

def response_generator(intent, tags, tokens):
	"""
	response_generator - function to generate response (searching in this version)
	Inputs:
		- intent : str
			Intent
		- tags : list
			List of tags
		- tokens : list
			List of tokens
	Outputs:
		- _: dict
			Dictionary of Intent and Entities
	"""

	entities = {}
	for idx in range(len(tags)):
		if tags[idx] != 'o':
			tag = tags[idx][2:]

			if not tag in entities:
				entities[tag] = [tokens[idx]]

			else:
				entities[tag].append(tokens[idx])

	return {'Intent' : intent, 'Entities' : entities}

def initialize_borot_ai():
	"""
	initialize_borot_ai - function to initalize Borot-AI models, NER tags and intents
	Inputs: None
	Outputs:
		- ner : NameEntityRecognizer class object
		- ic : IntentClassifier class object
		- tags : list of NER tags
		- intents : list of intents
		- commands : dict of intent-action
	"""
	# initialize BiLSTM-CRF model
	ner = NER(configs.BILSTM_CRF_MODEL, tag_table = configs.BILSTM_CRF_TAG_PATH, word_table = configs.BILSTM_CRF_WORD_PATH)


	# initialize intent classifier
	ic = IC(model = configs.IC_MODEL, intents = configs.IC_INTENT_PATH, vectorizer = configs.IC_VECTORIZER_PATH)

	# read ner-tag list
	with open(configs.BILSTM_CRF_TAG_PATH) as file:
		tags = file.read().split('\n')

	# read intent list
	with open(configs.IC_INTENT_PATH) as file:
		intents = file.read().split('\n')

	return ner, ic, tags, intents
