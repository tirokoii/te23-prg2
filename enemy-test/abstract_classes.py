from abc import ABC, abstractmethod
from typing import List

class Item:
    @abstractmethod
    
    def __init__(self):
        pass

class Inventory:
    def __init__(self):
        self.contents = []

    def get_content(self):
        self.contents: List[Item] = []