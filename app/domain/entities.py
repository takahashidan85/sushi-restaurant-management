from dataclasses import dataclass
from typing import List

@dataclass
class MenuItemEntity:
    id: int = None
    name: str = ""
    price: float = 0.0
    category: str = ""
