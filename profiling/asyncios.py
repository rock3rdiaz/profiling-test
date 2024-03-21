from typing import Any
import asyncio
import cProfile, pstats, io
from pstats import SortKey
import concurrent.futures
import math
import time

PRIMES = [
        1122725350952931987612435,
        1125827059421719098712651,
        1122725350952932819019823,
        1152800951907733909812564,
        1157978480770999823467182,
        1099726899285419890012871
]


async def is_prime(n: int) -> bool:
    print(f'[INFO]: processing number {n}')
    if n < 2:
        return False
    if n == 2:
        return True
    await asyncio.sleep(3)
    if n % 2 == 0:
        return False
    return True


async def batch_job(number: int) -> Any:
    print('[INFO]: starting job ...')
    return is_prime(number)


async def execute_task() -> None:
    profiler = cProfile.Profile()
    profiler.enable()
    try:
        response = await asyncio.gather(*[is_prime(p) for p in PRIMES])
        print(f'[INFO]: Job finalized. Result was: {response}')
    except Exception as ex:
        print(f'[ERROR]: Error in job: {str(ex.args)}')
    profiler.disable()

    # criteria en los resultados
    s = pstats.Stats(profiler)
    
    # odenado por tiempo gastado y acumulado
    #s.sort_stats(SortKey.TIME, SortKey.CUMULATIVE).print_stats(10)
    
    # por tiempo acumulado (incluye las subfunciones)
    s.sort_stats(SortKey.CUMULATIVE).print_stats(10)
    
    # por nombre de archivo
    #s.split_dirs().sort_stats(SortKey.FILENAME).print_stats()
    
    # imprime los datos by default
    #profiler.print_stats()
                    
    #s.print_callees()

