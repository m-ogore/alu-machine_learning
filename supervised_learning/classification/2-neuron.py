#!/usr/bin/env python3

import numpy as np

class Neuron:
    def __init__(self, nx):
        
        #Initializes the object with the given nx value.

        #Parameters:
        #    nx (int): The value to initialize nx with.

        #Raises:
        #   TypeError: If nx is not an integer.
        #  ValueError: If nx is less than 1.
        
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        
        self.nx = nx
        self.__W = np.random.normal(size=(1,nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        
        #Get the value of the property W.

        return self.__W

    @property
    def b(self):
        
        #Get the value of the 'b' property.
        
        return self.__b

    def A(self):
        
        #Returns the value of the private attribute __A.

        return self.__A

    def forward_prop(self, X):
        """
        Performs forward propagation on the given input data.

        Parameters:
            X (numpy.ndarray): The input data with shape (nx, m).
                nx (int): The number of input features to the neuron.
                m (int): The number of examples.

        Returns:
            A (numpy.ndarray): The output of the forward propagation.
        """
        #X is a numpy.ndarray with shape (nx, m) that contains the input data
        # nx is the number of input features to the neuron
        # m is the number of examples


        self.nx = X.shape[0]
        m = X.shape[1]

        X = np.ndarray((self.nx, m))
        z =  z = np.matmul(self.__W, X) + self.__b
        self.__A =1 / (1 + np.exp(-z))
        return A        