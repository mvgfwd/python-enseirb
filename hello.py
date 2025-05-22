#!/usr/bin/env python3

#print("Hello World")

def say_hello(whom='world'):
    print(f"Hello {whom}")


#Magical Receipt
if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1 :
        say_hello(sys.argv[1])
        
    say_hello()