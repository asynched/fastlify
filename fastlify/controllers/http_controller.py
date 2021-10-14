from fastlify.http.request import Request
from fastlify.http.response import Response
from fastlify.interfaces.http import AbstractHTTPController


class HTTPController(AbstractHTTPController):
    def get(request: Request) -> Response:
        return HTTPController._default_handler(request)

    def post(request: Request) -> Response:
        return HTTPController._default_handler(request)

    def patch(request: Request) -> Response:
        return HTTPController._default_handler(request)

    def put(request: Request) -> Response:
        return HTTPController._default_handler(request)

    def delete(request: Request) -> Response:
        return HTTPController._default_handler(request)
