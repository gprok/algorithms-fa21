
class Heap:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        for v in self.heap:
            print(v, end=" ")
        print()

    def insert(self, v):
        self.heap.append(v)
        self.heapify_up()

    def heapify_up(self):
        pos = len(self.heap) - 1
        while pos > 0:
            parent_pos = self.parent(pos)
            if self.heap[parent_pos] < self.heap[pos]:
                self.heap[parent_pos], self.heap[pos] = self.heap[pos], self.heap[parent_pos]
                pos = parent_pos
            else:
                break

    def get_max(self):
        if self.is_empty():
            return None
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop(-1)
        self.heapify_down()
        return max

    def heapify_down(self):
        pos = 0
        while pos is not None:
            max_ch_pos = self.max_child(pos)
            if max_ch_pos is not None:
                if self.heap[max_ch_pos] > self.heap[pos]:
                    self.heap[max_ch_pos], self.heap[pos] = self.heap[pos], self.heap[max_ch_pos]
                else:
                    break
            pos = max_ch_pos

    def parent(self, p):
        return (p - 1) // 2

    def max_child(self, p):
        left = self.child(p, 1)
        right = self.child(p, 2)
        if left is None:
            return None
        elif right is None:
            return left
        else:
            return left if self.heap[left] > self.heap[right] else right

    def child(self, p, k):
        pos = 2 * p + k
        if pos >= len(self.heap):
            return None
        else:
            return pos


if __name__ == '__main__':
    heap = Heap()
    print(heap.get_max())
    heap.insert(30)
    heap.insert(67)
    heap.insert(4)
    heap.insert(54)
    heap.insert(12)
    heap.insert(44)
    heap.insert(90)
    heap.insert(16)
    heap.display()
    print("===========")
    heap.get_max()
    heap.display()
    heap.get_max()
    heap.display()
