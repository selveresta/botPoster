# bot.py
from utils.imports import MemoryStorage, Bot, Dispatcher
import logging
import config

if config.DEBUG:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler("../bot.log"),  # Log to a file
            logging.StreamHandler(),  # Log to console
        ],
    )

logger = logging.getLogger(__name__)

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
