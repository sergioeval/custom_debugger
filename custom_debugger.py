from functools import wraps
import logging
from .custom_exception import FailedCustomException
from .log_templates import INFO_TEMPLATE, ERROR_TEMPLATE

# logger = logging.getLogger()


def custom_debugger(fn):
    logger = logging.getLogger(__name__)

    @wraps(fn)
    def inner(*args, **kwargs):
        """logg data"""
        try:
            # print(f"Function Executed OK: {fn.__qualname__}")
            # print(fn.__dir__())
            logger.info(INFO_TEMPLATE.format(
                fn_name=fn.__qualname__,
                fn_file_name=fn.__code__.co_filename))

            return fn(*args, **kwargs)
        except Exception as e:
            logger.error(ERROR_TEMPLATE.format(
                fn_name=fn.__qualname__,
                fn_file_name=fn.__code__.co_filename,
                error=e
            ))
            raise FailedCustomException(
                message=f"EXCEPTION RAISED BY THIS EXCEPTION: {e}")

    return inner
