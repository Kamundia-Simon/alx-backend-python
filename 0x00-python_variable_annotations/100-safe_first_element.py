#!/usr/bin/env python3
"""
Returns the first element of a sequence if it exists & None if false
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    duck-typed annotations
    """
    if lst:
        return lst[0]
    else:
        return None
