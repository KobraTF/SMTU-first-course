def main():
    val=input()
#Символы, которые мы должны вывести    
    length=int(input())
#Высота зиг-зага
    flag1,flag2=True,True
#Флаг1 - завершение кода, флаг2 - переключение счётчика    
    Len=len(val)
    counter=1
#Счётчик этажей    
    floor=1
#Этаж -номер строки, на которую мы выводим в даный момент символы    
    if length==1:
        print(val)
    else:
        modifier=(length-1)*2
#Целочисленный делитель
        while flag1:
            num=0
            f=0
            for _ in range(Len):
                if counter==floor:
                    print(val[num],end='')
                elif not flag2:
                    print(' ',end='')
                if counter==Len:
                    flag2=False
                elif counter==1:
                    flag2=True
                if flag2:
                    counter+=1
                else:
                    counter-=1
                num+=1
            if floor<length:
                floor+=1
            else:
                flag1=False
#Завершение программы
if __name__ =='__main__':
    main()