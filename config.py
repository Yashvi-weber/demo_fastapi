from dotenv import load_dotenv 
import os

load_dotenv()

DB_URL = os.environ.get("DB_URL")
ALGORITHM = os.environ.get("algorithms")
SECRET_KEY = os.environ.get("secret_key")