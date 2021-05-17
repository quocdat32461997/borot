"""
conversation.py - module to store Log class
"""

# import dependencies
from collections import deque

class Log:
	"""
	Log - class to sotre single-session logs of conversations of users' queries (questions) and agenets' responses (answers)
	"""

	def __init__(self, user_id):
		"""
		__init__ - Log constructor
		Inputs:
			- user_id : int
				Id of the user who owns the conversation logs
		"""
		self.user_id = user_id
		self.logs = []

	def _load_conversations(self):
		"""
		_load_conversations - function to load conversation logs from database initially
		"""

		self.logs = []

	def add(self, query, response, status = 0):
		"""
		add - function to add new queries/response to logs
		Inputs:
			- query : str
				User's query
			- response : str
				Agent's response
			- status: int
				-1, 0, 1 values for the user's rating on Agent. By default, 0 for neutral
		Outputs:
			- None
		"""
		self.logs.append({
			'query' : query,
			'response' : response,
			'status' : status})
