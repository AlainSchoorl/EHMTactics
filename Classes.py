import random
from operator import itemgetter

class Individual(list):

    def mutate(self):
        mutConst = 0.2
        mutConst2 = 0.3
        for x in range(0, 18):
            for y in range(0, 10):
                if random.random() < mutConst:
                    self[((x*13)+y)] = random.randint(1,5)
            for y in range(10, 3):
                if random.random() < mutConst:
                    self[(x*13)+y] = random.randint(0,2)
        #run through each playerGenes element and have a small chance of changing them completely

        if random.random() < mutConst2:
            self[234] = random.randint(1,5)
        if random.random() < mutConst2:
            self[235] = random.randint(1,4)
        if random.random() < mutConst2:
            self[236] = random.randint(1,3)
        if random.random() < mutConst2:
            self[237] = random.randint(1,6)
        if random.random() < mutConst2:
            self[238] = random.randint(1,4)
        if random.random() < mutConst2:
            self[239] = random.randint(1,3)
        if random.random() < mutConst2:
            self[240] = random.randint(1,4)
        if random.random() < mutConst2:
            self[241] = random.randint(1,3)
        #Then run through each genes element and have a small chance of changing them completely

    def breed(self, partner, i):
        child = self
        for x in range(0,242):
            if random.random() < 0.5:
                child[x] = partner[x]
        child[242] = 0
        child[243] = 0
        child[244] = i
        return child

    def toText(self):
        print("text in csv")#all genes in csv

class Population:
    __individuals = []

    def __init__(self, i):
        self.__individuals = i

    def getIndividual(self, i):
        return self.__individuals[i]

    def getLength(self):
        return len(self.__individuals)

    def getFull(self):
        return self.__individuals

    def addLucky(self, l):
        self.__individuals.extend(l)

    def sort(self):
        self.__individuals = sorted(self.__individuals, key=itemgetter(244,242), reverse=True)

    def toText(self):
        print(self.__individuals)

    def selectParents(self):
        self.sort()
        parents = Population(self.__individuals[0:32])
        tempList = []
        usedList = []
        print(len(self.__individuals))
        for x in range(0, 18):
            y = random.randint(32, 99)
            while y in usedList:
                y = random.randint(32,99)
            tempList.append(self.__individuals[y])
            usedList.append(y)
        parents.addLucky(tempList)
        return parents

    def breed(self, i):
        random.shuffle(self.__individuals)
        newList = []
        i = i*-1
        for r in range(0,4):
            x = 0
            while x < 49:
                newList.append(self.__individuals[x].breed(self.__individuals[(x+1)], i))
                x += 2
            random.shuffle(self.__individuals)
            print ('Breeding. Now has ' + str(len(newList)))
        for x in range(0,100):
            if random.random() < 0.33:
                newList[x].mutate()
        newGen = Population(newList)
        return newGen
