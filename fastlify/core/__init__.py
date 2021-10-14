from flask import Flask, request
from functools import wraps
from uuid import uuid4
from fastlify.controllers.http_controller import HTTPController
from fastlify.interfaces.http import AbstractHTTPController


class Fastlify(Flask):
    HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete']

    @classmethod
    def create(cls, context: str = __name__):
        return cls(context)

    def listen(self, host: str = '0.0.0.0', port: int = 779, debug=False):
        self.run(host, port, debug)

    def register_controller(self, controller: AbstractHTTPController):
        if issubclass(type(controller), HTTPController):
            self.register_http_controller(controller)
            return

        self.register_generic_http_controller(controller)

    def register_generic_http_controller(self, controller: AbstractHTTPController):
        methods = [method for method in dir(controller) if not method.startswith('_')]
        controller_endpoint: str = controller.__endpoint__

        for method in methods:
            controller_handler_function = getattr(controller, method)
            controller_http_method = getattr(controller_handler_function, '__method__')
            controller_method_endpoint: str = getattr(
                controller_handler_function, '__endpoint__', ''
            )
            controller_method_full_url: str = (
                controller_endpoint + controller_method_endpoint
            )

            application_method_handler = getattr(self, controller_http_method)

            server_endpoint_handler = application_method_handler(
                controller_method_full_url
            )
            server_endpoint_handler(
                Fastlify.curry(
                    controller_handler_function.__func__,
                    request,
                )
            )

    def register_http_controller(self, controller: AbstractHTTPController):
        controller_endpoint: str = controller.__endpoint__

        for method in self.HTTP_METHODS:
            controller_handler_function = getattr(controller, method)
            controller_method_endpoint: str = getattr(
                controller_handler_function, '__endpoint__', ''
            )
            controller_method_full_url: str = (
                controller_endpoint + controller_method_endpoint
            )

            application_method_handler = getattr(self, method)

            server_endpoint_handler = application_method_handler(
                controller_method_full_url
            )
            server_endpoint_handler(
                Fastlify.curry(
                    controller_handler_function.__func__,
                    request,
                )
            )

    def curry(callback, *args, **kwargs):
        @wraps(callback)
        def decorated():
            return callback(*args, **kwargs)

        decorated.__name__ = str(uuid4())
        return decorated
