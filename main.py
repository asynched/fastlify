from fastlify import Fastlify
from controllers import HelloController, TestController
from middlewares import AuthMiddleware

app = Fastlify.create()

app.register_middleware(AuthMiddleware)

app.register_controller(HelloController)
app.register_controller(TestController)

if __name__ == '__main__':
    app.listen(port=8081, debug=False)
