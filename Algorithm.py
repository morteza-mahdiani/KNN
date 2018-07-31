#k-Nearest Neighbors
import math

def distance(instance1, instance2):
    dst = 0
    if len(instance1) < len(instance2):
        length = len(instance1)
    else:
        length = len(instance2)
    # calculate euclidean distance between two vector
    for x in range(length - 1):
        dst += pow(instance1[x] - instance2[x], 2)
    return math.sqrt(dst)

def getNeighbors(trainningset, testInstance, numberOfNeighbor):
    distanceList = []
    for x in range(len(trainningset)):
        dist = distance(trainningset[x], testInstance)
        distanceList.append([trainningset[x],dist])
    distanceList = sorted(distanceList, key = lambda dist: dist[1])
    # print distanceList
    neighbors = []
    for x in range(numberOfNeighbor):
         neighbors.append(distanceList[x][0])
    return neighbors


def normalizer(data):
    length = len(data)

    minTemp = float("inf")
    for x in range(length - 1):
        if data[x] < minTemp:
            minTemp = data[x]
    for x in range(length - 1):
        data[x] = data[x] - minTemp

    maxTemp = -1 * float("inf")
    for x in range(length -1):
        if data[x] > maxTemp:
            maxTemp = data[x]
    for x in range(length - 1):
        data[x] = data[x] / maxTemp

    return data

def sim(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] == data[j]:
                return data[i]

def updateAbundance(oldData, newData):
    for i in range(newData):
        if newData[i] == 1:
            oldData[i] == 1
    return oldData