## The Traveling Salesperson Problem

# Import classe from TSP new package
import tsp

import json
from random import random
from random import randint
import matplotlib.pyplot as plt


# Define the origin city 
#---------------------------------------------------------------------------------------

list_cities=[]
MembCities = tsp.Cities()
for city in MembCities.largest_cities():
    print("City:  %s" % city.name)
    list_cities.append(city.name)
print("City:  %s" % (list_cities))
    
city_name = input("Type a name of swedish city:")
city_name = str(city_name)
print(list_cities.index(city_name))


# Individuo class
#----------------------------------------------------------------------------------------

class Individuals():
    def __init__(self, time_distances, cities, generation=0):
        self.time_distances = time_distances  
        self.cities = cities 
        self.generation = generation
        self.note_review = 0
        self.chromosome = []
        self.visited_cities = []
        self.travelled_distance = 0
        self.probability = 0

        # Create a chromosome (dont repeat city) always teh same size of the cities
        cities = []
        for i in range(len(self.cities)):
            cities.append(i)
        

        while len(cities) > 0:
            city = randint(0, len(cities) - 1) # randint returns an integer number selected element from the specified range
            self.chromosome.append(cities.pop(city)) # pop removes and returns the last value from the list or the given index value
           
                    
         
    def fitness(self):
        sum_distance = 0
        current_city = self.chromosome[0] 
        print("Current city:  %s" % (current_city))

        for i in range(len(self.chromosome)):
            d = tsp.Distance(self.cities)
            dest_city = self.chromosome[i] 
            distance = d.get_distance(current_city, dest_city)
            sum_distance += distance
            self.visited_cities.append(dest_city)  
            current_city = dest_city

  
            if i == len(self.chromosome) - 1:
                sum_distance += d.get_distance(self.chromosome[len(self.chromosome) - 1], self.chromosome[0])

        self.travelled_distance = sum_distance


    def crossover(self, otherIndividual):
        genes_1 = self.chromosome
        genes_2 = otherIndividual.chromosome
        selected_gene = randint(0, len(genes_1) - 1)
        self.exchange_gene(selected_gene, genes_1, genes_2)
        exchanged_genes = []
        exchanged_genes.append(selected_gene)
        while True:
            duplicated_gene = self.get_duplicated_gene(genes_1, exchanged_genes)
            if (duplicated_gene == -1):
                break
            self.exchange_gene(duplicated_gene, genes_1, genes_2)
            exchanged_genes.append(duplicated_gene)

        childs = [
            Individuals(self.time_distances, self.cities, self.generation + 1),
            Individuals(self.time_distances, self.cities, self.generation + 1)
        ]

        childs[0].chromosome = genes_1
        childs[1].chromosome = genes_2

        return childs



    def exchange_gene(self, gene, genes_1, genes_2):
        tmp = genes_1[gene]
        genes_1[gene] = genes_2[gene]
        genes_2[gene] = tmp


    def get_duplicated_gene(self, genes, exchanged_genes):
        for gene in range(len(genes)):
            if gene in exchanged_genes:
                continue

            if len([g for g in genes if g == genes[gene]]) > 1:
                return gene

        return -1



    def mutate(self, mutationRate):
        if randint(1, 100) <= mutationRate:
            print("Making a mutation on the chromosome %s" % self.chromosome)
            genes = self.chromosome
            gene_1 = randint(0, len(genes) - 1)
            gene_2 = randint(0, len(genes) - 1)
            tmp = genes[gene_1]
            genes[gene_1] = genes[gene_2]
            genes[gene_2] = tmp
            print("Value after mutation: %s" % self.chromosome)
        return self


