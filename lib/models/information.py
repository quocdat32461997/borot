"""
info.py - module to store Info class
"""

class Info:
	"""
	Info - class to store retreived Info from DB
	"""

	def __init__(self, ids, texts, name = 'Info'):
		"""
		Infor class constructor
		Inputs:
			- ids : list of integers
				Unique ids for info pieces
			- texts : list of texts
				Infor texts
		"""

		self.ids = ids
		self.texts = texts
		self.name = name
