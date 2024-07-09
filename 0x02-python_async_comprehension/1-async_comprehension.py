#!/usr/bin/env python3

import asyncio
from random import randint  # Import for generating random numbers


async def async_generator():
    """
    Asynchronous generator that yields random numbers 10 times with 1 second delay.

    Yields:
        int: A random integer between 0 and 10 (inclusive).
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield randint(0, 10)

async def async_comprehension():
    """
    Asynchronous coroutine that collects 10 random numbers using async comprehension.

    Returns:
        list[int]: A list of 10 random integers between 0 and 10 (inclusive).
    """
    return [async_number async for async_number in async_generator()]

