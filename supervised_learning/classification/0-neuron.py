#!/usr/bin/env python3
from numpy import random

'''
class constructor: def __init__(self, nx):
nx is the number of input features to the neuron
If nx is not an integer, raise a TypeError with the exception: nx must be an integer
If nx is less than 1, raise a ValueError with the exception: nx must be a positive integer
All exceptions should be raised in the order listed above
Public instance attributes:
W: The weights vector for the neuron. Upon instantiation, it should be initialized using a random normal distribution.
b: The bias for the neuron. Upon instantiation, it should be initialized to 0.
A: The activated output of the neuron (prediction). Upon instantiation, it should be initialized to 0.

'''

class Neuron:
    def __init__(self, nx):
        self.nx = nx

        if not isinstance(self.nx, int):
            raise TypeError('nx must be an integer')
        if self.nx < 0:
            raise ValueError('nx must be a positive integer')
        
        self.w = random.normal()
        self.b = 0
        self.A = 0

    