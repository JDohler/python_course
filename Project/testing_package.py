# Testing the package first
## The Traveling Salesperson Problem

# Import classe from TSP new package
import tsp

print ("--------------------------------------------------------------------------")
print ("The 10 Largest Swedish Cities")
print ("--------------------------------------------------------------------------")

list_cities=[]
MembCities = tsp.Cities()
for city in MembCities.largest_cities():
    print("City:  %s" % city.name)
    list_cities.append(city.name)
print("City:  %s" % (list_cities))
    
city_name = input("Type a name of swedish city:")
city_name = str(city_name)
print(list_cities.index(city_name))



""""   
for index, distance in enumerate(city.distances):
    print("De %s --> %s = %s" % (city.name, MembCities.largest_cities[index].name, distance))

print ("--------------------------------------------------------------------------")
"""