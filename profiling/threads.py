from typing import Any
from pyinstrument import Profiler
import threading
import concurrent.futures
import httpx
import time
import random


URLS = [
        'https://pokeapi.co/api/v2/pokemon/ditto',
        'https://pokeapi.co/api/v2/pokemon/aegislash',
        'https://pokeapi.co/api/v2/pokemon/pikachu', 
        'https://pokeapi.co/api/v2/pokemon/mewtwo',
        'https://pokeapi.co/api/v2/pokemon/onix'
]


def thread_initializer() -> None:
    print('[INFO]: thread started')


def batch_job(url: str) -> Any:
    print('[INFO]: starting job ...')
    client = httpx.Client()
    if random.choice([1, 3]) == 1:
        time.sleep(10)
    return client.get(url)


def execute_task() -> None:
    profiler = Profiler()
    profiler.start()
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(URLS), 
                                               initializer=thread_initializer) as executor:
        futures = [executor.submit(batch_job, url) for url in URLS]
        for f in concurrent.futures.as_completed(futures):
            try:
                response = f.result()
                print(f'[INFO]: Job finalized. Result was: {response}')
            except Exception as ex:
                print(f'[ERROR]: Error in job: {str(ex.args)}')
    profiler.stop()
    profiler.print()
                  


