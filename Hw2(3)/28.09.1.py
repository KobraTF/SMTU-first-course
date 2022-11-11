def main():
    s=input()
    temp=''
    arr=[]
    arr2=[]
    for x in range(len(s)):
        if s[x] not in temp:
            temp+=s[x]
        else:
            arr.append(temp)
            arr2.append(len(temp))
            temp=temp[temp.find(s[x])+1:]+s[x]
        #print(arr,arr2,temp,s,x)
    arr.append(temp)
    arr2.append(len(temp))
    print(arr[arr2.index(max(arr2))])
if __name__=='__main__':
    main()