from src.application.routes.object_values.url_path import UrlPath
from src.application.routes.auth_routes import AuthenticateClientRoute
from src.application.routes.client_routes import ClientRoute

url_pattern = [
    UrlPath(path="/auth", view=AuthenticateClientRoute, name="authenticate_client"),
    UrlPath(path="/client", view=ClientRoute, name="create_client"),
]
