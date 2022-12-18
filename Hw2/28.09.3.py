def main():
    s=input()
    chrlist=[]
    indexlist=[]
    opening='({['
    closing=')}]'
    for x in range(len(s)):
        if s[x] in opening:
            chrlist.append([x,closing[opening.find(s[x])]])
        elif len(chrlist)!=0 and s[x] in closing:
            if chrlist[-1][1]==s[x]:
                indexlist.append([chrlist[-1][0],x])
                #print(chrlist)
                chrlist.pop()
                if len(indexlist)>1 and indexlist[-1][0]-1==indexlist[-2][1]:
                    indexlist[-2][1]=indexlist[-1][1]
                    indexlist.remove(indexlist[-1])
            else:
                chrlist=[]
    mlist=[[x[1]-x[0],x] for x in indexlist]
    if len(mlist)!=0:
        m=max(mlist)
        print(s[m[1][0]:m[1][1]+1])
        #print(mlist, s[mlist[]])


if __name__ == '__main__':
    main()