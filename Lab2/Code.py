import copy
from typing import Generator
from typing import TypeAlias

# Глобальная аннотация шахматного поля, чтобы не пришлось писать из чего оно состоит в каждой функции, которая его использует
field:TypeAlias=list[list[int]]

# Функция для вывода нынешнего состояния доски: "-1" - фигура, "0" - свободная клетка, любое другое число - клетка под боем(число указывает сколько фигур бьют на эту клетку)
def PrintField(Field:field)-> None:
    for i in range(side):
        print(Field[i])

# Генератор, отсекающий ходы фигуры, выходящие за рамки игрового поля
def FigureMoves(x:int,y:int)-> Generator[tuple[int, int], None, None]:
    for i in ((x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+3),(x-1,y+3),(x-3,y+1),(x-3,y-1),(x-1,y-3),(x+1,y-3),(x+3,y-1),(x+3,y+1)):
        if not(i[0]>side-1 or i[1]>side-1 or i[0]<0 or i[1]<0):
            yield i

# Функция, ставящая фигуру на указанную клетку
def PlaceFigure(x:int,y:int,Field:field)-> field:
    # Расстановка клеток боя на поле
    for i in FigureMoves(x,y):
        Field[i[1]][i[0]]+=1
    # Ставим саму фигуру
    Field[y][x]=-1
    return Field

# Функция, убирающая фигуру с указанной клетки
def RemoveFigure(x:int,y:int,Field:field)-> field:
    # Убираем бой этой фигуры с тех клеток, на которых он был
    for i in FigureMoves(x,y):
        Field[i[1]][i[0]]-=1
    # Убираем саму фигуру
    Field[y][x]=0
    return Field

# Рекурентная функция, с точкой остановки "Все дополнительные фигуры поставлены"
def recursion(place:int,CurrentPos:int,Field:field,Figures:list=[])-> None:

    # Указываю на то что буду менять в этой функции значения глобальных переменных
    global Flag
    global OutputField
    # Точка остановки, если нам не нужно больше ставить фигуры на поле, мы записываем нынешнюю расстановку в файл и выходим из этой ветки рекурсии
    if place==0:
        # Здесь мы записываем первую удачную расстановку, чтобы потом её вывести в консоль, после чего больше не заходим в это условие
        if Flag==1:
            OutputField=copy.deepcopy(Field)
            Flag=False
        File.write(",".join(map(str,Figures))+'\n')
        return

    # Тело рекурсии
    else:

        # Представляем нашу шахматную доску в виде последовательности клеток, избавляясь от двумерности. Идти по доске мы начинаем с "Нулевой позиции"
        for pos in range(CurrentPos,side**2):

            #Если мы находим пустую клетку, то ставим на неё фигуру, записываем её местоположение, \\
            # меняем значение "Нулевой позиции" на следующую клетку после той, на которую мы поставили фигуру
            if Field[pos//side][pos%side]==0:
                Field=PlaceFigure(pos%side,pos//side,Field)
                Figures.append((pos%side,pos//side))
                recursion(place-1,pos+1,Field,Figures)

                # По достижению точки остановки мы возвращаемся сюда и переходим в другую ветку, снимая поставленную ранее на эту клетку фигуру
                Figures.pop(len(Figures)-1)
                Field=RemoveFigure(pos%side,pos//side,Field)
               
def main():
    # Объявление глоббальных переменных. 1) Сторонаа поля 2) Само шахматное поле 3) Поле для вывода в консоль 4) Флаг(нужен для более простого вывода поля в консоль)
    global side
    global File
    global OutputField
    global Flag
    Flag=True
    OutputField=[]
    
    # Считывание данных из файла
    with open('input.txt','r') as f:
        side,place,OnField=map(int,f.readline().split())

        # Генерация поля, расстановка константных фигур
        Field=[[0]*side for _ in range(side)]
        for _ in range(OnField):
            x,y=map(int,f.readline().split())
            Field=PlaceFigure(x,y,Field)
    # Рекурентная магия(подробнее в самой функции рекурсии), запись всех возможных расстановок в файл
    File=open("output.txt",'w')
    recursion(place,0,Field)
    File.close()

    # Вывод количества расстановок и поля в консоль, более чёткое обозначение отсутствия решений
    NoSolution=False
    with open("output.txt",'r') as f:
        file=f.readlines()
        if len(file)==0:
            NoSolution=True
            print('No Solutions')
        else:
            print(len(file))
            PrintField(OutputField)
    if NoSolution:
        with open("output.txt",'w') as f:
            f.write('No Solutions')

if __name__=='__main__':
    main()