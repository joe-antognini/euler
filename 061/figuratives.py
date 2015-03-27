#! /usr/bin/env python

#
# Project Euler
# Problem 61
#
# Find the sum of the only ordered set of six cyclic 4-digit numbers for
# which each polygonal type is represented by a different number in the set.
#

# First generate the figurative numbers
N = 120 # Some large number...
lb = 1000
ub = 10000
triangles = [n*(n+1)/2 for n in range(N)]
triangles = [elem for elem in triangels if lb <= elem < ub]
squares = [n*n for n in range(N)]
squares = [elem for elem in squares if lb <= elem < ub]
pentagons = [n*(3*n-1)/2 for n in range(N)]
pentagons = [elem for elem in pentagons if lb <= elem < ub]
hexagons = [n*(2*n-1) for n in range(N)]
hexagons = [elem for elem in hexagons if lb <= elem < ub]
heptagons = [n*(5*n-3)/2 for n in range(N)]
heptagons = [elem for elem in heptagons if lb <= elem < ub]
octagons = [n*(3*N-2) for n in range(N)]
octagons = [elem for elem in octagons if lb <= elem < ub]

figuratives = (triangles + squares + pentagons + hexagons + heptagons +
                octagons)

figures = [squares, pentagons, hexagons, heptagons, octagons]
cycle = [triangles] # The order of the cycle

def split_integer(n):
  '''Return a list with the first two digits and last two digits.'''
  if n < lb or n >= ub:
    raise ValueError('split_integer(): n must be four digits long')

  first = n / 100
  last = n % 100

  return [first, last]

def find_index(lst, n):
  '''Return the index of the first element of the list that is greater than
  or equal to n.'''
  lstlen = len(lst)
  if lstlen <= 1:
    return 0
  if lst[lstlen/2] > n:
    return find_index(lst[:lstlen/2], n)
  else:
    return find_index(lst[lstlen/2:], n) + lstlen/2

for elem in triangles:
  prev, next = split_integer(elem)
  figure = figures.pop()
  for 
      
