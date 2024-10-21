#!/usr/bin/env python3
"""
a type-annotated function that takes a float as and arg &
returns a function that multiplies a float
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda value: value * multiplier
