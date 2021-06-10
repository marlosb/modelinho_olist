import sys

from abt import get_abt
from train import get_models

# Create constants
DATA_PATH = 'data/olist_dsa.db'
QUERY_PATH = 'sql/Script_ABT_olist_dtref_safra_20200818.sql'
model_path = 'models/'

primeira_safra = "2018-03-01"
ultima_safra = "2018-05-01"

if __name__ == '__main__':

    if '-abtonly' in sys.argv:
        print('Generating ABT')
        get_abt(DATA_PATH, QUERY_PATH, primeira_safra, ultima_safra)
    elif '-trainonly' in sys.argv:
        print('Training models')
        get_models(DATA_PATH, model_path)
    else:
        print('Generating ABT and training models')
        get_abt(DATA_PATH, QUERY_PATH, primeira_safra, ultima_safra)
        get_models(DATA_PATH, model_path)