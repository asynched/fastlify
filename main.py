from fastlify import Fastlify
from controllers import HelloController, TestController

app = Fastlify.create()

app.register_controller(HelloController)
app.register_controller(TestController)

if __name__ == '__main__':
    app.listen(port=8081, debug=False)
