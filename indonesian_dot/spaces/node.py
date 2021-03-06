from math import sqrt

"""
Creates a node, forming the basis of a graph or tree.

----------
Parameters
----------

state : str
    The state of this node as a string. 

predecessor : Node
    A predecessor of this node.

previous_action : int
    An action that resulted from the creation of this node from the predecessor node. 
    The range is [0, len(state) - 1].

g : int
    The cost from the predecessor node to this node.

h : int
    The estimated cost from this node to the goal node.

f : int
    The estimated cost from the predecessor node to the goal node.

depth : int
    The depth of this node. 
    This parameter is not enforced.
    Note: predecessor's depth + 1 = this node's depth

length : int
    returns the length of this node.
    Note: this is not the size of the node.

width : int
    returns the same result as length since this node contains the same length and width.

size : int
    returns the total size of this node as length * width, or simply len(state).
    
-------
Methods
-------

__eq__(other) -> {None, True, False}
    returns True iff the other object is an instance of a Node, and they have the same f, g, h and state parameters 

__str__() -> str
    return the state of the node.
    
__le__(other) -> {None, True, False}
    return True iff the function and the state of this object is less than or equal to the other object's.
    
__lt__(other) -> {None, True, False}
    return True iff the function and the state of this object is less than the other object's.

__ge__(other) -> {None, True, False}
     return True iff the function and the state of this object is greater than or equal to the other object's.
     
__gt__(other) -> {None, True, False}
    return True iff the function and the state of this object is greater than the other object's.
    
__cmp__(other) -> {None, -1, 0, 1}
    returns -1 if the function and the state of this object is less than the other.
    0 if it's equal to the other object's.
    1 if it's greater than the other object's.
    None if that object is not of type Node.
    
__contains__(item) -> {None, True, False}
    return True if the item state is contained in this object.

__len__() -> int
    return the length of the state this node is wrapped around.
    Note: the length is defined as the length of a square, and not the size of the square.
    
touch(action) -> Node
    touches the adjacent tokens of this node based on action, and returns a new node pointing to this node.
    This node effectively becomes a predecessor.
    
search_artifact() -> str
    return the string representation of a search artifact: f, g, h and this state.
    Example: 0 0 0 010111010

solution_artifact() -> str
    return the string representation of a solution artifact: action taken to get to this state.
    Example: B2 000000000
    
"""


class Node:
    def __init__(self, state, predecessor=None, action=None):
        self._predecessor = predecessor
        self._previous_action = action
        self._state = state

        self._depth = 0 if not predecessor else predecessor.depth + 1
        self._g = 0
        self._h = 0
        self._f = 0
        self._size = len(state)
        self._length = int(sqrt(self._size))

    @property
    def length(self):
        return self._length

    @property
    def width(self):
        return self._length

    @property
    def size(self):
        return self._size

    @property
    def depth(self):
        return self._depth

    @property
    def f(self):
        return self._f

    @property
    def g(self):
        return self._g

    @property
    def h(self):
        return self._h

    @g.setter
    def g(self, new_g):
        self._g = new_g
        self._f = new_g + self._h

    @h.setter
    def h(self, new_h):
        self._h = new_h
        self._f = new_h + self._g

    @property
    def predecessor(self):
        return self._predecessor

    @property
    def previous_action(self):
        return self._previous_action if self._previous_action is not None else -1

    @property
    def state(self):
        return self._state

    def __eq__(self, other):
        return hash(self._state) == hash(other._state)

    def __str__(self):
        return self._state

    def __le__(self, other):
        return not self > other

    def __lt__(self, other):
        return other._f > self._f or (self._f == other._f and self._state < other._state)

    def __ge__(self, other):
        return not self > other

    def __gt__(self, other):
        return not self < other

    def __contains__(self, item):
        return self._state == item

    def __len__(self):
        return self.length

    def __iter__(self):
        for x in self._state:
            yield int(x)

    def __hash__(self):
        return hash(self._state)

    def touch(self, action):

        size = len(self._state) - 1
        length = self._length
        integer_action = 2 ** (size - action)

        if action - length >= 0:
            integer_action += 2 ** (size - (action - length))

        if action + length <= size:
            integer_action += 2 ** (size - (action + length))

        if action % length > 0:
            integer_action += 2 ** (size - (action - 1))

        if action % length < length - 1:
            integer_action += 2 ** (size - (action + 1))

        new_state = int(self._state, 2) ^ integer_action
        new_state = f'{new_state:0{self._size}b}'

        return Node(new_state, self, action)

    def search_artifact(self):
        return f'{self._f} {self._g} {self._h} {self._state}'

    def solution_artifact(self):
        if self._previous_action is None:
            return f'0 {self._state}'
        else:
            row, column = divmod(self._previous_action, self._length)

            row = chr(row + ord('A'))
            return f'{row}{column + 1} {self._state}'
