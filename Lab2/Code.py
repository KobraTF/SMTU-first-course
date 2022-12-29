import copy
from typing import Generator
from typing import TypeAlias

field:TypeAlias=list[list[int]]

def PrintField(Field):
    for i in range(side):
        print(Field[i])

def FigureMoves(x:int,y:int)-> Generator[int, None, None]:
    for i in ((x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+3),(x-1,y+3),(x-3,y+1),(x-3,y-1),(x-1,y-3),(x+1,y-3),(x+3,y-1),(x+3,y+1)):
        if not(i[0]>side-1 or i[1]>side-1 or i[0]<0 or i[1]<0):
            yield i

def PlaceFigure(x:int,y:int,Field:field)-> field:
    for i in FigureMoves(x,y):
        Field[i[1]][i[0]]+=1
    Field[y][x]=-1
    return Field

def RemoveFigure(x:int,y:int,Field:field)-> field:
    for i in FigureMoves(x,y):
        Field[i[1]][i[0]]-=1
    Field[y][x]=0
    return Field

def recursion(place:int,CurrentPos:int,Field:field,Figures:list=[])-> None:
    global Flag
    global OutputField
    if place==0:
        if Flag==1:
    
            OutputField=copy.deepcopy(Field)
            Flag=False
        File.write(",".join(map(str,Figures))+'\n')
        return
    else:
        for pos in range(CurrentPos,side**2):
            if Field[pos//side][pos%side]==0:
                Field=PlaceFigure(pos%side,pos//side,Field)
                CurrentPos=pos
                Figures.append((pos%side,pos//side))
                recursion(place-1,CurrentPos+1,Field,Figures)
                Figures.pop(len(Figures)-1)
                Field=RemoveFigure(pos%side,pos//side,Field)
               
def main():
    
    with open('input.txt','r') as f:
        global side
        global File
        global OutputField
        global Flag
        Flag=True
        OutputField=[]
        side,place,OnField=map(int,f.readline().split())
        Field=[[0]*side for _ in range(side)]
        for _ in range(OnField):
            x,y=map(int,f.readline().split())
            Field=PlaceFigure(x,y,Field)
        File=open("output.txt",'w')
        recursion(place,0,Field)
        File.close()
        with open("output.txt",'r') as f:
            print(len(f.readlines()))
            PrintField(OutputField)
if __name__=='__main__':
    main()