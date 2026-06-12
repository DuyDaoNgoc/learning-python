
import types

class Duy:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
profile = Duy(name=input("nhập tên: "), age=int(input("nhập tuổi: ")))
profile.display_info()


from reloadall import status, tryreload
def  transitive_reload(objects,visited):
        while objects:
            nexts = objects.pop()
            if(type(nexts) == types.ModuleType and not nexts in visited):
                status(nexts)
                tryreload(nexts)
                visited.add(nexts)
                objects.extend(nexts.__dict__.values())
def reload_all(*args):
    transitive_reload(list(args),set())
from reloadall import tester
if __name__ == "__main__":
    tester(reload_all,"reloadall3")


class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):
        print(f'{self.name} gâu gâu đang ăn')


a = Animal('Generic animal')
b = Dog('Buddy')

a.eat()
b.eat()


# [/////////////////////////////////////////////////////////]
# [//  /////////////////// ///////////              // /////]
# [//  ////          /////  /////////////////////////  /////]
# [//  ///////////////////  /////////////////////////  /////]
# [//  ///////     ///////  //////////       ////////  /////]
# [//  ////////  /////////  //////            ///////  /////]
# [//  ///////////////////  /////////////////////////  /////]
# [//  /////        //////  ///////           ///////  /////]
# [//  ///////////////////  /////////////////////////  /////]
# [//  ///////////////////  /////       /////////////  /////]
# [//  ///////////////////  /////////////////////////  /////]
# [//  //////      ///////  /////////////      //////  /////]
# [//  ///////////////////  /////////////////////////  /////]
# [//  ///////////////////  /////            ////////  /////]
# [//  /////        //////  //////////////  /////////  /////]
# [/////////////////////////////////////////////////////////]
# //////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
