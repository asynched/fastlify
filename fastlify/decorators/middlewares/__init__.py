from flask import request
from fastlify.middlewares.http import AbstractHTTPMiddleware

def middleware(function):
    def decorated():
        return function(request)
    
    return decorated

def class_middleware(base_class: type):
    instance: AbstractHTTPMiddleware = base_class()
    return instance.handle.__func__
