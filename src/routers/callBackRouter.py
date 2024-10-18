import logging
from utils.imports import CallbackQuery, FSMContext, Router, Bot
from utils.helpers import make_post
from utils.domain import KeyboardConfig, CustomUrlButton
from filters.posterCallback import PosterCallBack
from utils.consts import (
    text1,
    text2,
    text3,
    text4,
    photo1,
    photo2,
    photo3,
    photo4,
    url,
    X,
    faq,
)

logger = logging.getLogger(__name__)


callback_router = Router()


@callback_router.callback_query(
    PosterCallBack.filter(),
)
async def poster(message: CallbackQuery, state: FSMContext, bot: Bot):
    user_choice = int(message.data.split(":")[1])

    config = KeyboardConfig(
        [
            CustomUrlButton("Registration", url),
            CustomUrlButton("FAQ", faq),
            CustomUrlButton("Follow X", X),
        ],
        [2, 1],
    )

    postArray = [
        {"t": text1, "p": photo1},
        {"t": text2, "p": photo2},
        {"t": text3, "p": photo3},
        {"t": text4, "p": photo4},
    ]
    await make_post(
        bot,
        -1002454474879,
        text=postArray[user_choice - 1]["t"],
        photo=postArray[user_choice - 1]["p"],
        keyboard_config=config,
    )
    # await make_post(
    #     bot,
    #     -1002445951772,
    #     text=postArray[user_choice - 1]["t"],
    #     photo=postArray[user_choice - 1]["p"],
    #     keyboard_config=config,
    # )
    await message.answer()
