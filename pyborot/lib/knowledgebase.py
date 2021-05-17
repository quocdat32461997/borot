"""
knowledgebase.py - module for knowledge base
"""

# import dependencies
import re
import math
import string
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = stopwords.words('english')

def create_kb(tf_idf, idf):
	"""
	create_kb - function to create knowledge base
	Inputs:
		- tf_idf : dictionary of key-doc and values - dictionary of token and its tf-idf score
		- idf : dictionary of key-token and value - idf score
	Output:
		- kb : pandas DataFrame
	"""
	properties = {}

	# fill all tokens to each document
	for doc in tf_idf.keys():
		for token in idf.keys():
			if not token in tf_idf[doc]:
				tf_idf[doc][token] = 0.0
		properties[doc] = list(tf_idf[doc].values())

	return pd.DataFrame.from_dict(properties, orient = 'index', columns = list(idf.keys())) 


def initialize_knowledge_base(files):
	"""
	initialize_knowledge_base - function to initalize knowledge base
	Inputs:
		- files : list of str
			List of files
	Outputs:
		- output : TBD
	"""

	texts = []
	# read all text files
	for file in files:
		with open(file) as f:
			text = f.read()
		texts.append(text)

	# compute tf-idf and idf of documents
	tf_idf, idf = _term_freq(texts)

	"""
	# sort the most important temrs in documents
	for doc, words in tf_idf.items():
		tf_idf[doc] = [item for item in sorted(words.items(), key = lambda x: x[-1], reverse = True) if item[-1] != 0.0]
	"""

	return tf_idf, idf, texts

def _term_freq(inputs):
	"""
	term_freq - function to build knowledge base by term-frequency and inverse-document-frequency 
	Inputs:
		- inputs : list of String
			List of texts
	Outputs:
		- tf-idf : term-frequency-inverse-document-frequencey dictioanry
		- idf : inverse-document-frequency dictionary
	"""

	tf_idf_dict = {} # key - unqiue integer encoding each text, and values are dictionary of {key=token, vales=coutn} 
	idf_dict = {}

	# preprocess text, and build frequency dictionary
	for text, idx in zip(inputs, range(len(inputs))):
		# lowercase
		text = text.lower()

		# remove punctuations
		text = re.sub("[" + string.punctuation+"]*", '', text)
		
		# tokenize words
		tokens = word_tokenize(text)

		# remove stop words
		tokens = [token for token in tokens if not token in stop_words]

		# initialize idx documetn
		tf_idf_dict[idx] = {}

		# compute term-frequency
		for token in tokens:
			if not token in tf_idf_dict[idx]:
				tf_idf_dict[idx][token] = 1
			else:
				tf_idf_dict[idx][token] += 1
			if not token in idf_dict:
				idf_dict[token] = [idx]
			elif not idx in idf_dict[token]:
				idf_dict[token].append(idx)

	
	# comptue inverse-document-frequency
	for token in idf_dict.keys():
		idf_dict[token] = math.log((1 + len(inputs)) / (1 + len(idf_dict[token])))

	# compute tf-idf
	for doc in tf_idf_dict.keys():
		for token in tf_idf_dict[doc].keys():
			tf_idf_dict[doc][token] *= idf_dict[token]
			
	return tf_idf_dict, idf_dict
