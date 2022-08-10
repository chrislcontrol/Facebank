from src.presenters.serializers.helpers.serializer import Serializer
from src.presenters.serializers.types import CharField


class AuthenticateClientSerializer(Serializer):
    username = CharField(max_length=255)
    password = CharField(max_length=255)
