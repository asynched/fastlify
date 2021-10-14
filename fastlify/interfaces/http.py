from abc import ABC
from fastlify.types import Request, Response
from fastlify.http.status import Status


class AbstractHTTPController(ABC):
    __endpoint__: str = None

    def _default_handler(request: Request) -> Response:
        return Response({'message': 'Method unavailable'}, status=Status.BAD_REQUEST)
