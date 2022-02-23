# Python code to illustrate the Module
class Fish:
       # First we create a constructor for this class
       # and add members to it, here is some animals
       def __init__(self):
           self.members = ["Puffer", "Moray Eel", "Piranha", "Stonefish"]

       # A normal print function
       def outMembers(self):
           print('These are the dangerous fish')
           for member in self.members:
               print('\t%s ' % member)