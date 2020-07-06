class Person:
    def __init__(self,name,age=0):
        self.name = name 
        self._age = age 

    def display_info(self):
        print(self.name)
        print(self._age) 

person = Person("Bari Allali",24)
person.display_info()
print(person._age)

class Person_one:
    def __init__(self,name,age=0):
        self.name = name 
        self.__age = age
    
    def display_info_one(self):
        print(self.name)
        print(self.__age)

person_one = Person_one()

person_one.display_info_one()
# cant access this varibale from outside the class
print(person_one.__age)