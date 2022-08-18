import glob
import inspect
from os.path import dirname, join

from sqlalchemy.orm import DeclarativeMeta

import src

modules = glob.glob(join(dirname(__file__), "*.py"))
for module in modules:
    if module.endswith(".py"):
        module_without_full_path = f"{src.__name__}.{module.split(f'/{src.__name__}/')[-1][:-3].replace('/', '.')}"
        if not module_without_full_path.endswith("__init__"):
            model_module = __import__(module_without_full_path, fromlist=[None])
            for name, obj in inspect.getmembers(model_module):
                if inspect.isclass(obj) and hasattr(obj, '__tablename__') and isinstance(obj, DeclarativeMeta):
                    locals()[obj.__class__.__qualname__] = obj
