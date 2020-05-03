from lib.exceptions.route_not_found_exception import RouteNotFoundException
from bootstrap import bootstrap
from controllers.controllers import HomeController, TestController

def application(env, start_response):
    try:
        response = bootstrap(env)

        start_response('200 OK', [('Content-Type', 'text/html')])

        return bytes(response, 'utf-8')
    except RouteNotFoundException:
        start_response('404 Not Found', [('Content-Type', 'text/html')])
