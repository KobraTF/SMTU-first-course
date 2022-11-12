from collections import namedtuple as nt
def bank_input():
    bank=nt('bank',['name','cost'])
    s=input('Введите банки в формате: ("название1" ,стоимость1),("название2" ,стоимость2),("название3" ,стоимость3): ')
    s=s.strip().split(',')
    arr=[]
    for _ in range(len(s)//2):
        arr+=[bank(s.pop(0).strip()[1:],int(s.pop(0).strip()[:-1]))]
    return arr
def CostSumm(indexes):
    return sum(Banks[i].cost for i in indexes)
def main():
    global Banks
    Banks=bank_input()
    if Banks[0].cost>Banks[1].cost:
        IndexList=[[0],[0]]
    else:
        IndexList=[[0],[1]]
    #print(IndexList)
    for x in range(2,len(Banks)):
        NewWay,OldWay=[*IndexList[0],x],[*IndexList[1]]
        if CostSumm(NewWay)>CostSumm(OldWay):
            IndexList[0],IndexList[1]=OldWay,NewWay
        else:
            IndexList[0],IndexList[1]=OldWay,OldWay
    print("Мы грабим: ")
    for x in IndexList[1]:
        print(x+1,Banks[x].name)
    print("Сумма награбленного:",CostSumm(IndexList[1]))
if __name__=="__main__":
    main()