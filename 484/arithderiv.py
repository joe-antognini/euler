#! /usr/bin/env python

from math import sqrt

def smallest_factor(n):
  '''Return the smallest factor of an integer.'''

  for i in range(2, int(sqrt(n))):
    if n % i == 0:
      return i
  return 1

def arith_deriv(n):
  '''Calculate the arithmetic derivative.'''
  a = smallest_factor(n)
  if a == 1:
    return 1
  else:
    b = n / a
    return a * arith_deriv(b) + arith_deriv(a) * b
