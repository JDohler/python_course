# Python code to illustrate the Module
class Fish:
       # First we create a constructor for this class
       # and add members to it, here is some animals
       def __init__(self):
           self.members = ["Tuna", "Clownfish", "Tarpon", "Carp"]

       # A normal print function
       def outMembers(self):
           print('These are the harmless fish')
           for member in self.members:
               print('\t%s ' % member)