# This file defines classes for flask configuration
import os


class Config:
    """Flask configuration class.
    """
    DEBUG = os.environ['DEBUG']
    SECRET_KEY = os.environ['SECRET_KEY']
    API_KEY = os.environ['API_KEY']
    DB_URI = os.environ['DB_URI']
    REGION = os.environ['REGION']
    PREFERRED_URL_SCHEME = ('https', 'http')[DEBUG == 'True']
    CITY_MAP = {'eastus': ['new york', 'boston', 'washington dc'], 
                'westus': ['san francisco', 'seattle', 'los angeles'], 
                'northeneurope': ['amsterdam', 'paris', 'rome']}
