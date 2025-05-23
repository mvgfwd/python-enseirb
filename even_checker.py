#!/usr/bin/env python3

def is_even(num=2):
    num = int(num)
    if num % 2 == 0:
        return print(f"{num} is even")
    else:
        return print(f"{num} is odd")
    

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 :
        is_even(sys.argv[1])
    else:
        pass