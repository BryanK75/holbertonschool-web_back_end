#!/usr/bin/env python3
"""
Ce module définit une coroutine asynchrone async_generator qui génère
10 nombres aléatoires compris entre 0 et 10, en attendant 1 seconde
entre chaque génération.
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine asynchrone qui génère 10 nombres aléatoires compris
    entre 0 et 10.
    Pour chaque nombre :
    - Attendre 1 seconde de manière asynchrone.
    - Produire (yield) le nombre aléatoire généré.

    Retourne:
        AsyncGenerator[float, None]: Générateur asynchrone de
        10 nombres aléatoires.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
