import os
from dotenv import load_dotenv
load_dotenv() 
PORT = int(os.getenv("PORT", 8080)) 
ENV = os.getenv("ENV", "production")
DEBUG = False if ENV == "production" else True 