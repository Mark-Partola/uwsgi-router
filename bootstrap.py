from lib.app import App

app = App()

def bootstrap(env):
    return app.run(
        action=env.get('REQUEST_METHOD'),
        path=env.get('REQUEST_URI')
    )
