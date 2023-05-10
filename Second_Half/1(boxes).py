from abc import ABC, abstractmethod
from typing import List, Dict

class Box(ABC):
    storage:None

    @abstractmethod
    def add():
        pass
    @abstractmethod
    def empty():
        pass

class Item():
    name:str
    value:int

    def __init__(self,name:str,value:int) -> None:
        self.name=name
        self.values=value

class ListBox(Box):
    storage:List

    def __init__(self):
        self.storage=[]
    def add(self,*items):
        self.storage.extend(items)
    def empty(self):
        self.storage.clear()

class DictBox(Box):
    storage:Dict
    counter:int

    def __init__(self):
        self.storage={}
        self.counter=0
    def add(self,*items):
        for item in items:
            self.storage.update(str(self.counter),item)
            self.counter+=1
    def empty(self):
        self.storage.clear()

def repack_boxes(*boxes:tuple(Box)):
    all_items=[]
    
    for b in boxes:
        if isinstance(b.storage,dict):
            all_items.extend(b.storage.values())
        else:
            all_items.extend(b.storage)
        b.empty()
    
    for _ in len(boxes):
        quantity=len(boxes)
        items_quant=len(all_items)
        b=boxes.pop(0)
        b.add([all_items.pop(0) for _ in range(items_quant//quantity)])

