import logging
from typing import Any

from rest_framework import exceptions, status
from rest_framework.response import Response

logger = logging.basicConfig(filemode="")


def success_response(
    data: Any,
    message: str = "Request was successful",
    status_code: int = status.HTTP_200_OK,
) -> Response:
    response_data = {
        "success": "true",
        "message": message,
        "data": data,
    }

    return Response(data=response_data, status=status_code)


def error_response(
    error: Any,
    message: str = "Request failed",
    status_code: int = status.HTTP_400_BAD_REQUEST,
) -> Response:
    response_data = {"message": message, "code": "error", "details": None}

    if isinstance(error, exceptions.APIException):
        response_data["code"] = error.code or error.default_code

        if isinstance(error.detail, (dict, list)):
            response_data["message"] = error.default_detail
            response_data["details"] = error.detail
        else:
            response_data["message"] = str(error.detail)

    elif isinstance(error, exceptions.ErrorDetail):
        response_data["message"] = str(error)
        response_data["code"] = error.code

    elif isinstance(error, dict):
        if "message" in error or "code" in error:
            response_data["message"] = error.get("message", response_data["message"])
            response_data["code"] = error.get("code", response_data["code"])
            details = {k: v for k, v in error.items() if k not in ["message", "code"]}
            response_data["details"] = details or None
        else:
            response_data["message"] = "Validation error"
            response_data["code"] = "invalid"
            response_data["details"] = error

    else:
        error_message = str(error) if not message else message
        response_data["message"] = error_message
        response_data["code"] = "error"

    if not response_data["details"]:
        del response_data["details"]

    return Response(response_data, status=status_code)
