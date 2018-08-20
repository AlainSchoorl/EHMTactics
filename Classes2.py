import random
from operator import itemgetter
import time

class Individual(list):

    def mutate(self, extinctList):
        mutConst = 0.015
        mutConst2 = 0.015
        mutConst3 = 0.035
        for x in range(0, 5):
            for y in range(0, 10):
                if random.random() < mutConst or (random.random() < mutConst3 and ((x*13)+y) in extinctList):
                    mod = ((x*13) + y ) % 13
                    if mod == 1 or mod == 7:
                        self[((x * 13) + y)] = random.randint(3, 5)
                    elif mod == 2 or mod == 6 or mod == 10:
                        self[((x * 13) + y)] = random.randint(1, 3)
                    elif mod == 8 or mod == 9:
                        self[((x * 13) + y)] = random.randint(2, 5)
                    else:
                        self[((x * 13) + y)] = random.randint(1, 5)
            for y in range(10, 13):
                if random.random() < mutConst or (random.random() < mutConst3 and ((x * 13) + y) in extinctList):
                    self[((x * 13) + y)] = random.randint(0, 1)
        #run through each playerGenes element and have a small chance of changing them completely
        if random.random() < mutConst2 or (random.random() < mutConst3 and 234 in extinctList):
            self[65] = random.randint(1, 5)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 235 in extinctList):
            self[66] = random.randint(1,4)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 236 in extinctList):
            self[67] = random.randint(1,3)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 237 in extinctList):
            self[68] = random.randint(1,6)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 238 in extinctList):
            self[69] = random.randint(1,4)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 239 in extinctList):
            self[70] = random.randint(1,3)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 240 in extinctList):
            self[71] = random.randint(1,4)
        if random.random() < mutConst2 or (random.random() < mutConst3 and 241 in extinctList):
            self[72] = random.randint(1,3)
        #Then run through each genes element and have a small chance of changing them completely

    def breed(self, partner, i):
        child = self
        for x in range(0,72):
            if random.random() < 0.5:
                child[x] = partner[x]
        child[73] = 0
        child[74] = 0
        child[75] = i
        child[76] = 0
        return child

    def toText(self):
        print("text in csv")#all genes in csv

class Population:
    __individuals = []

    def __init__(self, i):
        self.__individuals = i

    def getIndividual(self, i):
        return self.__individuals[i]

    def setIndividual(self, i, ind):
        self.__individuals[i] = ind

    def getLength(self):
        return len(self.__individuals)

    def getFull(self):
        return self.__individuals

    def addLucky(self, l):
        self.__individuals.extend(l)

    def sort(self):
        self.__individuals = sorted(self.__individuals, key=itemgetter(75,73), reverse=True)

    def toText(self):
        print(self.__individuals)

    def shuffle(self):
        random.shuffle(self.__individuals)

    def selectParents(self):
        self.sort()
        parents = Population(self.__individuals[0:36])
        parents.addLucky(self.__individuals[0:6])
        tempList = []
        usedList = []
        print(len(self.__individuals))
        for x in range(0, 8):
            y = random.randint(36, 99)
            while y in usedList:
                y = random.randint(36,99)
            tempList.append(self.__individuals[y])
            usedList.append(y)
        parents.addLucky(tempList)
        return parents

    def breed(self, i, eList):
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
            if random.random() < 0.45:
                newList[x].mutate(eList)
        newGen = Population(newList)
        return newGen

    def getExtinctList(self):
        newList = []
        for x in range(0, 5):
            for y in range(0, 10):
                count1 = 0
                count2 = 0
                count3 = 0
                count4 = 0
                count5 = 0
                for ind in self.__individuals:
                    if ind[(x*13)+y] == 5:
                        count5 += 1
                    elif ind[(x*13)+y] == 4:
                        count4 += 1
                    elif ind[(x*13)+y] == 3:
                        count3 += 1
                    elif ind[(x*13)+y] == 2:
                        count2 += 1
                    elif ind[(x*13)+y] == 1:
                        count1 += 1
                iterator = [count1, count2, count3, count4, count5]
                i = 0
                for count in iterator:
                    if count < 4:
                        i += 1
                if i > 2:
                    newList.append((x*13)+y)
                    print ("Added " + str((x*13)+y) + " to extinctList")
            for y in range(10, 13):
                count1 = 0
                for ind in self.__individuals:
                    if ind[(x * 13) + y] == 1:
                        count1 += 1
                if count1 > 90 or count1 < 10:
                    newList.append((x * 13) + y)
                    print ("Added " + str((x * 13) + y) + " to extinctList")
        for run in range(65, 72):
            count1 = 0
            count2 = 0
            count3 = 0
            count4 = 0
            count5 = 0
            count6 = 0
            for ind in self.__individuals:
                if ind[run] == 5:
                    count5 += 1
                elif ind[run] == 4:
                    count4 += 1
                elif ind[run] == 3:
                    count3 += 1
                elif ind[run] == 2:
                    count2 += 1
                elif ind[run] == 1:
                    count1 += 1
                elif ind[run] == 6:
                    count6 += 1
            iterator = [count1, count2, count3, count4, count5, count6]
            i = 0
            for count in iterator:
                if count < 3:
                    i += 1
            if run == 65:
                if i > 1:
                    newList.append(run)
                    print ("Added " + str(run) + " to extinctList")
            elif run == 66 or run == 69 or run == 71:
                if i > 2:
                    newList.append(run)
                    print ("Added " + str(run) + " to extinctList")
            elif run == 67 or run == 70 or run == 72:
                if i > 3:
                    newList.append(run)
                    print ("Added " + str(run) + " to extinctList")
            elif run == 68:
                if i > 0:
                    newList.append(run)
                    print ("Added " + str(run) + " to extinctList")
        return newList
