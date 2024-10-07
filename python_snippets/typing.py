"""
Typing helpers and type aliases for internal and external use.
"""

from typing import TypeAlias

# JSON type aliases inspired by:
# https://github.com/python/typing/issues/182#issuecomment-1320974824

Json: TypeAlias = "JsonDict | JsonList | str | int | float | bool | None"
"""Python representation of a JSON structure."""

JsonDict: TypeAlias = dict[str, "Json"]
"""Python representation of a JSON object."""

JsonList: TypeAlias = list["Json"]
"""Python representation of a JSON list."""
