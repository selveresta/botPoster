import os
from pathlib import Path
from utils.imports import (
    BotCommand,
    Bot,
    FSInputFile,
    InlineKeyboardBuilder,
    InlineKeyboardButton,
    ParseMode,
    InputFile,
)
from utils.domain import KeyboardConfig, CustomCallbackButton, CustomUrlButton
from filters.posterCallback import PosterCallBack


async def setup_bot_commands(bot: Bot):
    bot_commands = [
        BotCommand(command="/command", description="Description"),
    ]
    await bot.set_my_commands(bot_commands)


async def make_post(bot: Bot, chat_id, text, photo, keyboard_config: KeyboardConfig):

    markup = InlineCustomKeyboard(keyboard_config, True)
    img = FSInputBase(photo)

    if photo:
        if "mp4" in photo:
            video = FSInputBase(photo)
            await bot.send_video(
                chat_id, video, caption=text, reply_markup=markup, height=300
            )
            return
        await bot.send_photo(
            chat_id, img, caption=text, reply_markup=markup, parse_mode=ParseMode.HTML
        )
    else:
        await bot.send_message(chat_id, text, reply_markup=markup)


def FSInputBase(file_name):
    path = Path(__file__).parent.parent.joinpath(f"./assets/{file_name}")
    return FSInputFile(path)


def InlineCustomKeyboard(keyboard_config: KeyboardConfig, isUrl: bool = False):
    builder = InlineKeyboardBuilder()

    for i in keyboard_config.buttons:

        if isUrl:
            i.__class__ = CustomUrlButton
            builder.add(InlineKeyboardButton(text=i.text, url=i.url))
        else:
            i.__class__ = CustomCallbackButton

            builder.add(
                InlineKeyboardButton(text=i.text, callback_data=i.callbackFilter)
            )

    builder.adjust(*keyboard_config.adjust)

    return builder.as_markup()


def createPosterButtons():
    buttons = [
        CustomCallbackButton(f"poster{i}", filter=PosterCallBack(posterNum=i).pack())
        for i in range(1, 5)
    ]

    config: KeyboardConfig = KeyboardConfig(buttons, [2, 2])

    markup = InlineCustomKeyboard(config)
    return markup
