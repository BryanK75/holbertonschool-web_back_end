#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Exclure la ligne d'en-tête

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # L'exemple tronque à 1000, mais ce n’est pas obligatoire
            # truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retourne un dictionnaire contenant une page de données basée sur un
        index, qui reste cohérente même si des lignes ont été supprimées.

        Args:
            index (int): L'index de départ (0-based) pour récupérer la page.
                         Doit être dans la plage valide.
            page_size (int): Le nombre d'éléments par page.

        Returns:
            Dict: Un dictionnaire avec les clés suivantes:
                - index (int): L'index actuel de départ de la page
                - next_index (int):
                  L'index suivant à interroger pour la page suivante
                - page_size (int): Le nombre d'éléments réellement retournés
                - data (List[List]): Les données de la page courante
        """
        assert isinstance(page, int) and page > 0, (
            "page must be a positive integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be a positive integer"
        )

        indexed_data = self.indexed_dataset()
        data_length = len(indexed_data)

        # Vérifie que l'index est dans la plage
        # Si index >= data_length, on lève une AssertionError
        assert index < data_length, "Index out of range"

        data = []
        current_index = index

        # Parcourir les index à partir de 'index' et récupérer 'page_size'
        # items existants
        while len(data) < page_size and current_index < data_length:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
            current_index += 1

        # current_index est maintenant l'index du prochain élément à récupérer
        # après cette page. Même si des éléments ont été supprimés, on avance
        # jusqu'au prochain index non vérifié.
        next_index = current_index

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index,
        }
