from src.presentation.base.schema.char_field import CharField
from src.presentation.base.schema.json_field import JSONField
from src.presentation.base.schema.schema import Schema


class CreateUserInputSchema(Schema):
    name = CharField(max_length=100)
    username = CharField(max_length=100)
    password = CharField(max_length=255)
    attributes = JSONField()
