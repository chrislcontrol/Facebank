class HttpRequest:
    def __init__(self, headers: dict = {}, body: dict = {}, params: dict = {}):
        self._headers = headers
        self._body = body
        self._params = params

    @property
    def headers(self) -> dict:
        return self._headers

    @property
    def body(self) -> dict:
        return self._body

    @property
    def params(self) -> dict:
        return self._params

    def __repr__(self):
        return (
            f"{self.__class__.__qualname__} (headers={self.headers}, body={self.body}, params={self.params})"
        )
