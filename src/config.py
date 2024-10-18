# config.py
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.environ.get("BOT_TOKEN", 0))

IS_GROUP_BOT = os.getenv("IS_GROUP_BOT", False) == "True"
DEBUG = os.getenv("DEBUG", True) == "True"

USE_DB = os.getenv("USE_DB", False)
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6377)
REDIS_DB = os.getenv("REDIS_DB", 0)
