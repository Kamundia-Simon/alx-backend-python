#!/usr/bin/env python3
"""
Return asynciotask
"""
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """using async syntax"""
    wait_random = __import__('0-basic_async_syntax').wait_random
    return asyncio.create_task(wait_random(max_delay))
