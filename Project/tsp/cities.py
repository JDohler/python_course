## The Traveling Salesperson Problem

class City():
    def __init__(self, name, distances): 
        self.name = name 
        self.distances = distances

    def getName(self):
        return self.name 


    def getDistances(self):
        return self.distances


class Cities():
    def __init__(self, cities=[]):
        self.cities = cities
    
    def largest_cities(self):
        ## this add cities members, here is the 10 largest Swedish cities
       # print("The 10 largest Swedish cities")
        # Distance in km. Writen in the same order as can be seen.
        self.cities = [
            City("Stockholm", [0, 470, 613, 70, 27, 108, 202, 200, 557, 112]),
            City("Goteborg", [470, 0, 272, 535, 491, 380, 285, 274, 215, 418]),
            City("Malmo", [613, 272, 0, 680, 635, 597, 502, 417, 65, 562]),
            City("Uppsala", [70, 535, 680, 0, 46, 78, 171, 265, 622, 110]),
            City("Upplands Vasby", [27, 491, 635, 46, 0, 93, 186, 221, 578, 134]),
            City("Vasteras", [108, 380, 597, 78, 93, 0, 95, 187, 540, 45]),
            City("Orebro", [202, 285, 502, 171, 186, 95, 0, 122, 446, 88]),
            City("Linkoping", [200, 274, 417, 265, 221, 187, 122, 0, 362, 149]),
            City("Helsingborg", [557, 215, 65, 622, 578, 540, 446, 362, 0, 505]),
            City("Eskilstuna", [112, 418, 562, 110, 134, 45, 88, 149, 505, 0])
        ]
        
        return self.cities

   
    def chromose_to_cities(self, chromosome):
       cities = []
       for i in range(len(chromosome)):
         cities.append(self.get_city(chromosome[i]).name)
       return cities

    def get_city(self, index):
        return self.cities[index]
        
  
    def get_city_distances(self, index):
        return self.get_city(index).distances

    def get_cities(self):
        return self.cities

    def set_cities(self, cities=[], distances=[[]]):
        self.cities = []
        for i in range(len(cities)):
            self.cities.append(City(cities[i], distances[i]))
            print(self.cities[i])    

    def get_total_cities(self):
        return len(self.cities)
