import Classes

def randomPopulation()
    newPopulation = []
    for x in range(0,99)
        newGenes = []
        newPlayers = []
        newGenes.append(random.randint(1,5))
        newGenes.append(random.randint(1,4))
        newGenes.append(random.randint(1,3))
        newGenes.append(random.randint(1,6))
        newGenes.append(random.randint(1,4))
        newGenes.append(random.randint(1,3))
        newGenes.append(random.randint(1,4))
        newGenes.append(random.randint(1,3))
        for y in range(0,17)
            for z in range(0,9)
                newPlayers.append(random.randint(1,5))
            for z in range(0,2)
                newPlayers.append(random.randint(0,1))
        newIndividual = Individual(newGenes, newPlayers)
        newPopulation.append(newIndividual)
    returnPop = Population(newPopulation)
    return returnPop

