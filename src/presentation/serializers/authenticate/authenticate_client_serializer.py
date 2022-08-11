from src.presentation.serializers.types.charfield import CharField
from src.presentation.serializers.types.serializer import Serializer


class AuthenticateClientSerializer(Serializer):
    username = CharField(max_length=255)
    password = CharField(max_length=255)
