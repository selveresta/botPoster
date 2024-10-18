import logging
from utils.imports import Command, Message, CommandObject, FSMContext, Bot
from utils.imports import Router
from utils.helpers import createPosterButtons

logger = logging.getLogger(__name__)


command_router = Router()


@command_router.message(Command("start"))
async def start(message: Message, state: FSMContext, command: CommandObject, bot: Bot):
    makup = createPosterButtons()
    if message.from_user.id == 370504153:
        await bot.send_message(
            message.from_user.id, "Choose Poster", reply_markup=makup
        )