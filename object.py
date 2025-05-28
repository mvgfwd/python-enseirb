class Banana:
    pass

my_banana = Banana()
other_banana = Banana()

#print
print(type(my_banana))
print(type(other_banana))
print(id(my_banana))
print(id(other_banana))


class Human():
    def is_mortal(self):
        return True
    
floreal = Human()

ins = isinstance(floreal, (Human))
print(f'is floreal is instance of Human => {ins}')

class Philosopher(Human):
    pass

socrates = Philosopher()
print(f'socrates is mortal => {socrates.is_mortal()}')


#redefinition
class Highlander(Human):
    def is_mortal(self):
        return False
    
zeus = Highlander()
print(f'zeus is mortal => {zeus.is_mortal()}')