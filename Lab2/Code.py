import copy

def PrintField(Field):
    for i in range(side):
        print(Field[i])

def FigureMoves(x:int,y:int):
    moves=((x+1,y+1),(x+1,y),(x+1,y-1),(x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+3),(x-1,y+3),(x-3,y+1),(x-3,y-1),(x-1,y-3),(x+1,y-3),(x+3,y-1),(x+3,y+1))
    LegitMoves=[i for i in moves if not(i[0]>side-1 or i[1]>side-1 or i[0]<0 or i[1]<0)]
    for i in LegitMoves:
        yield i

def PlaceFigure(x:int,y:int,Field:list[list[int]])-> list[list[int]]:
    TempField=copy.deepcopy(Field)
    for i in FigureMoves(x,y):
    #    if TempField[i[1]][i[0]]==-1:
    #        return Field
        TempField[i[1]][i[0]]+=1
    TempField[y][x]=-1
    return TempField

def RemoveFigure(x:int,y:int,Field:list[list[int]])-> list[list[int]]:
    TempField=copy.deepcopy(Field)
    for i in FigureMoves(x,y):
        #if TempField[i[1]][i[0]]==-1:
        #    return Field
        TempField[i[1]][i[0]]-=1
    TempField[y][x]=0
    return TempField

def recursion(place:int,CurrentX:int, CurrentY:int, Field:list[list[int]],Figures:list=[])-> list[list[int]]:
    if place==0:
        #PrintField(Field)
        #print()
        if frozenset(Figures) not in answer:
            
            File.write(",".join(map(str,Figures))+'\n')
            answer.add(frozenset(Figures))
        #File.write(",".join(map(str,Figures))+'\n')
        return
    else:
        for y in range(CurrentY,side):
            for x in range(CurrentX,side):
                
                #if x==0 and y==2:
                   # PrintField(Field)
                  #  print()
                Flag=False
                if Field[y][x]==0:
                    Field=PlaceFigure(x,y,Field)
                    Flag=True
                #if x==0 and y==2:
                 #   PrintField(Field)
                 #   print()
                 #   break
                if Flag and Field[y][x]==-1:
                    CurrentX=x
                    Flag=False
                    Figures.append((x,y))
                    recursion(place-1,CurrentX+1,CurrentY,Field,Figures)
                    Figures.pop(-1)
                    Field=RemoveFigure(x,y,Field)
                    #print(x,y)
            CurrentX=0
        
                
#Оптимизировать!!!!!!!!!!!!!!!

def main():
    with open('input.txt','r') as f:
        global side
        global File
        global answer
        answer=set()
        side,place,OnField=map(int,f.readline().split())
        Field=[[0]*side for _ in range(side)]
        for _ in range(OnField):
            x,y=map(int,f.readline().split())
            Field=PlaceFigure(x,y,Field)
        File=open("output.txt",'w')
        recursion(place,0,0,Field)
        File.close()
    print(len(answer))
if __name__=='__main__':
    main()