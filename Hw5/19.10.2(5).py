from itertools import combinations
def main(list1):
    set1=set(list1)
    set2=set()
    for x in range(len(set1)):
        set3={tuple(i) for i in combinations(set1,x+1)}
        set2.update(set3)
    print("Количество подмножеств: "+str(2**len(set1)-1),set2, sep='\n')

if __name__=='__main__':
    list1=list(map(int,input('Введите список через пробел: ').split(' ')))
    main(list1)