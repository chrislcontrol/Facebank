from src.infra.helpers.url_path import UrlPath
from src.main.routes.auth_routes import AuthenticateClientRoute
from src.main.routes.client_routes import ClientRoute

url_pattern = [
    UrlPath(path="/auth", view=AuthenticateClientRoute, name="authenticate_client"),
    UrlPath(path="/client", view=ClientRoute, name="create_client"),
]
