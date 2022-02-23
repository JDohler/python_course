# Python code to illustrate the Module
class Mammals:
       # First we create a constructor for this class
       # and add members to it, here is some animals
       def __init__(self):
           self.members = ["Cow", "Dog", "Horse", "Goat"]

       # A normal print function
       def outMembers(self):
           print('These are the harmless mammals')
           for member in self.members:
               print('\t%s ' % member)