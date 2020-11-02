"""
configs.py - module to store server configurations
"""

# import dependencies import os
import os
import json

# Database paramaters
DB = 'borot_ai'
HOST = 'localhost'
USER = 'LOCAL_DB_USER'
PASSWORD = 'LOCAL_DB_PASSWORD'

# path to knowledge base
KN_PATH = os.path.dirname(os.path.abspath(__file__))
KN_BASE_PATH = os.path.join(KN_PATH, 'knowledge_base')
