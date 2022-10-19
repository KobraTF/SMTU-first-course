def main():
    s=input()
    flag=True
    ex='([{}])'
    arr=[]
    arr2=[]
    opening='([{'
    closing=')]}'
    """ for x in range(3):
        if s.count(ex[x])!=s.count(ex[5-x]):
            flag=False
            print(flag)
            break """
    if flag:
        x=0
        o=''
        f=True
        right=''
        while True:
            if s=='':
                break
            elif s[x] in opening:
                o+=closing[opening.find(s[x])]
                f=True
            elif o!='' and s[x]==o[-1]:
                if f:
                    right+=opening[closing.find(s[x])]+s[x]
                else:
                    right=opening[closing.find(s[x])]+right+s[x]
                s=s[:x-1]+s[x+1:]
                o=o[:len(o)-1]
                f=False
                x-=2
            else:
                arr.append(right)
                arr2.append(len(right))
                s=s[x+1:]
                o=''
                right=''
                x=0
                #print(s,o,x)
                continue
                flag=False
            x+=1
            if x==len(s):
                break
            #print(s[:x-1]+s[x+1:],s,o,o[:len(o)-1],x)
        #print(flag)
        if flag:
            print(right)
        else:
            print(arr[arr2.index(max(arr2))])



if __name__=='__main__':
    main()