import yaml
import os
from pathlib import Path

GLOBAL_CONFIG_PATH = os.path.join(Path(os.path.abspath(__file__)).parent, '..', 'config', 'ml_config.yaml')

print(os.path.abspath(__file__))
with open(GLOBAL_CONFIG_PATH) as fp:
    GLOBAL_CONFIG = yaml.load(fp, Loader=yaml.FullLoader)

SPACY_MODEL = GLOBAL_CONFIG['application']['spacy_model']
