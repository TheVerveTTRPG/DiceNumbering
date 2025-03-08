import numpy as np
import math as mp
import sys

# Set d = to the number of dice faces.
d = int(10)

#Uncomment the row for the vectors assocaiated with the dice size and dimension you are investigating.

#d4 in 2D
#Vectors = np.matrix('0 1; 1 0; 0 -1; -1 0')
#d4 in 3D
#Vectors = np.matrix('1 1 1; 1 -1 -1; -1 1 -1; -1 -1 1')/np.sqrt(3)
#d6 in 2D
#Vectors = np.matrix('0 1; 0.866 0.5; 0.866 -0.5; 0 -1; -0.866 -0.5; -0.866 0.5')
#d6 in 3D
#Vectors = np.matrix('0 1 0; 0 0 1; 1 0 0; -1 0 0; 0 0 -1; 0 -1 0')
#d8 in 2D
#Vectors = np.matrix('0 0.7071; 0.7071 0; 1 -0.7071; 0.7071 -1; 0 -0.7071; -0.7071 0; -1 0.7071; -0.7071 1')
#d 8 in 3D
#Vectors = np.matrix('1 1 1; 1 1 -1; 1 -1 1; 1 -1 -1; -1 1 1; -1 1 -1; -1 -1 1; -1 -1 -1')/np.sqrt(3)
#d10 in 3D
#Vectors = np.matrix('0.21851 0.6725 0.70711; -0.57206 0.41563 0.70711; -0.57206 -0.41563 0.70711; 0.21851 -0.6725 0.70711; 0.70711 0 0.70711; -0.70711 0 -0.70711; -0.21851 0.6725 -0.70711; 0.57206 0.41563 -0.70711; 0.57206 -0.41563 -0.70711; -0.21851 -0.6725 -0.70711')
#d12 in 3D
#Vectors = np.matrix('0.85065 0.52573 0; 0.85065 -0.52573 0; 0 0.85065 -0.52573; 0.52573 0 -0.85065; 0 -0.85065 -0.52573; -0.52573 0 -0.85065; 0.52573 0 0.85065; 0 0.85065 0.52573; -0.52573 0 0.85065; 0 -0.85065 0.52573; -0.85065 0.52573 0; -0.85065 -0.52573 0')
#d20 in 3D - DO NOT RUN THIS! IT TAKES 2 MILLION YEARS!
#Vectors = np.matrix('0.491123473    0.35682209  0.794654472; -0.187592474    0.577350269 0.794654472; -0.607061998    0   0.794654472; -0.187592474    -0.577350269    0.794654472; 0.491123473 -0.35682209 0.794654472; 0.794654472 0.577350269 0.187592474; -0.303530999    0.934172359 0.187592474; -0.982246946    0   0.187592474; -0.303530999    -0.934172359    0.187592474; 0.794654472 -0.577350269    0.187592474; 0.303530999 0.934172359 -0.187592474; -0.794654472    0.577350269 -0.187592474; -0.794654472    -0.577350269    -0.187592474; 0.303530999 -0.934172359    -0.187592474; 0.982246946 0   -0.187592474; 0.187592474 0.577350269 -0.794654472; -0.491123473    0.35682209  -0.794654472; -0.491123473    -0.35682209 -0.794654472; 0.187592474 -0.577350269    -0.794654472; 0.607061998 0   -0.794654472')

#Calculation
DiceNumbers = np.arange(d)+np.ones(d)
Divisors = np.arange(d)
Divisors[0] = 1
Best = np.array([0, 1000])
Worst = np.array([0, 0])
for i in range(1,d):
    Divisors[i] = mp.factorial(Divisors[i])
loop = int((mp.factorial(d-1)))
for i in range(0,loop):
    Numbering = np.remainder((np.floor(np.divide(i,Divisors))),DiceNumbers)
    String = np.ones(1)
    for j in range(2,d+1):
        String = np.insert(String,int(Numbering[j-1]),j)
    Resultant = np.linalg.norm(np.dot(String,Vectors))
    if Resultant < Best[1]:
        Best = np.array([int(i), Resultant])
    if Resultant > Worst[1]:
        Worst = np.array([int(i), Resultant])
    if Resultant < 0.19:
        print(i, String, Resultant)

#Print best and worst
i = int(Best[0])
Numbering = np.remainder((np.floor(np.divide(i,Divisors))),DiceNumbers)
String = np.ones(1)
for j in range(2,d+1):
    String = np.insert(String,int(Numbering[j-1]),j)
print('Best: ', i, String, Best[1])

i = int(Worst[0])
Numbering = np.remainder((np.floor(np.divide(i,Divisors))),DiceNumbers)
String = np.ones(1)
for j in range(2,d+1):
    String = np.insert(String,int(Numbering[j-1]),j)
print('Worst: ', i, String, Worst[1])
