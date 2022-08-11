from src.presentation.serializers.types.charfield import CharField
from src.presentation.serializers.types.serializer import Serializer


class RegisterClientSerializer(Serializer):
    username = CharField()
    password = CharField()
    email = CharField()
