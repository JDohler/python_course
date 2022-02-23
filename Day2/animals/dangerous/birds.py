# Python code to illustrate the Module
class Birds:
           	# First we create a constructor for this class
           	# and add members to it, here is some animals
           	def __init__(self):
           		self.members = ["Ostrich", "Eagle", "Emu", "Casuar"]

           	# A normal print function
           	def outMembers(self):
           		print('These are the dangerous birds')
           		for member in self.members:
           			print('\t%s ' % member)