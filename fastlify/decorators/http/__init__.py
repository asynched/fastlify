from typing import Callable
from fastlify.interfaces.http import AbstractHTTPController

DecoratedFunctionType = Callable[[Callable], Callable]


def controller(endpoint: str) -> Callable[[type], AbstractHTTPController]:
    def decorated(controller_class: type) -> AbstractHTTPController:
        instance: AbstractHTTPController = controller_class()
        instance.__endpoint__ = endpoint

        return instance

    return decorated


def route(endpoint: str, method: str = None) -> DecoratedFunctionType:
    def decorated(function: Callable) -> Callable:
        nonlocal method
        if not method:
            method = function.__name__

        setattr(function, '__endpoint__', endpoint)
        setattr(function, '__method__', method)
        return function

    return decorated


def generic_route_decorator(method: str, endpoint: str) -> DecoratedFunctionType:
    def decorated(function: Callable) -> Callable:
        setattr(function, '__endpoint__', endpoint)
        setattr(function, '__method__', method)
        return function

    return decorated


def generate_generic_handler(method: str, endpoint: str) -> DecoratedFunctionType:
    def decorate(function) -> Callable:
        return generic_route_decorator(method, endpoint)(function)

    return decorate


def get(endpoint: str):
    return generate_generic_handler('get', endpoint)


def post(endpoint: str):
    return generate_generic_handler('post', endpoint)


def put(endpoint: str):
    return generate_generic_handler('put', endpoint)


def patch(endpoint: str):
    return generate_generic_handler('patch', endpoint)


def delete(endpoint: str):
    return generate_generic_handler('delete', endpoint)
