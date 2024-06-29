import logging

from utils.imports import BaseMiddleware, Message
from typing import Callable, Dict, Any, Awaitable
from config import IS_GROUP_BOT

logger = logging.getLogger(__name__)


class ChatTypeMiddleware(BaseMiddleware):
    def __init__(self):
        self.handle_groups = IS_GROUP_BOT
        super().__init__()

    async def __call__(
        self,
        handler: Callable[[Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        is_private = event.chat.type == "private"
        is_group = event.chat.type in ["group", "supergroup"]

        data["is_private"] = is_private
        data["is_group"] = is_group

        if is_group and not self.handle_groups:
            data["cancel_handler"] = True
            return

        return await handler(event, data)