class GeneticAlgorithm():
    def __init__(self, population_size=20, cities=[]):
        self.populationSize = population_size
        self.population = []
        self.generation = 0
        self.best_solution: 0
        self.cities = cities


    def init_population(self, time_distances, cities):
        for i in range(self.populationSize):
            self.population.append(Individuals(time_distances, cities))

        self.best_solution = self.population[0]

    def sort_population(self):
        self.population = sorted(self.population,
                                 key=lambda population: population.travelled_distance,
                                 reverse=False)


    def best_individual(self, individual):
        if individual.travelled_distance < self.best_solution.travelled_distance:
            self.best_solution = individual


    def sum_travelled_distance(self):
        sum = 0
        for individual in self.population:
            sum += individual.travelled_distance
        return sum


    def select_parents(self, sum_travelled_distances):
        total_coefficient = 0
        parent = -1  # nenhum indivíduo sorteado
        sum = 0
        i = 0


        for index in range(len(self.population)):
            total_coefficient += (1 / self.population[index].travelled_distance)


        for i_ in range(len(self.population)):
            coefficient = (1 / self.population[i_].travelled_distance)
            self.population[i_].probability = (coefficient / total_coefficient)

        sortedValue = random() 

        self.sort_population()
        while i < len(self.population) and sum < sortedValue:
            sum += self.population[i].probability
            parent += 1
            i += 1
        return parent

    def view_generation(self):
        best = self.population[0]
        print("G: %s -> Value: %s Chromosome: %s" % (
            best.generation,
            best.travelled_distance,
            best.chromosome
        ))

    def resolve(self, mutationRate, generations, time_distances, cities):
        self.init_population(time_distances, cities)
        for individual in self.population:
            individual.fitness()

        self.sort_population()
        self.view_generation()

        for generation in range(generations):
            sum_travelled_distance = self.sum_travelled_distance()
            newPopulation = []

            for i in range(0, self.populationSize, 2):
       
                parent1 = self.select_parents(sum_travelled_distance)
                parent2 = self.select_parents(sum_travelled_distance)


                childs = self.population[parent1].crossover(self.population[parent2])

                newPopulation.append(childs[0].mutate(mutationRate))
                newPopulation.append(childs[1].mutate(mutationRate))


            self.population = list(newPopulation)

            for individual in self.population:
                individual.fitness()
                # Uncomment do debug
                print("New population %s - Fitness %s" %
                      (individual.chromosome, individual.travelled_distance))

            # ordena população para melhor solução estar na primeira posição
            self.sort_population()
            self.view_generation()

            best = self.population[0]
            self.best_individual(best)

        print("\nBest solution -> G: %s - Total distance: %s - Chromosome: %s" % (
            self.best_solution.generation,
            self.best_solution.travelled_distance,
            self.best_solution.visited_cities
        ))


        return [
            self.best_solution.generation,
            self.best_solution.travelled_distance,
            self.best_solution.visited_cities
        ]


def parseJson(event, key):
    return json.loads(json.dumps(event[key]))


def handler(event, context):
    body_cities = None
    body_distances = None
    population_size = 20
    mutation_rate = 1  
    generations = 1000  
    time_distances = []

    if event:
        event = json.loads(event['body'])
        population_size = int(event['populationSize'])
        mutation_rate = int(event["mutationRate"])
        generations = int(event["generations"])
        body_cities = event['cities']
        body_distances = event["distances"]

    try:
        c = tsp.Cities()
        if body_cities and body_distances:
            c.set_cities(body_cities, body_distances)
        else:
            c.largest_cities() 
        cities_list = c.get_cities()

        for city in cities_list:
            print("Distance city: %s\n******" % city.name)
            time_distances.append(city.distances)
            print(city.distances)
            for index, distance in enumerate(city.distances):
                print("De %s --> %s = %s" % (city.name, cities_list[index].name, distance))

        ga = GeneticAlgorithm(population_size)
        result = ga.resolve(mutation_rate, generations, time_distances, cities_list)

        print({
            'generation': result[0],
            'travelled_distance': result[1],
            'chromosome': result[2],
            'cities': c.chromose_to_cities(result[2])
        })
        
        plt.plot(c.chromose_to_cities(result[2]))
        plt.title("Cities")
        plt.show() 


        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'generation': result[0],
                'travelled_distance': result[1],
                'chromosome': result[2],
                'cities': c.chromose_to_cities(result[2])
            })
        }

    except ImportError:
        print(ImportError)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': "Erro"
            })
        }


  
if __name__ == "__main__":
    handler(None, None)

