import json
from typing import Optional, Tuple

from flask import current_app


def read_json(filename: str, encoding: str = "utf-8"):
    with open(filename, encoding=encoding) as f:
        return json.load(f)


def get_limit_and_offset(page: Optional[int] = None) -> Tuple[int, int]:
    limit = current_app.config["ITEMS_PER_PAGE"]
    page = page if isinstance(page, int) else 1
    offset = 0 if page < 1 else limit * (page - 1)
    return limit, offset
