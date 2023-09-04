from rest_framework import status

from config.common.base.exception import BaseAPIException


class UnknownServerException(BaseAPIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = "Internal server error"
    code = 1001
