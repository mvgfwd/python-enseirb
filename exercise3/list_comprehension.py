li = ['vélo', 'volant', 'fin', 'test']

#this will print each length of element in list li
[len(x) for x in li]

#total character in list li
sum([len(x) for x in li])

#show result with 'v' in list li
[x for x in li if x[0] == "v"]

#this is create tuples of name each element + length of it
{(x,len(x)) for x in li}

#create sets of element key and the length element for the value
{x: len(x) for x in li}

#create sets that make all key has an 'o' inside each element in list li
{x: len(x) for x in li if 'o' in x}

#make list with 3 lists inside it which has 4 zero inside it
l = [[0] * 4] * 3
l[0][0] = 1

#list even
l_iseven = [ [ i % 2 == 0 for i in row] for row in l ]