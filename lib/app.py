import functools
from .exceptions.route_not_found_exception import RouteNotFoundException


class App:
    def __init__(self):
        self._routes = {}
        self._raw_routes = []

    def controller(self, cl):
        for route in self._raw_routes:
            path = route.get('path')
            action = route.get('action')
            method = route.get('method')

            if path not in self._routes:
                self._routes[path] = {}

            self._routes[path][action] = {
                'method': method,
                'context': cl()
            }

        return cl

    def action(self, action, path):
        def decorate(fn):
            @functools.wraps(fn)
            def wrapper(self, *args, **kwargs):
                return fn(self, *args, **kwargs)

            self._raw_routes.append({
                'method': wrapper,
                'path': path,
                'action': action
            })

            return wrapper

        return decorate

    def run(self, action, path):
        routes = self._routes

        if path not in routes:
            raise RouteNotFoundException

        route = routes[path][action]

        return route.get('method')(route.get('context'))
