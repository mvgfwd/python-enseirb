#open('data.txt')

f = open('data.txt', mode='w')
f
f.write('Hello world!!qw')
f.close()
print(f.closed)


with open('data.txt') as f:
    content = f.readlines()
    print(content)
    print(type(content))


print('un', 2, 3.0)

import sys
print('Erreur!', file=sys.stderr)

line = sys.stdin.readline()
print(f"written => {line}")