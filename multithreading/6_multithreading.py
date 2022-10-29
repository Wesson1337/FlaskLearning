import asyncio
import logging
import multiprocessing
import time
from multiprocessing.pool import ThreadPool
from aiohttp import ClientSession

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

INPUT_VALUES = [
    'https://yakitoriya.ru'
] * 200


def task(url: str):
    response = requests.get(url, timeout=(5, 5))
    return response.status_code


async def async_task(url: str):
    async with ClientSession() as session:
        async with session.get(url=url) as response:
            return response.status


def task_execution_with_threadpool():
    pool = ThreadPool(processes=8)
    start = time.time()
    result = pool.map(task, INPUT_VALUES)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Time taken in seconds with threadpool - {end - start}')
    logger.info(result)


def sequential_approach():
    start = time.time()
    result = []
    for inp in INPUT_VALUES:
        result.append(task(inp))
    end = time.time()
    logger.info(f'Time taken in seconds with sequential approach - {end - start}')
    logger.info(result)


def task_execution_with_processpool():
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    start = time.time()
    result = pool.map(task, INPUT_VALUES)
    pool.close()
    pool.join()
    end = time.time()
    logger.info(f'Time taken in seconds with process pool - {end - start}')
    logger.info(result)


async def task_execution_with_async():
    start = time.time()
    tasks = []
    for inp in INPUT_VALUES:
        tasks.append(asyncio.create_task(async_task(inp)))

    results = await asyncio.gather(*tasks)

    end = time.time()

    logger.info(f'Time taken in seconds with async - {end - start}')
    logger.info(results)

if __name__ == '__main__':
    # sequential_approach()
    # task_execution_with_threadpool()
    # task_execution_with_processpool()
    asyncio.run(task_execution_with_async())
