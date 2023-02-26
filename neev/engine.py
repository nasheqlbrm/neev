# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_engine.ipynb.

# %% auto 0
__all__ = ['Value']

# %% ../nbs/00_engine.ipynb 3
import math
import numpy as np
import matplotlib.pyplot as plt

# %% ../nbs/00_engine.ipynb 22
class Value:
    '''stores a single scalar value and its gradient'''
    def __init__(self, 
                 data,# a scalar value
                 _children=(),# The children of this value
                 _op='',# The operation that created this value
                 label=''):
        self.data, self._prev, self._op = data, set(_children), _op
        self.label, self.grad = label, 0
        
    def __add__(self, other):
        out = Value(self.data + other.data, (self,other), '+')
        return out
    
    def __mul__(self, other):
        out = Value(self.data * other.data, (self,other),'*')
        return out
    
    def __repr__(self):
        return f'Value(data={self.data})'
