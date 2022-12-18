def req(Goal:int,CurrentSum:int,NextNumIndex:int,Numbers:list) ->list:
    # Точка остановки
    if NextNumIndex==len(Numbers) and Goal==CurrentSum:
        return Numbers
    elif NextNumIndex==len(Numbers) and Goal!=CurrentSum:
        return ['No solution']
    if Goal>CurrentSum:
        if Numbers[NextNumIndex][0]>=0:
            CurrentSum+=Numbers[NextNumIndex][0]
            Numbers[NextNumIndex]=tuple([Numbers[NextNumIndex][1],'+'+str(Numbers[NextNumIndex][0])])
        elif Numbers[NextNumIndex][0]<0:
            CurrentSum-=Numbers[NextNumIndex][0]
            Numbers[NextNumIndex]=tuple([Numbers[NextNumIndex][1],'-('+str(Numbers[NextNumIndex][0])+')'])
    else:
        if Numbers[NextNumIndex][0]>=0:
            CurrentSum-=Numbers[NextNumIndex][0]
            Numbers[NextNumIndex]=tuple([Numbers[NextNumIndex][1],'-'+str(Numbers[NextNumIndex][0])])
        elif Numbers[NextNumIndex][0]<0:
            CurrentSum+=Numbers[NextNumIndex][0]
            Numbers[NextNumIndex]=tuple([Numbers[NextNumIndex][1],'+('+str(Numbers[NextNumIndex][0])+')'])
    print(Goal,CurrentSum,NextNumIndex+1,Numbers)
    return req(Goal,CurrentSum,NextNumIndex+1,Numbers)
# Ключ сортировки словаря(сортируем по модулям чисел)
def TupleAbsSorting(tup:tuple) ->int:
    return abs(tup[0])

def main():
    # Считывание данных из файла: S - цель, n - количество чисел, x - список чисел, связанных с их изначальным индексом
    with open("input.txt",'r') as f:
        s=f.readline().split(' ')
        n=int(s[0])
        S=int(s[-1])
        x=[(int(s[1:-1][i]),i) for i in range(len(s[1:-1]))]
    # Сортировка списка, для упрощения алгоритма
    x=list(sorted(x,key=TupleAbsSorting,reverse=True))
    print(n,S,x)
    # Вызываем функцию, показывающую какие знаки какому числу нам нужно ставить
    x=req(S,x[0][0],1,x)
    OutputString=''
    print(x)
    # Если мы не нашли решение в функции, выводим "нет решений"
    if x[0]=='No solution':
        with open("output.txt",'w') as f:
            f.write(x[0])
    else:
        # Ставим знак первому числу
        if x[0][0]>0:
            x[0]=(x[0][1],'+'+str(x[0][0]))
        else:
            x[0]=(x[0][1],str(x[0][0]))
        # Возвращаем последовательность в исходное состояние, форматируем для вывода, выводим
        x=sorted(x)
        for i in range(len(x)):
            OutputString+=str(x[i][1])
        with open("output.txt",'w') as f:
            f.write(OutputString)
            
        
if __name__=='__main__':
    main()