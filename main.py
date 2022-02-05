from queue import PriorityQueue
from classes import *
from func import *
from random import random
def main():

    PriorityQueue = heap()

    for i in time(24 * 7 * 60):

        prob = random()

        if prob > 0.96:

            p, l = randVals()

            Job = JobID(p, l)

            PriorityQueue.insert(Job)


    PriorityQueue.display()
if __name__ == '__main__':
    main()


