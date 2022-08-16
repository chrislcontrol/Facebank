from src.infra.adapters.sql_alchemy.models.client import ClientDB
from src.infra.adapters.sql_alchemy.models.token import TokenDB
from src.infra.adapters.sql_alchemy.models.user import UserDB

models = [
    ClientDB,
    TokenDB,
    UserDB
]
