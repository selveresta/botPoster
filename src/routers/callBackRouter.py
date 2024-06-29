import logging
from utils.imports import CallbackQuery, FSMContext
from utils.imports import Router

logger = logging.getLogger(__name__)


callback_router = Router()


@callback_router.callback_query()
def start(message: CallbackQuery, state: FSMContext):
    print("Callback Query")
