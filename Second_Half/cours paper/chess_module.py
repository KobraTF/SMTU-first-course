from abc import abstractmethod,ABC
from typing import Generator

# Интерфейс фигуры
class FigureBase(ABC):

    @abstractmethod
    def move_set(self,x:int, y:int, borderline:int) -> Generator[tuple[int,int],None,None]:
        pass
    @abstractmethod
    def __call__(self, x:int, y:int, borderline:int) -> Generator[tuple[int,int],None,None]:
        pass

# Класс фигуры, необходимый для просчитывания атаки
class Figure(FigureBase):

    # Объект класса фигуры можно вызвать как функцию
    def __call__(self, x: int, y: int, borderline: int) -> Generator[tuple[int,int],None,None]:
        return self.move_set(x,y,borderline)

    # Метод класса, генерирующий все возможные клетки атаки при постановке фигуры на выбранную клетку
    def move_set(self,x:int, y:int, borderline:int) -> Generator[tuple[int,int],None,None]:
        for i in (
            (x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),
            (x-1,y),(x-1,y+1),(x,y+1),(x+1,y+3),(x-1,y+3),
            (x-3,y+1),(x-3,y-1),(x-1,y-3),(x+1,y-3),(x+3,y-1),(x+3,y+1)
            ):
            if not(i[0]>borderline-1 or i[1]>borderline-1 or i[0]<0 or i[1]<0):
                yield i

# Класс игровой доски, осуществляет манипуляции с игровым полем, содержит информацию об игровом поле
class Desk():

    n:int
    figure:FigureBase
    storage=[]

    # Инициализирую пустое игровое поле при создании объекта
    def __init__(self, n:int, figure:FigureBase) -> None:
        self.figure = figure
        self.n = n
        self.storage = [0]*(n**2)
        pass
    
    # Метод, который ставит фигуру на доску. Возвращает True, если смог поставить фигуру, False, если не смог
    def set(self, x:int, y:int,owner:int=-2) -> bool: #owner = -1, если фигуру ставил человек, -2 если фигуру ставил скрипт
        n=self.n
        storage = self.storage
        if storage[y*n+x] == 0:
            storage[y*n+x] = owner
            for cords in self.figure(x,y,self.n):
                storage[cords[1]*n+cords[0]]+=1
            return True
        else:
            return False

    # Метод, убирающий фигуру с доски. Возвращает True, если смог убрать фигуру, False, если не смог
    def remove(self, x:int, y:int) -> bool:
        n=self.n
        storage = self.storage
        if storage[y*n+x] < 0:
            storage[y*n+x] = 0
            for cords in self.figure(x,y,self.n):
                storage[cords[1]*n+cords[0]]-=1
            return True
        else:
            return False

    # Метод, возвращающий координаты всех фигур, стоящих на доске
    def show_fig(self) -> Generator[tuple[int,int],None,None]:
        for index in range(self.n**2):
            if self.storage[index]<0:
                yield (index%self.n,index//self.n)
        pass
    
    # Метод, убирающий все фигуры, расставленные алгоритмом
    def clear(self) -> None:
        for index in range(self.n**2):
            if self.storage[index]==-2:
                self.remove(index%self.n,index//self.n)
        pass

    # При попытке взаимодействия с объектом возвращает списочную форму представления доски
    def __repr__(self) -> list:
        return self.storage

    # При попытке вывести объект в терминал, выведет его в списочном виде
    def __str__(self) -> str:
        return str(self.__repr__())

# Класс, отвечающий за просчёт вариантов расстановки
class Calculator():
    # При инициализации объекта класса пробует расставиль фигуры на доску хотя бы одним способом
    def __init__(self, l:int, desk:Desk) -> None:

        self.fast_answer(l,0,desk)

    # Рекурсивный алгоритм, который производит запись в файл. Заканчивает свою работу, когда найдёт все возможные варианты расстановок
    def recursion(self, file, l:int, current_position:int, desk:Desk) -> None:

        if l==0:
            file.write(' '.join(map(str,desk.show_fig()))+'\n')
            return 

        for pos in range(current_position,desk.n**2):
            if desk.set(pos%desk.n,pos//desk.n):
                self.recursion(file,l-1,pos,desk)
                desk.remove(pos%desk.n,pos//desk.n)

    # Такой же рекурсивный алгоритм, но завершает свою работу как только найдёт хотя бы одну расстановку
    def fast_answer(self, l:int, current_position:int, desk:Desk) ->bool:
        
        if l==0:
            return False

        for pos in range(current_position,desk.n**2):
            if desk.set(pos%desk.n,pos//desk.n):
                if not self.fast_answer(l-1,pos,desk):
                    return False
                desk.remove(pos%desk.n,pos//desk.n)
        
        return True



if __name__ == '__main__':
    a=Figure()
    for i in a(0,2,5):
        print(i)