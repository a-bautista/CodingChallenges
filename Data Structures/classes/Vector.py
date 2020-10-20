def main():
    vector = Vector(5)
    print(vector.__len__())
    vector [1] = 23
    vector[-1] = 33

    vector2 = vector + vector # use the magic method __add__()
    print(vector2)


class Vector:
    '''Represents a vector in a multidimensional space'''

    def __init__(self, d):
        '''Create a d-dimensional vector of zeroes'''
        self._coords = [0]*d

    def __len__(self):
        '''Return the dimension of the vector.'''
        return len(self._coords)

    def __getitem__(self, j):
        '''Return the jth coordinate of vector.'''
        return self._coords[j]

    def __setitem__(self, j, val):
        '''Set the jth coordinate of vector to given value.'''
        self._coords[j] = val

    def __add__(self, other):
        '''Return the sum of 2 vectors'''
        if len(self)!=len(other):
            raise ValueError('Dimensions must agree.')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        '''Return True if vector has same coordinates as other.'''
        return self._coords == other._coords

    def __ne__(self, other):
        '''Return True if vector differs from other'''
        return not self == other

    def __str__(self):
        '''Produce string representating of vector'''
        return '<' + str(self._coords)[1:-1] + '>'

if __name__ == '__main__':
    main()


