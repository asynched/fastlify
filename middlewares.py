from fastlify.decorators.middlewares import class_middleware
from fastlify.http.status import Status
from fastlify.http.request import Request
from fastlify.http.response import Response
from fastlify.middlewares.http import AbstractHTTPMiddleware

@class_middleware
class AuthMiddleware(AbstractHTTPMiddleware):
    def handle(request: Request) -> Response:
        return Response({
            'message': 'Error'
        }, status=Status.INTERNAL_SERVER_ERROR)
