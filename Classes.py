import random

class Individual
    __genes = []
    __playerGenes = []
    __fitness = []

    def __init__(self, geneCode, playerCode):
        self.__genes = geneCode
        self.__playerGenes = playerCode

    def getGenes(self):
        return self.__genes

    def getPlayerGenes(self):
        return self.__playerGenes

    def getFitness(self):
        return self.__fitness

    def setFitness(self, l):
        self.__fitness = l

    def mutate(self):
        if random.random < 0.042
            self.__genes[0] = random.randint(1,5)
        if random.random < 0.042
            self.__genes[1] = random.randint(1,4)
        if random.random < 0.042
            self.__genes[2] = random.randint(1,3)
        if random.random < 0.042
            self.__genes[3] = random.randint(1,6)
        if random.random < 0.042
            self.__genes[4] = random.randint(1,4)
        if random.random < 0.042
            self.__genes[5] = random.randint(1,3)
        if random.random < 0.042
            self.__genes[6] = random.randint(1,4)
        if random.random < 0.042
            self.__genes[7] = random.randint(1,3)
        #Run through each genes element and have a small chance of changing them completely
        for x in range(0, 17)
            for y in range(0, 9)
                if random.random < 0.042
                    self.__playerGenes[((x*13)+y)] = random.randint(1,5)
            for y in range(10,12)
                if random.random < 0.042
                    self.__playerGenes[(x*13)+y] = random.randint(0,1)
        #Then run through each playerGenes element and have a small chance of changing them completely

    def breed(self, partner)
        child = self
        for x in self.__genes:
            if random.random < 0.5
                child.getGenes[x] = partner.getGenes[x]
        for x in self.__playerGenes:
            if random.random < 0.5
                child.getGenes[x] = partner.getGenes[x]
        return child

    def toText(self:
        #all genes in csv

class Population
    __individuals = []

    def __init__(self, i):
        self.__individuals = i

    def getIndividual(self, i):
        return self.__individuals[i]

    def getLength(self):
        return len(self.__individuals)

    def sort(self):
        #Sort population from most fit to least fit

    def toText(self):
        print(self.__individuals)

    def selectParents(self):
        self.sort()
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
        for x in newList
            if random.random < 0.25
                newList[x].mutate()
        return newList
