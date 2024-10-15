#!/usr/bin/env python3
"""
coroutine that will execute async_comprehension
four times in parallel using asyncio.gather
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the total runtime and return it."""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
