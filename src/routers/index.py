from utils.imports import Dispatcher
from .commandRouter import command_router
from middlewares.ChatTypeMiddleware import ChatTypeMiddleware
from middlewares.ExceptionMiddleware import ExceptionMiddleware

routers = [command_router]


def register_routers(dp: Dispatcher):
    for rout in routers:
        rout.message.middleware(ChatTypeMiddleware())
        rout.message.middleware(ExceptionMiddleware())

        dp.include_router(rout)
