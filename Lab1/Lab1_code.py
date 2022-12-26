def req(Goal:int,Index:int,Data:list,end:bool=False)->list:
    #Проверка, нужно ли нам вообще что-то вычитать
    if sum(Data)==Goal:
            return Data
    #Цикл с перебором знаков
    for sign in (1,-1):
        Data[Index]*=sign
        if Index+1!=len(Data):
            req(Goal,Index+1,Data)
            if sum(Data)==Goal:
                return Data    
    #Если в цикле не было найдено решение, то мы доходим до выхода, который указывает на отсутствие решений            
    return ['No solution']

def main():
    # Считывание данных из файла: S - цель, n - количество чисел, x - список чисел, связанных с их изначальным индексом
    with open("input.txt",'r') as f:
        s=f.readline().split(' ')
        n=int(s[0])
        S=int(s[-1])
        x=[int(s[1:-1][i]) for i in range(len(s[1:-1]))]
    #Вызов рекурсии
        output=req(S,1,x)
    #Запись данныйх в файл, форматирование
    if output[0]=='No solution':
        with open('output.txt','w') as f:
            f.write('No solution')
    else:
        with open('output.txt','w') as f:
            f.write("+".join(map(str,output)).replace("+-",'-'))
    #Точка входа в программу
if __name__=="__main__":
    main()