#!/usr/bin/env python3

import asyncio
import random

async def async_generator():
  """
  Async generator that yields random numbers 10 times with 1 second delay.
  """
  for _ in range(10):
    await asyncio.sleep(1)
    yield random.randint(0, 10)
