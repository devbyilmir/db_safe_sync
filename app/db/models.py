from dataclasses import dataclass
from typing import List


@dataclass
class ColumnSchema:
    name: str
    type: str


@dataclass
class TableSchema:
    name: str
    columns: List[ColumnSchema]
