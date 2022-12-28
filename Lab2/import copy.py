import copy

def PrintField(Field):
    for i in range(side):
        print(Field[i])

def FigureMoves(x:int,y:int)-> list:
    moves=((x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+3),(x-1,y+3),(x-3,y+1),(x-3,y-1),(x-1,y-3),(x+1,y-3),(x+3,y-1),(x+3,y+1))
    LegitMoves=[i for i in moves if not(i[0]>side-1 or i[1]>side-1 or i[0]<0 or i[1]<0)]
    for i in LegitMoves:
        yield i

def PlaceFigure(x:int,y:int,Field:list[list[int]])-> list[list[int]]:
    TempField=copy.deepcopy(Field)
    for i in FigureMoves(x,y):
        if TempField[i[1]][i[0]]==-1:
            return Field
        TempField[i[1]][i[0]]+=1
    TempField[y][x]=-1
    return TempField

def RemoveFigure(x:int,y:int,Field:list[list[int]])-> list[list[int]]:
    TempField=copy.deepcopy(Field)
    for i in FigureMoves(x,y):
        if TempField[i[1]][i[0]]==-1:
            return Field
        TempField[i[1]][i[0]]-=1
    TempField[y][x]=0
    return TempField

def recursion(place:int,CurrentX:int, CurrentY:int, Field:list[list[int]],Figures:list=[])-> list[list[int]]:
    if place==0:
        answer.add(tuple(Figures))
    else:
        if CurrentX>side-1:
            CurrentX=0
            CurrentY+=1
        for y in range(side):
            if CurrentY<y:
                CurrentY=y
            if CurrentY==y:
                for x in range(side):
                    if CurrentX==x:
                        if CurrentX<x:
                            CurrentX=x
                        if Field[y][x]==0:
                            Field=PlaceFigure(x,y,Field)
                            if Field[y][x]==-1:
                                Figures.append((x,y))
                                #PrintField(Field)
                                #print()
                                recursion(place-1,CurrentX+2,CurrentY,Field)
                                Field=RemoveFigure(x,y,Field)
                                Figures.pop(-1)
                    #print(x,y)
                CurrentY=y



#Рекурсия идёт по пизде, подумай что не так, в остальном всё вроде ок. Вывод в файл потом придумай




def main():
    with open('input.txt','r') as f:
        global side
        global answer
        answer=set()
        side,place,OnField=map(int,f.readline().split())
        Field=[[0]*side for _ in range(side)]
        for _ in range(OnField):
            x,y=map(int,f.readline().split())
            Field=PlaceFigure(x,y,Field)
        recursion(place,0,0,Field)
    print(answer)
    #PrintField(Field)
if __name__=='__main__':
    main()