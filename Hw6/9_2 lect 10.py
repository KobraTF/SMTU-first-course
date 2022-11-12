def main():
    rim={'I':1,"V":5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    inp=list(input()[::-1].upper())
    #print(inp,rim)
    inp=[rim[x] for x in inp]
    inp.append(0)
    su=0
    for x in range(len(inp)-1):
        if inp[x+1]<inp[x]:
            su+=inp[x]-inp[x+1]*2
        else:
            su+=inp[x]
    print(su)
if __name__ =="__main__":
    main()
