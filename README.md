# Fastlify

Fastlify is a framework built around Flask for dealing with REST APIs

## Example app

```py
from fastlify import Fastlify
from fastlify.http.request import Request
from fastlify.http.response import Response
from fastlify.decorators.http import controller
from fastlify.controllers.http_controller import HTTPController

app = Fastlify.create()

@controller("/")
class HelloController(HTTPController):
	def get(request: Request) -> Response:
		return Response({
			"message": "Hello, world!"
		}, status=200)

app.register_controller(HelloController)

if __name__ == "__main__":
	app.listen(port=8081)
```

## Author

| ![Eder Lima](https://github.com/Nxrth-x.png?size=100) |
| ----------------------------------------------------- |
| [Eder Lima](https://github.com/Nxrth-x)               |
