#!/usr/bin/env python3
"""
Func to measure execution time
"""
import asyncio
import time


def measure_time(n: int, max_delay: int) -> float:
    """
    measures total exection time returnsag time aken
    """

    """wait_n;"""
    start = time.time()
    asyncio.run(__import__('1-concurrent_coroutines').wait_n(n, max_delay))
    end = time.time()
    total = end - start
    return (total)/n
