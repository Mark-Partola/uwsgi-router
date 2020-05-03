from bootstrap import app

@app.controller
class HomeController:
    def __init__(self):
        self._requests = 0

    @app.action(action='GET', path='/')
    def home(self):
        self._requests += 1
        return f'Home {self._requests}'


@app.controller
class TestController:
    def __init__(self):
        self._requests = 0

    @app.action(action='GET', path='/test')
    def test(self):
        self._requests += 1
        return f'Test {self._requests}'