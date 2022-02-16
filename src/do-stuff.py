from helpers import create_instance
import os
from dotenv import load_dotenv

load_dotenv() 

API_URL = os.getenv('API_URL')
API_KEY = os.getenv('API_KEY')

if __name__ == "__main__":
    create_instance(API_URL, API_KEY)