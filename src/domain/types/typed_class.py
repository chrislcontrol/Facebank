from src.domain.decorators.typed_method import typed_method, validate_annotations


class TypedClass:
    def __getattribute__(self, name):
        attr = object.__getattribute__(self, name)
        if not callable(attr):
            return attr

        return typed_method(attr)

    def __new__(cls, *args, **kwargs):
        validate_annotations(annotations=cls.__init__.__annotations__, *args, **kwargs)

        return super().__new__(cls)
