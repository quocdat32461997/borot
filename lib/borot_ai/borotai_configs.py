"""
borotai_configs.py - module to store configurations for Borot AI modules
"""

# import dependencies
import os

# retrieve AI path
BOROT_AI_PATH = os.path.dirname(os.path.abspath(__file__))

# BiLSTM_CRF paths
BILSTM_CRF = os.path.join(BOROT_AI_PATH, 'BiLSTM_CRF')
BILSTM_CRF_MODEL = os.path.join(BILSTM_CRF, 'bilstm_crf_model')
BILSTM_CRF_MODEL_AWS = ''
BILSTM_CRF_WORD_PATH = os.path.join(BILSTM_CRF, 'words.txt')
BILSTM_CRF_TAG_PATH = os.path.join(BILSTM_CRF, 'tags.txt')

# intent_classifier paths
IC = os.path.join(BOROT_AI_PATH, 'intent_classifier')
IC_MODEL = os.path.join(IC, 'intent_classifier.sav')
IC_VECTORIZER_PATH = os.path.join(IC, 'tfidf_vectorizer.pickle')
IC_INTENT_PATH = os.path.join(IC, 'intent_list.txt')

# intent-action path
INTENT_ACTION = os.path.join(BOROT_AI_PATH, 'intent_actions_list.txt')
