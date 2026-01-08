import ctypes

class DynamicArray:
    def __init__(self):
        self._n = 0  # count elements
        self._capacity = 1  # default capacity
        self.A = self._make_array(self._capacity)

    
    def __len__(self):
        return self._n


    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()

    
    def __getitem__(self, index):
        if index < 0 or index >= self._n:
            raise IndexError('Index out of bounds')
        return self.A[index]

    
    def append(self, value):
        if self._n == self._capacity:
            self.resize(2 * self._capacity)
        self.A[self._n] = value
        self._n += 1


    def resize(self, new_capacity):
        B = self._make_array(new_capacity)
        for i in range(self._n):
            B[i] = self.A[i]
        self.A = B
        self._capacity = new_capacity



if __name__ == "__main__":
    a = DynamicArray()
    a.append("a")
    a.append("b")
    a.append("c")

    print("len:", len(a))     # 3
    print(a[0], a[1], a[2])   # a b c

    for k in range(10):
        a.append(k)
    print("len:", len(a))
    print("capacity:", a._capacity)
    print("last element:", a[len(a) - 1])
