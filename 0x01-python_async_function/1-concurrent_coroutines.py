#!/usr/bin/env python3
"""
Async routine with 2 args
"""
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spaw wait random n times)"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    delay = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))

    return sorted(delay)
