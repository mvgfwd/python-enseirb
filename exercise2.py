#IF ELSE
li = ['vélo', 'volant', 'fin', 'test', 'test']
if 'vélo' not in li:
    li.insert(0, 'vélo')
elif 'moto' not in li:
    li.append('moto')
else:
    li.remove('fin')
print("li => ", li)


#WHILE LOOP
v = li[:2]
while len(v) < 4:
    v.append(v[0]+v[-1])
print("v => ", v)


#FOR LOOP
for x in li:
    print(f'elements of li: {x}')

for i, x in enumerate(li):
    print(f'li[{i}] = {x}')

c = []
for i in range(10):
    c.append(li[i % len(li)])
print(f"c => {c}")


#MATH
def double(x):
    return x * 2

d_3 = double(3)
d_list = double([1,2,3])
print(f"double(3) => {d_3}")
print(f"double([1,2,3]), {d_list}")
#double('a') //ERROR
#double({1,2,3}) //ERROR

[len(x) for x in li]
#FUNCTION
def hello(name, greeting='Hello'):
    return f'{greeting}, {name}!'

hello_john = hello('John')
hello_john_bonjour = hello('John', greeting='Bonjour')
hello_error = hello('John', 'Bonjour')
print(f"hello('John') {hello_john}")   
print(f"hello('John', greeting='Bonjour') {hello_john_bonjour}")
print(f"hello('John', 'Bonjour') {hello_error}")


def sum_power(x, y, power_x=2, power_y=2):
    return x**power_x + y**power_y
#sp_3 = sum_power(3) //ERROR
#sp_34 = sum_power(3, 4) //ERROR
#sp_py = sum_power(3, 4, power_y=3) //ERROR
