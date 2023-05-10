from abc import ABC, abstractmethod
from typing import List, Dict
from random import randint
from dataclasses import dataclass

def main():
    
    class Box(ABC):
        storage:None

        @abstractmethod
        def add():
            pass
        @abstractmethod
        def empty():
            pass
    
    @dataclass
    class Item:
        name:str
        value:int

    class ListBox(Box):
        storage:List

        def __init__(self):
            self.storage=[]
        def add(self,*items:Item):
            if items:
                self.storage.extend(items)
        def empty(self):
            a=self.storage.copy()
            self.storage.clear()
            return a


    class DictBox(Box):
        storage:Dict
        counter:int

        def __init__(self):
            self.storage={}
            self.counter=1
        def add(self,*items:Item):
            
            #print(items, 1 if items else 0)
            if items:
                for item in items:
                    self.storage.update({str(self.counter):item})
                    self.counter+=1
        def empty(self):
            a=self.storage.copy()
            self.storage.clear()
            self.counter=1
            return a

    def repack_boxes(*boxes):
        all_items=[]
        boxes=list(boxes)
        if isinstance(boxes[0], list):
            boxes=list(*boxes[0])
        for b in boxes:
            if isinstance(b.storage,dict):
                all_items.extend(b.storage.values())
            else:
                all_items.extend(b.storage)
            b.empty()
        
        for _ in range(len(boxes)):
            quantity=len(boxes)
            items_quant=len(all_items)
            b=boxes.pop(0)
            b.add(*[all_items.pop(0) for _ in range(items_quant//quantity)])
    
    listboxlist=[ListBox() for _ in range(randint(1,15))]
    dictboxlist=[DictBox() for _ in range(randint(1,15))]
    itemlist=[Item(str(randint(1,100)),i) for i in range(randint(0,150))]
    #print(len)
    lists=listboxlist+dictboxlist
    #print(lists)
    
    for _ in range(len(lists)):
        current:Box
        current=lists.pop(0)
        curitems=[]
        if itemlist:
            for _ in range(randint(0,5)):
                if itemlist:
                    curitems.append(itemlist.pop(0))
            current.add(*curitems)
    
    lists=listboxlist+dictboxlist
    print(f'{len(lists)} boxes before sorting:')
    
    for _ in range(len(lists)):
        current:Box
        current=lists.pop(0)
        print(len(current.storage), end=' ')
    print()
    print()
    lists=listboxlist+dictboxlist
    print(f'{len(lists)} boxes after sorting:')
    repack_boxes(*lists)
    for i in range(len(lists)):
        """current:Box
        current=lists.pop(0)
        print(len(current.storage),end=' ')"""
        print(len(lists[i].empty()))
    




if __name__=="__main__":
    main()