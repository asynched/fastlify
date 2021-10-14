from fastlify.http.request import Request
from fastlify.http.response import Response


class AbstractHTTPMiddleware:
    def handle(request: Request) -> Response:
        pass
