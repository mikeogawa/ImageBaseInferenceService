from dataclasses import fields
from typing import Any, Dict


class Dict2Obj:

    def __init__(self, dict_val: Dict[str, Any]):
        for k, v in dict_val.items():
            setattr(self, k, v)

    def convert_to(self, domain_class, **additional) -> Any:
        names = [f.name for f in fields(domain_class)]
        default_value = {f.name: f.default for f in fields(domain_class)}
        init_dict = {**{n: getattr(self, n, default_value[n]) for n in names}, **additional}

        return domain_class(**init_dict)
