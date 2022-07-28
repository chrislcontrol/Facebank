class HttpResponse:
    def __init__(self, status_code: int, body: any):
        self._status_code = status_code
        self._body = body

    @property
    def body(self) -> any:
        return self._body

    @property
    def status_code(self) -> int:
        return self._status_code

    def __repr__(self):
        return f"{self.__class__.__qualname__} (status_code={self._status_code}, body={self._body})"
