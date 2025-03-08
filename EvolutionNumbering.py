import numpy as np
import math as mp
import sys

n = int(1000) # population size. I recommend around 1000.
d = int(20) # dice face number
g = int(5) # number of generations. 5 is usually more than enough.

# Uncomment the vectors for the dice you are investigating. Note only d12 and d20 are given here but the others can be copied from the other script.
#d12 in 3D
#Vectors = np.matrix('0.85065 0.52573 0; 0.85065 -0.52573 0; 0 0.85065 -0.52573; 0.52573 0 -0.85065; 0 -0.85065 -0.52573; -0.52573 0 -0.85065; 0.52573 0 0.85065; 0 0.85065 0.52573; -0.52573 0 0.85065; 0 -0.85065 0.52573; -0.85065 0.52573 0; -0.85065 -0.52573 0')
#d20 in 3D
#Vectors = np.matrix('1 1 1; 1 1 -1; 1 -1 1; 1 -1 -1; -1 1 1; -1 1 -1; -1 -1 1; -1 -1 -1; 0 0.618033988749895 1.61803398874989; 0 0.618033988749895 -1.61803398874989; 0 -0.618033988749895 1.61803398874989; 0 -0.618033988749895 -1.61803398874989; 1.61803398874989 0 0.618033988749895; 1.61803398874989 0 -0.618033988749895; -1.61803398874989 0 0.618033988749895; -1.61803398874989 0 -0.618033988749895; 0.618033988749895 1.61803398874989 0; 0.618033988749895 -1.61803398874989 0; -0.618033988749895 1.61803398874989 0; -0.618033988749895 -1.61803398874989 0')

#Calculation
DiceNumbers = np.arange(d)+np.ones(d)

# Function to create a random numbering
def RandDice(DiceNumbers):
    d = np.size(DiceNumbers)
    order = np.random.rand(1,d)
    inds = order.argsort()
    return DiceNumbers[inds]

#Function finds the magnitude of the bias vector
def EvalDice(Numbering,Vectors):
    return np.linalg.norm(np.dot(Numbering,Vectors))

#Function creates all variations on a given numbering which are 1 face swap different.
def Variate(Numbering,d,Vectors):
    Population = np.copy(Numbering)
    Population = np.insert(Population,0,EvalDice(Numbering,Vectors),axis=1)
    for i in range(0,d-1):
        for j in range (i+1,d-0):
            Swapped = np.copy(Numbering)
            Swapped[0,i] = Numbering[0,j]
            Swapped[0,j] = Numbering[0,i]
            Swapped = np.insert(Swapped,0,EvalDice(Swapped,Vectors),axis=1)
            Population = np.insert(Population,0,Swapped,axis=0)
    return Population

#Function runs the evolution process for 1 generation
def Evolve(Population,Vectors,DiceNumbers,d,n):
    newPopulation = int(1)
    for i in range(0,n):
        if isinstance(Population, int):
            Numbering = RandDice(DiceNumbers)
        else:
            Numbering = Population[i,range(1,d+1)]
            Numbering = Numbering.reshape(1,-1)
        if isinstance(newPopulation, int):
            newPopulation = Variate(Numbering,d,Vectors)
        else:
            newPopulation = np.insert(Variate(Numbering,d,Vectors),0,newPopulation,axis=0)
    newPopulation = newPopulation[newPopulation[:, 0].argsort()]
    newPopulation = newPopulation[range(0,n),:]
    return newPopulation

#Actual script
Population = int(1)
Best = int(1)
for i in range(0,g):
    print(i)
    Population = Evolve(Population,Vectors,DiceNumbers,d,n)
    if isinstance(Best, int):
        Best = Population[0,:]
    elif Best[0] >= Population[0,0]:
        Best = Population[0,:]
    print(Population)

print(Best)
