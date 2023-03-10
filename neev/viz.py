# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_viz.ipynb.

# %% auto 0
__all__ = ['trace', 'get_dot', 'view_dot']

# %% ../nbs/01_viz.ipynb 3
from fastdot import *
from IPython.display import SVG, display
from .engine import *

# %% ../nbs/01_viz.ipynb 6
def trace(root:Value):# root node of the computation graph
    '''builds a set of all nodes and edges in a graph'''
    nodes, edges = set(), set()
    def build(v):
        if v not in nodes:
            nodes.add(v)
            for child in v._prev:
                edges.add((child, v))
                build(child)
    build(root)
    return nodes, edges

# %% ../nbs/01_viz.ipynb 18
def get_dot(root:Value,# root node of the computation graph
            rankdir='LR'):# TB (top to bottom graph) | LR (left to right)
    """
    get a pydot graph corresponding to this computation graph
    """
    assert rankdir in ['LR', 'TB']
    
    def get_op_name(op):
        op_dict = {'+' : 'PL', '-': 'MN', 
                   '*' : 'MU', '/': 'DI', 
                   'tanh':'tanh','exp':'exp',
                   'ReLU':'ReLU'
                  }
        if op.startswith('**'):
            return (op
                    .replace('.','DOT')
                    .replace('**-','POWM')
                    .replace('**','POW')
                   )
        return op_dict[op]
    
    nodes, edges = trace(root)
    dot = Dot(rankdir=rankdir,directed=True)
    
    for n in nodes:
        # for any value in the graph, create a rectangular (`record`) node for it
        nd_label = f'{n.label} \n data {n.data:.4f} \n grad {n.grad:.4f}'
        nd_name = str(id(n))
        nd = dot.add_item(nd_label, name=nd_name, fillcolor=None)
#         print(f'node:{nd_label};name:{nd_name}')
        if n._op:
            # if this value is the result of some operation create an op node for it
            nd_op_name = get_op_name(n._op) + str(id(n))  
            nd_op = dot.add_item(n._op, 
                                 name=nd_op_name, fillcolor=None, 
                                 height=0.25, width=0.25)
#             print(f'node:{n._op};name:{nd_op_name}')
            # and connect this node to it
            dot.add_item(nd_op.connect(nd))
            
    for n1, n2 in edges:
        n1_nd_name = str(id(n1))
        n1_nd = dot.get_node(n1_nd_name)[0]
        n2_op_nd_name = get_op_name(n2._op) + str(id(n2))
        n2_op_nd = dot.get_node(n2_op_nd_name)[0]
#         print(f'Fetch: {n2_op_nd_name} is {n2_op_nd}')
        # connect n1 to the op node of n2
        dot.add_item(n1_nd.connect(n2_op_nd))
    
    return dot

# %% ../nbs/01_viz.ipynb 19
# https://stackoverflow.com/questions/4596962/display-graph-without-saving-using-pydot
# https://stackoverflow.com/questions/30334385/display-svg-in-ipython-notebook-from-a-function
def view_dot(root:Value):# root node of the computation graphg:pydot.Dot
    '''view the computation graph as a svg'''
    g = get_dot(root)
    svg = SVG(g.create_svg())
    display(svg)
