import asyncio

from bot import dp, bot
from routers.index import register_routers
from config import USE_DB
from utils.helpers import setup_bot_commands
from db.redis import connect_to_db


async def main():
    if USE_DB:
        connect_to_db()

    register_routers(dp)
    await setup_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
