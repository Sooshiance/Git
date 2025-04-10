import logging
from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import exceptions, status
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError, OperationalError
from django.conf import settings

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    custom_response_data = {
        "message": "An error occurred",
        "code": "error",
        "details": None,
    }
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    if response is not None:
        status_code = response.status_code
        if isinstance(exc, exceptions.APIException):
            custom_response_data.update(
                {
                    "message": exc.default_detail,
                    "code": exc.default_code,
                    "details": exc.detail,
                }
            )
        else:
            custom_response_data.update(
                {"message": str(exc), "code": "client_error", "details": None}
            )
    else:
        if isinstance(exc, Http404):
            status_code = status.HTTP_404_NOT_FOUND
            custom_response_data.update(
                {"message": "Resource not found", "code": "not_found"}
            )
        elif isinstance(exc, PermissionDenied):
            status_code = status.HTTP_403_FORBIDDEN
            custom_response_data.update(
                {"message": "Permission denied", "code": "permission_denied"}
            )
        elif isinstance(exc, IntegrityError):
            status_code = status.HTTP_400_BAD_REQUEST
            custom_response_data.update(
                {"message": "Database integrity error", "code": "integrity_error"}
            )
        elif isinstance(exc, OperationalError):
            status_code = status.HTTP_503_SERVICE_UNAVAILABLE
            custom_response_data.update(
                {"message": "Database connection error", "code": "database_unavailable"}
            )
        else:
            logger.error("Unhandled exception", exc_info=True)
            custom_response_data.update(
                {"message": "Internal server error", "code": "server_error"}
            )

    if settings.DEBUG and status_code >= 500:
        custom_response_data["details"] = str(exc)
    elif 400 <= status_code < 500:
        if (
            "details" not in custom_response_data
            or custom_response_data["details"] is None
        ):
            custom_response_data["details"] = str(exc) if settings.DEBUG else None

    if custom_response_data["details"] is None:
        del custom_response_data["details"]

    return Response(custom_response_data, status=status_code)
