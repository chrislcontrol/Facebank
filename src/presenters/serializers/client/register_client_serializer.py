from src.presenters.serializers.helpers.serializer import Serializer
from src.presenters.serializers.types import CharField


class RegisterClientSerializer(Serializer):
    username = CharField()
    password = CharField()
    email = CharField()
