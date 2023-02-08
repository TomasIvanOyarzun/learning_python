class Person:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
       
       
    def walk(self):
        print(f"{self.name} is walking !!!")

  


    def __repr__(self) -> str:
        return f"{self.name} {self.lastname}"




class ListPerson:

    def __init__(self):
        self.listPersons = []

        






