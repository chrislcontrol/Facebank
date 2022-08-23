from typing import List


class HttpMethods:
    GET = 'get'
    HEAD = 'head'
    POST = 'post'
    PUT = 'put'
    DELETE = 'delete'
    CONNECT = 'connect'
    OPTIONS = 'options'
    TRACE = 'trace'

    @classmethod
    def all(cls) -> List[str]:
        return [value for key, value in vars(cls).items() if not key.startswith('_')]
