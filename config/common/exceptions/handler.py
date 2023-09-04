from datetime import datetime
from typing import Optional

from rest_framework.exceptions import APIException
from rest_framework.response import Response

from config.common.base.exception import BaseAPIException
from config.common.base.response import custom_response
from config.common.exceptions.exceptions import UnknownServerException
from config.settings.base import logger


def default_exception_handler(exc: Exception, context: dict) -> Response:
    logger.error("[EXCEPTION_HANDLER]")
    logger.error(f"[{datetime.now()}]")
    logger.error("> exc")
    logger.error(f"{exc}")
    logger.error("> context")
    logger.error(f"{context}")

    response = handle_api_exception(exc, context)

    if response:
        return response

    # TODO: 슬랙 모니터링 채널에 오류 리포트
    return handle_api_exception(UnknownServerException(), context)


def handle_api_exception(exc: Exception, context: dict) -> Optional[Response]:
    if not isinstance(exc, APIException):
        return None

    message = getattr(exc, "detail")
    status_code = getattr(exc, "status_code")
    code = getattr(exc, "code", BaseAPIException.code)

    return custom_response(code=code, message=message, status_code=status_code)
