#!/usr/bin/env python3
"""
Ce module définit une coroutine measure_runtime qui exécute
async_comprehension quatre fois en parallèle, mesure le temps total
d'exécution, et le retourne. En exécutant les quatre tâches simultanément,
le temps total reste d'environ 10 secondes, car chaque async_comprehension
attend 10 fois 1 seconde (soit environ 10 secondes au total), et ce délai
n'est pas raccourci par la mise en parallèle (les 4 coroutines attendent
chacune leurs 10 secondes en même temps).
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Exécute async_comprehension quatre fois en parallèle à l'aide de
    asyncio.gather, mesure et retourne le temps total d'exécution.

    Retourne:
        float: Le temps total en secondes.
    """
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    return end - start
