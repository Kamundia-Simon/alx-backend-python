#!/usr/bin/env python3
"""
a coroutine called async_comprehension that takes no arguments."""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension(): -> List[float]
    """Collects 10 random numbers asynchronously using async comprehension"""
    return [num async for num in async_generator()]
