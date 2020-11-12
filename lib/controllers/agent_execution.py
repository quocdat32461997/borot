"""
agent_execution.py - module for read/write execution
"""

# import dependencies
import os

from lib.borot_ai import ner, intent_detection, response_generator

def question_answer(USERobj, NERobj, ICobj, query, intents, tags, kb, db):
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

		- kb : pandas DF
			DataFrame of knowledge base
		- db : list
			List of texts
	Outputs:
		- output : str
			Output text (answer/response)
	"""

	# intent detection
	intent = intent_detection(ICobj, query)

	# identify name-entities
	ner_output = ner(NERobj, query)
	text = ner_output['text'].tolist()[0]
	tags = ner_output['tags'].tolist()[0]

	# generate response
	response = response_generator(intent, tags, text)

	# search knowledge
	info = _search_info(response['Entities'], kb, db)
	
	return {'Intent' : intent, 'Entities' : response['Entities'], 'Relevant_info' : info}

def _search_info(input, kb, db):
	"""
	search_info - function to search info in Knowledge base given input tokens
	Inputs:
		- input : dict
			Dictionary of entity-key and list of words
		- kb : Pandas dataframe
			Dataframe of tokens x documents
		- db : list
			List of texts
	Outputs:
		- output : TBD
	"""
	# retrieva all words
	words = []
	for v in input.values():
		words.extend(v)

	# filter out-of-vocab keywords
	words = [word for word in words if word in kb.columns]
	print(words)

	if not words:
		return None
	# extract 
	doc = kb.sort_values(by = words, axis = 'index', ascending = False).index[0]

	return db[doc]
