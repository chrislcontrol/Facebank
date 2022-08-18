from src.presentation.base.schema.char_field import CharField
from src.presentation.base.schema.schema import Schema


class AuthenticateClientInputSchema(Schema):
    username = CharField(max_length=255)
    password = CharField(max_length=255)
