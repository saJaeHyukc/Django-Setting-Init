from typing import Optional

from rest_framework import status
from rest_framework.response import Response


def custom_response(
    data: Optional[dict] = None,
    code: Optional[int] = 0,
    message: Optional[str] = "Success",
    status_code: int = status.HTTP_200_OK,
    **kwargs,
) -> Response:
    json_data = dict()
    json_data["data"] = data or {}
    json_data["code"] = code
    json_data["message"] = message
    json_data["success"] = code == 0
    return Response(json_data, status=status_code, **kwargs)
