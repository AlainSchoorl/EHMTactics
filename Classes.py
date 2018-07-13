import random

class Individual
    __genes = []
    __playerGenes = []
    __fitness = []

    def __init__(self, geneticCode):
        self.__genes = geneticCode.split(" ", 8)
        self.__playerGenes = geneticCode.split("")[-234:]


    def getGenes(self):
        return self.__genes

    def getPlayerGenes(self):
        return self.__playerGenes

    def getFitness(self):
        return self.__fitness

    def setFitness(self, l):
        self.__fitness = l

    def mutate(self):
        #Run through each genes element and have a small chance of changing them completely
        #Then run through each playerGenes element and have a small chance of changing them completely

    def breed(self, partner)
        child = self
        for x in self.__genes:
            if(random.random < 0.5)
                child.getGenes[x] = partner.getGenes[x]
        for x in self.__playerGenes:
            if(random.random < 0.5)
                child.getGenes[x] = partner.getGenes[x]
        return child

class Population
    __individuals = []

    def __init__(self, i):
        self.__individuals = i

    def getIndividual(self, i):
        return self.__individuals[i]

    def mutate(self):
        #Run through each individual and have a 20%ish chance to mutate() them

    def sort(self):
        #Sort population from most fit to least fit

    def toText(self):
        #return csv of population

    def selectParents(self):
        parents = self.__individuals[0:32]
        tempList = []
        usedList = []
        for x in range(0, 17)
            y = random.randint(32, 99)
            while y in usedList
                y = random.randint(32,99)
            tempList.append(self.__individuals[y])
            usedList.append(y)
        parents = parents.extend(tempList)
        return parents

    def breed(self):
        random.shuffle(self.__individuals)
        newList = []
        x = 0
        while x < 49
            newList.append(self.__individuals[x].breed(self.__individuals[(x+1)]))
            x += 2
        random.shuffle(self.__individuals)
        x = 0
        while x < 49
            newList.append(self.__individuals[x].breed(self.__individuals[(x+1)]))
            x += 2
        return newList
