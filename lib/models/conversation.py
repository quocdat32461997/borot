"""
conversation.py - module to store Log class
"""

# import dependencies
from collections import deque

class Log:
	"""
	Log - class to sotre single-session logs of conversations of users' queries (questions) and agenets' responses (answers)
	"""

	def __init__(self):
		"""
		__init__ - Log constructor
		"""
		self.log_id = 1
		self.logs = deque()

	def add(self, input):
		"""
		add - function to add new query/response to logs
		Inputs:
			- input : text
		Outputs:
			- None
		"""
		self.logs.append(input)
