from itertools import *
def main():
    pin=input()
    nums={
        '1':{1,2,4},
        '2':{1,2,3,5},
        '3':{2,3,6},
        '4':{1,4,7,5},
        '5':{2,4,5,6,8},
        '6':{3,5,6,9},
        '7':{4,7,8},
        '8':{5,7,8,9,0},
        '9':{6,8,9},
        '0':{8,0}
    }
    pin=[nums[x] for x in pin]
    pins=list(product(*pin))
    pins=[''.join(map(str,x)) for x in pins]
    print(pins)
if __name__=='__main__':
    main()