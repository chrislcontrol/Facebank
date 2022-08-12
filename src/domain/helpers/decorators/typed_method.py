from typing import Callable, Any, List, Tuple

from src.domain.exceptions.invalid_input import InvalidInput
from src.domain.types.value_object import ValueObject


def validate_annotations(annotations: dict, *args, **kwargs) -> Tuple[Tuple, dict]:
    if args:
        raise TypeError('Positional arguments not allowed.')

    wrong_fields = []
    for arg, value in kwargs.copy().items():
        expected_type = annotations.get(arg)

        if not expected_type:
            raise TypeError(f"Parameter {arg} missing typing annotation.")

        if isinstance(value, ValueObject):
            kwargs[arg] = value.validate()

        elif expected_type != Any:
            if not isinstance(value, expected_type):
                wrong_fields.append({"field": arg, "description": f"Expected {expected_type.__qualname__.upper()} "
                                                                  f"but {value.__class__.__name__.upper()} "
                                                                  f"was provided."})

    if wrong_fields:
        raise TypeError(wrong_fields)

    return args, kwargs


def typed_method(func) -> Callable:
    annotations = func.__annotations__

    def return_func(*args, **kwargs):
        _, new_kwargs = validate_annotations(annotations=annotations, *args, **kwargs)
        return func(**new_kwargs)

    return return_func
