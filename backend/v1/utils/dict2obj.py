from dataclasses import fields
from typing import Any, Dict


class Dict2Obj:

    def __init__(self, dict_val: Dict[str, Any]):
        for k, v in dict_val.items():
            setattr(self, k, v)

    def convert_to(self, domain_class, **additional) -> Any:
        names = [f.name for f in fields(domain_class)]

        return domain_class(**{getattr(self, n) for n in names}, **additional)
