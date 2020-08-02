import yaml
import os

GLOBAL_CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config', 'ml_config.yaml')

with open(GLOBAL_CONFIG_PATH) as fp:
    GLOBAL_CONFIG = yaml.load(fp, Loader=yaml.FullLoader)

SPACY_MODEL = GLOBAL_CONFIG['application']['spacy_model']
