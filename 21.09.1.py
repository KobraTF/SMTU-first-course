def main():
    val=input('Введите число:')
    if val==val[::-1]:
        print(True)
    else:
        print(False)
if __name__ =='__main__':
    main()