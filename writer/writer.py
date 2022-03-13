import asyncio

import aiofiles
import os
from datetime import datetime, timezone


async def write(data: tuple, file_name: str):
    # if os.path.exists(file_name):
    async with aiofiles.open(file_name, mode="a") as f:
        await f.write(preprocess(data))


def preprocess(data):
    return f"{datetime.fromtimestamp(int(data[0])/1000.0, tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')}," \
           f"{data[1]}," \
           f"{','.join(data[2])}," \
           f"{','.join(data[3])}\n"


def FactoryCSVWriter():
    return write