# evolutionary algorithm, made by Musab Schluck,
# it's a simple example to illustrate how to use
# genetic algorithm to approximate a solution of
# the equation 2930 = ax + bx^2 + cx^3 + dx^4
# in order to approximate a, b, c, d
# i presented a solution which is 1x + 2x^2 + 3x^3 + 4x^4
# then we lit the program find a population of solutions

#  -------------- The Algorithm -------------- #
# Initialisation
# Evaluation	<--------------<---------
# Terminate?	- if reach goal finish	^
# Selection								-
# Variation 	- go back to Evaluation	>
# -------------------------------------------- #

# Goal = 1x + 2x^2 + 3x^3 + 4x^4, where x = 5
# 2930 = ax + bx^2 + cx^3 + dx^4 
# find a,b,c,d using Evolutionary algorithm

from random import uniform
from copy import copy
# I used the copy module in order to not have a referance of the variable p

def sorting_function(l):
	'''takes a solution and returns the difference between its value and the desired value'''
	x = 5
	a, b, c, d = l[0], l[1], l[2], l[3]
	return abs(2930 - (a*x + b*x**2 + c*x**3 + d*x**4))

# Initialisation
# Making a population of 100 solution that are randomly chosen from a uniform distribution
p = []		# p = [ [a1,b1,c1,d1], [a2,b2,b3,c4], .. ]
for i in range(100):
	p.append([uniform(-100, 100), uniform(-100, 100),
		uniform(-100, 100), uniform(-100, 100)])

while True:
	# Evaluation
	p.sort(key = sorting_function)

	# Terminate?
	tolerance = 0.001
	if sorting_function(p[0]) < tolerance:
		print('best solution score:',sorting_function(p[0]))
		print('Top 10 best solutions:\n',p[0:10])
		break

	# Selection
	p = p[0:50]

	# Variation
	p2 = copy(p)
	for i in p2:
		p.append([uniform(i[0]-5, i[0]+5),
			uniform(i[1]-5, i[1]+5),
			uniform(i[2]-5, i[2]+5),
			uniform(i[3]-5, i[3]+5)])