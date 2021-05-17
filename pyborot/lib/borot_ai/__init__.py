# borot_ai

from .nlu import initialize_borot_ai, ner, intent_detection, response_generator
from .BiLSTM_CRF.bilstm_crf.inference import NameEntityRecognizer as NER
from .intent_classifier.inference import IntentClassifier as IC
