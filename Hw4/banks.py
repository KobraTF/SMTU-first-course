from collections import namedtuple
from itertools import count
bank=namedtuple('bank',['bankname','bankvalue'])
'''def bankinput():
    name,value=input("Введите имя и стоимость банка через пробел: ").split(' ')
    value=int(value)
    my_bank=bank(name,value)
    return my_bank
'''
def main():
    number=int(input('Введите количество банков: '))
#    banks=[bankinput() for _ in range(number)]
    s=list(input("Введите список банков: ")[1:-1].split('),'))
    banks=[bank(x.split(',')[0][2:-1],int(x.split(',')[1])) for x in s[:-1]]
    banks.append(bank(s[-1].split(",")[0][2:-1],int(s[-1].split(",")[1][:-1])))
    maxsum=0
    valuesum=0
    banksoutput=[]
    output=[] 
    for counter in range(2):
        f=False
        valuesum+=banks[counter].bankvalue
        banksoutput.append(tuple([banks[counter].bankname,counter+1]))
        counter+=2
        if counter ==number-2==1 or counter>=number:
            f=True
        while True:
            if counter == number-3:
                valuesum+=banks[counter+2].bankvalue
                banksoutput.append(tuple([banks[counter+2].bankname,counter+3]))
                break
            elif counter==number-1:
                valuesum+=banks[counter].bankvalue
                banksoutput.append(tuple([banks[counter].bankname,counter+1]))
                break
            elif counter>=number-2 and f:
                break
            if banks[counter].bankvalue<banks[counter+1].bankvalue:
                valuesum+=banks[counter+1].bankvalue
                banksoutput.append(tuple([banks[counter+1].bankname,counter+2]))
                counter+=3
            else:
                valuesum+=banks[counter].bankvalue
                banksoutput.append(tuple([banks[counter].bankname,counter+1]))
                counter+=2
            f=True
        if valuesum>maxsum:
            maxsum=valuesum;output=banksoutput
        valuesum=0
        banksoutput=[]
    print(maxsum,output)


if __name__=="__main__":
    main()