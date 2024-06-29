from utils.imports import BotCommand, Bot


async def setup_bot_commands(bot: Bot):
    bot_commands = [
        BotCommand(command="/command", description="Description"),
    ]
    await bot.set_my_commands(bot_commands)
