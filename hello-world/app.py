from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.request import Request
import logging


def show_users_controller(request: Request):
    """
    The controller must accept a `request` and return a `response`.
    """
    print("Incoming request: " + str(request))
    return Response("<body><h1>Users: [potato]</h1></body>")


def user_routes(config: Configurator):
    """
    Routes are used to, well, create the routes and
    link them to their controllers (called views in this 💩 framework).
    """
    config.add_route("show_users", "/show")  # /users/show
    config.add_view(show_users_controller, route_name="show_users")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(asctime)s] %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )

    # Docs for pyramid: https://docs.pylonsproject.org/projects/pyramid/en/latest/api/config.html
    with Configurator() as config:
        config.include(user_routes, route_prefix="/users")
        app = config.make_wsgi_app()
    serve(app, host="0.0.0.0", port=1234)
