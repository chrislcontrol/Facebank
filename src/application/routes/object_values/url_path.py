from dataclasses import dataclass


@dataclass
class UrlPath:
    path: str
    view: any
    name: str

    @property
    def view_func(self):
        return self.view.as_view(self.name)
