# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/6_nn.ipynb.

# %% auto 0
__all__ = ['Neuron']

# %% ../nbs/6_nn.ipynb 3
import random
from .engine import Value

# %% ../nbs/6_nn.ipynb 4
class Neuron:

    def __init__(self, nin):
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(random.uniform(-1,1))
        
    def __call__(self,x):
        # w.x + b (w.x is a dot product)
        return 0.0
