import random

class Fish:
    def __init__(self,color_value,species_type,water_region,fish_size):
        self.color = color_value
        self.species = species_type
        self.region = water_region
        self.size = fish_size

def randcol():
    color_seed = random.randint(1,4)
    if color_seed == 1:
        return "White"
    if color_seed == 2:
        return "Rainbow"
    if color_seed == 3:
        return "Salmon"
    if color_seed == 4:
        return "Tuna"

def randspec():
    species_seed = random.randint(1,4)
    if species_seed == 1:
        return "Trout"
    if species_seed == 2:
        return "Bass"
    if species_seed == 3:
        return "Salmon"
    if species_seed == 4:
        return "Tuna"

def randreg():
    region_seed = random.randint(1,2)
    if region_seed == 1:
        return "Saltwater"
    if region_seed == 2:
        return "Freshwater"

def randsize():
    size_seed = random.randint(1,4)
    if size_seed == 1:
        return "Smol"
    if size_seed == 2:
        return "Medium"
    if size_seed == 3:
        return "Large"
    if size_seed == 4:
        return "Obese"

population = []
for i in range(10000):
    population.append(Fish(randcol(),randspec(),randreg(),randsize()))

trout_counter = 0

for fishy in population:
    if fishy.species == "Trout":
        trout_counter += 1

print("Before sort:")
for i in range(10):
    print(population[i].species,end=", ")
print()

population.sort(key=lambda fish: fish.species)

print("After sort:")
for i in range(10):
    print(population[i].species,end=", ")
print()

print("There are", trout_counter, "trout")