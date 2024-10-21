#!/usr/bin/env python3
"""
Get a value from a dictionary returning a default if the key is not found
"""
from typing import Mapping, Any, TypeVar, Union,  Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dict
    """
    if key in dct:
        return dct[key]
    else:
        return default
