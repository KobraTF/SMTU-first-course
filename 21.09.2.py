def main():
    val=input('Введите число:')
    if int(val) in range(-2**7,2**7-1):
        if val[0]=='-' and int(val[:0:-1])in range(2**7+1):
            print('-',int(val[:0:-1]),sep='')
        elif val[0]!='-' and  int(val[::-1])in range(2**7):
            print(int(val[::-1]))
        else:
            print('no solution')
    else:
        print('no solution')
if __name__ =='__main__':
    main()