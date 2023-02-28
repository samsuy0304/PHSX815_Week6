#! /usr/bin/env python

# Necessary Libraries
import numpy as np
import matplotlib.pyplot as plt

#Importing the random class
from Random import Random

class Integration:

    #Initialization method for the Integration Class
    def __init__(self, f, a=0, b=np.pi):
        self.function = f
        self.lowlim = a
        self.highlim = b
    
    #Function for Midpoint rule
    def midpoint_rule(self, n):
        h = (self.highlim - self.lowlim) / n
        x = np.linspace(self.lowlim + h/2, self.highlim - h/2, n)
        return h * np.sum(self.function(x))

    #Function for gauss-legendre quadrature
    def gauss_quad(self):
        x = [-(3/5)**0.5, 0, (3/5)**0.5]
        w = [5/9, 8/9, 5/9]
        x_labels = [(self.highlim-self.lowlim)/2 * x_i + (self.highlim+self.lowlim)/2 for x_i in x]
        return (self.highlim-self.lowlim)/2 * np.dot(w, self.function(x_labels))

    def monte_carlo(self,n):
        rng = Random(5555)
        x = rng.Random_Range(self.lowlim, self.highlim, n)  # generate n random points in [a, b]
        fx = self.function(x)  # evaluate the function at the random points
        area = np.mean(fx) * (self.highlim - self.lowlim)  # estimate the area under the curve
        return area
