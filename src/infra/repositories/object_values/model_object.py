class ModelObject:
    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
