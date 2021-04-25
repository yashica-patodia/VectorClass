# VectorClass
Implementation of vector class in python representing the coordinates of a vector in multidimensional space.For example, in a
three-dimensional space, we might wish to represent a vector with coordinates 5, −2, 3 .
Although it might be tempting to directly use a Python list to represent those
coordinates, a list does not provide an appropriate abstraction for a geometric vector. In
particular, if using lists, the expression [5, −2, 3] + [1, 4, 2] results in the list [5, −2, 3, 1,
4, 2]. When working with vectors, if u = 5, −2, 3 and v = 1, 4, 2 , one would expect the
expression, u + v, to return a three-dimensional vector with coordinates 6, 2, 5.

I  therefore tried to define a Vector class, in Vector.py, that provides a better abstraction
for the notion of a geometric vector. Internally, the vector should rely upon an instance
of a list, named _coords, as its storage mechanism. By keeping the internal list
encapsulated, it should be able to enforce the desired public interface for instances of
our class.
