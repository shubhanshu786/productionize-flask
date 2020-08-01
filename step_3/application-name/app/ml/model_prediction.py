import spacy
from app.utils.commons import SPACY_MODEL
from app import logger

SPACY_NLP = None


def load_model():
    global SPACY_NLP
    if SPACY_NLP is None:
        try:
            SPACY_NLP = spacy.load(SPACY_MODEL)
        except:
            logger.error('Some error occurred while loading spacy model')


def process_pos(doc, results):
    result_list = []
    for token in doc:
        result_list.append((token.text, token.pos_))
    results['pos'] = result_list


def process_ner(doc, results):
    result_list = []
    for ent in doc.ents:
        result_list.append((ent.text, ent.label_))
    results['ner'] = result_list


def process_tokenization(doc, results):
    result_list = []
    for token in doc:
        result_list.append(token.text)
    results['tokens'] = result_list


def process_document(text, task):
    global SPACY_NLP
    load_model()
    doc = SPACY_NLP(text)
    results = {
        'text': text
    }
    if task.lower() == 'pos':
        process_pos(doc, results)
    elif task.lower() == 'ner':
        process_ner(doc, results)
    elif task.lower() == 'tokens':
        process_tokenization(doc, results)
    else:
        logger.error('Wrong parameter passed')
    return results
