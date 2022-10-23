def funcName(list1,list2):
    set1,set2=set(list1),set(list2)
    answ1,answ2,answ3,answ4={str(x) for x in set1&set2 },{str(x) for x in set1.symmetric_difference(set2) },{str(x) for x in set1-set2 },{str(x) for x in set2-set1 }
    ans1,ans2,ans3,ans4='1) '+str(len(answ1))+' элементов: '+(', '.join(answ1)),'2) '+str(len(answ2))+' элементов: '+(', '.join(answ2)),'3) '+str(len(answ3))+' элементов: '+(', '.join(answ3)),'4) '+str(len(answ4))+' элементов: '+(', '.join(answ4))
    return [ans1,ans2,ans3,ans4]
if __name__ =='__main__':
    list1,list2=list(map(int,input('Введите элементы списка через пробел: ').split(' '))),list(map(int,input('Введите элементы списка через пробел: ').split(' ')))
    print(*funcName(list1,list2), sep='\n')