import logging
from utils.imports import BaseMiddleware, Message
from typing import Callable, Dict, Any, Awaitable
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramConflictError,
    TelegramEntityTooLarge,
    TelegramForbiddenError,
    TelegramMigrateToChat,
    TelegramNetworkError,
    TelegramNotFound,
    TelegramRetryAfter,
    TelegramServerError,
    TelegramUnauthorizedError,
)

logger = logging.getLogger(__name__)


class ExceptionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any],
    ) -> Any:
        try:
            return await handler(event, data)
        except TelegramBadRequest as e:
            logging.error(f"Bad Request: {e}")
        except TelegramConflictError as e:
            logging.error(f"Conflict Error: {e}")
        except TelegramEntityTooLarge as e:
            logging.error(f"Entity Too Large: {e}")
        except TelegramForbiddenError as e:
            logging.error(f"Forbidden Error: {e}")
        except TelegramMigrateToChat as e:
            logging.info(f"Chat migrated: {e}")
            # Handle migration, e.g., update chat ID in database
        except TelegramNetworkError as e:
            logging.error(f"Network Error: {e}")
        except TelegramNotFound as e:
            logging.error(f"Not Found: {e}")
        except TelegramRetryAfter as e:
            logging.warning(f"Retry After: {e}")
            # Handle retry logic
        except TelegramServerError as e:
            logging.error(f"Server Error: {e}")
        except TelegramUnauthorizedError as e:
            logging.critical(f"Unauthorized Error: {e}")
            # Handle unauthorized error, e.g., check bot token
        except Exception as e:
            logging.exception(f"Unexpected error: {e}")
