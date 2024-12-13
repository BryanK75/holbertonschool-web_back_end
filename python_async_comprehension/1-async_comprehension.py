#!/usr/bin/env python3
"""
Ce module définit une coroutine async_comprehension qui utilise une
compréhension asynchrone pour collecter 10 nombres aléatoires fournis
par async_generator, puis les retourne sous forme de liste.
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine asynchrone qui collecte 10 nombres aléatoires générés par
    async_generator, en utilisant une compréhension asynchrone, puis
    retourne la liste de ces 10 valeurs.

    Retourne:
        List[float]: Liste des 10 nombres aléatoires.
    """
    return [i async for i in async_generator()]
