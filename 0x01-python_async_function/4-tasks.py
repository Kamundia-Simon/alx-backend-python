#!/usr/bin/env python3
"""
Modified wait_n function)
"""
import asyncio
from typing import List


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    function body
    """
    task_wait_random = __import__('3-tasks').task_wait_random
    delay = await asyncio.gather(*[task_wait_random(max_delay)
                                   for _ in range(n)])
    return sorted(delay)
