# In this python file, only the definations for the magic functions and the basic operations
# for the question segments are provided. There may be the need to add new functions or overload
# existing ones as per the question requirements.

class Vector:

    def __init__(self, *args):
        # if arg is an int(dimension)
        if isinstance(args[0], int):
            self._coords = [0] * args[0]


        # if the argument is a list
        elif isinstance(args[0], list):
            self._coords = args[0].copy()

    # return the dimension of the vector
    def __len__(self):
        return len(self._coords)

    # return the jth coordinate of the vector
    def __getitem__(self, j):
        return self._coords[j]

    # set the jth coordinate of vector to val
    def __setitem__(self, j, val):
        self._coords[j] = val

    # u + v
    def __add__(self, other):
        n = len(other)
        m = len(self._coords)
        if n == m:
            vec = Vector(n)
            for i in range(n):
                vec[i] = self._coords[i] + other[i]
            return vec

        else:
            print("Vector of different dimensions cannot be added")

    # return True if vector has same coordinates as other
    def __eq__(self, other):
        n = len(other)
        m = len(self._coords)
        if n == m:

            for i in range(n):
                if self._coords[i] != other[i]:
                    return False
            return True

        else:
            return False

    # return True if vector differs from other
    def __ne__(self, other):
        if self._coords == other:
            return False
        else:
            return True

    # return the string representation of a vector within <>
    def __str__(self):
        n = len(self._coords)
        vec_str = ""
        if n == 0:
            return vec_str
        vec_str = "<"
        vec_str += str(self._coords[0])
        for i in range(n - 1):
            vec_str += ","
            vec_str += str(self._coords[i + 1])
        vec_str += ">"
        return vec_str

    # Soln for Qs. 2
    def __sub__(self, other):
        n = len(other)
        m = len(self._coords)
        if n == m:
            vec = Vector(n)
            for i in range(n):
                vec[i] = self._coords[i] - other[i]
            return vec

        else:
            print("Vector of different dimensions cannot be subtracted")

    # Soln for Qs. 3
    def __neg__(self):
        n = len(self._coords)
        vec = Vector(n)
        for i in range(n):
            vec[i] = -self._coords[i]
        return vec

    def __rmul__(self, value):
        return (self * value)

    # Soln for Qs. 4, 5 and 6
    def __mul__(self, other):
        n = len(self._coords)
        if isinstance(other, int):
            vec = Vector(n)
            for i in range(n):
                vec[i] = other * self._coords[i]
            return vec
        elif isinstance(self._coords, Vector):
            m = len(other)
            if m == n:
                dot_product = 0
                for i in range(n):
                    dot_product += other[i] * self._coords[i]
                return dot_product
            else:
                print("The dimensions need to be same")


# Add suitable print statements to display the results
# of the different question segments
def main():
    v1 = Vector(5)
    v2 = Vector(7)
    v3 = Vector([1, 2, 3, 4, 5])
    print("Testing and printing the different question segments ")

    print("Finding length")
    print(len(v1))
    print(len(v2))
    print(len(v3))
    print("\n")

    print("Printing the vectors")
    print("v1= "+str(v1))
    print("v2= "+str(v2))
    print("v3= "+str(v3))
    print("\n")

    for i in range(len(v1)):
        v1[i]=i+1
    print("New v1 "+str(v1))




    print("\n")
    print("Testing right multiplication with number: ")
    print(("3*v3 = " + str(3 * v3)))
    print("Testing left multiplication with number: ")
    print(("v3*3 = " + str(v3 * 3)))
    print("\n")

    print("Dot product for two vectors: ")
    print("v1*v3 = " + str(v1 * v3)+"\n")
    print("Addition of two vectors: ")
    print("v1 + v3 = " + str(v1 + v3)+"\n")
    print("Subtraction of two vectors: ")
    print("v1 - v3 = " + str(v1 - v3)+"\n")
    print("Negative operator of vector: ")
    print("-v3 = " + str(-v3)+"\n")
    print("\n")
    print("Testing equal to operator for vectors: ")
    print("v1 == v3 : " + str(v1 ==  v3))
    print("Testing not equal to operator for vectors: ")
    print("v2!= v1 : "+str(v2 != v1))
    print("Vector initialisation with iterator: ")
    v4 = Vector([x for x in range(2, 12, 3)])
    print("v4 = " + str(v4))




if __name__ == '__main__':
    main()
