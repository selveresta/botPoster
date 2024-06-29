import logging
from utils.imports import Command, Message, CommandObject, FSMContext
from utils.imports import Router

logger = logging.getLogger(__name__)


command_router = Router()


@command_router.message(Command("start"))
def start(message: Message, state: FSMContext, command: CommandObject):
    print("Start Command")


@command_router.message(Command("help"))
def help(message: Message, state: FSMContext):
    print("Start Command")
