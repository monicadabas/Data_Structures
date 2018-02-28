# Binary Min heap implementation

class Heap:
    def __init__(self):
        self.heap_size = 0
        self.array = []

    # restores the heap property when an element is added
    def heapify_up(self, i):
        if i > 0:
            parent_i = int((i-1)/2) # index of parent of i
            if self.array[parent_i] > self.array[i]:
                self.array[parent_i], self.array[i] = self.array[i], self.array[parent_i]
                self.heapify_up(parent_i)

    def insert_element(self, x):
        self.array.append(x)
        self.heap_size += 1
        if self.heap_size > 1:
            self.heapify_up(self.heap_size-1)

    # only returns the minimum which is at index 0
    def find_min(self):
        if self.heap_size > 0:
            return self.array[0]
        else:
            print("Empty heap")
            return

    # restores the heap property when an element is deleted
    def heapify_down(self, i):
        left_child = int(i*2+1)
        right_child = int(i*2+2)
        smallest = i

        if left_child < int(self.heap_size/2+1) and self.array[left_child] < self.array[i]:
            smallest = left_child

        if right_child < int(self.heap_size/2+1) and self.array[right_child] < self.array[smallest]:
            smallest = right_child

        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.heapify_down(smallest)

    # deletes minimum from root and does not return anything
    def delete_min(self):
        if self.heap_size == 0:
            print("Empty heap")
        else:
            self.array[0], self.array[self.heap_size-1] = self.array[self.heap_size-1], self.array[0]
            self.array.pop()
            self.heap_size -= 1
            self.heapify_down(0)

    # deletes the minimum which is at index 0 and also returns it
    def extract_min(self):
        minimum = self.find_min()
        if minimum is not None:
            self.delete_min()
        return minimum

    def print_heap(self):
        if self.heap_size == 0:
            print("Empty heap")
        else:
            print(self.array)


# create a min heap from a list of elements

def get_smallest(A, i):
    l = len(A)
    left = int(i*2 + 1)
    right = int(i*2 + 2)
    smallest = i
    if left < l and A[left] < A[i]:
        smallest = left

    if right < l and A[right] < A[smallest]:
        smallest = right

    return smallest


def heapify(A, i):
    if i > 0:
        parent_i = int((i-1)/2)
        if A[parent_i] > A[i]:
            A[parent_i], A[i] = A[i], A[parent_i]
        heapify(A, parent_i)
        smallest = get_smallest(A, i)
        if smallest != i:
            A[smallest], A[i] = A[i], A[smallest]


def build_heap(elements_list):
    length = len(elements_list)

    for i in range(length-1, int(length/2)-1, -1):
        heapify(elements_list, i)
    print(elements_list)


# min heap sort
def heapify_down(A, i):
    if i >= 0:
        smallest = get_smallest(A, i)
        if smallest != i:
            A[smallest], A[i] = A[i], A[smallest]
            heapify_down(A, smallest)


def heap_sort(A):
    sorted_A = []
    build_heap(A)
    l = len(A)
    for i in range(l):
        sorted_A.append(A[0])
        A[0], A[-1] = A[-1], A[0]
        A.pop()
        heapify_down(A, 0)

    return sorted_A


