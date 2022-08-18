from src.presentation.base.schema.char_field import CharField
from src.presentation.base.schema.schema import Schema


class RegisterClientInputSchema(Schema):
    username = CharField()
    password = CharField()
    email = CharField()
