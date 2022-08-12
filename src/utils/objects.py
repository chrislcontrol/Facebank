def serialize_object(obj) -> dict:
    return {key: value for key, value in vars(obj).items() if not key.startswith('_')}
