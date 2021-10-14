from fastlify.http.status import Status
from fastlify.http.request import Request
from fastlify.http.response import Response
from fastlify.decorators.http import controller, get
from fastlify.controllers.http_controller import HTTPController
from fastlify.controllers.generic_http_controller import GenericHTTPController


@controller('/')
class HelloController(HTTPController):
    def get(request: Request) -> Response:
        return Response({'message': 'Hello, world!'}, status=Status.OK)


@controller('/test')
class TestController(GenericHTTPController):
    @get('/message')
    def get_test_message(request: Request) -> Response:
        return Response(
            {
                'message': 'Hello, world!',
            },
            status=Status.IM_A_TEAPOT,
        )
