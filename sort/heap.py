
class Heap():
    def __init__(self):
        self.queue = []
    
    def insert(self, x):
        self.queue.append(x)
        last_index = len(self.queue) - 1
        # 마지막 단말 노드
        while 0 <= last_index:
            # 부모 노드
            parent = self.parent(last_index)
            if 0 <= parent and self.queue[parent] < self.queue[last_index]:
                # swap
                self.queue[parent], self.queue[last_index] = self.queue[last_index], self.queue[parent]
                last_index = parent
            else:
                break
    
    def delete(self):
        last_index = len(self.queue) - 1
        # swap
        self.queue[0], self.queue[last_index] = self.queue[last_index], self.queue[0]
        max_value = self.queue.pop()
        # heapify
        self.heapify(0)
        return max_value

    def heapify(self, i):
        left, right = self.left_child(i), self.right_child(i)
        max_idx = i
        
        if left <= len(self.queue)-1 and self.queue[left] > self.queue[max_idx]:
            max_idx = left
        if right <= len(self.queue)-1 and self.queue[right] > self.queue[max_idx]:
            max_idx = right
            
        if max_idx != i:
            # swap
            self.queue[i], self.queue[max_idx] = self.queue[max_idx], self.queue[i]
            self.heapify(max_idx)
            
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return index*2 + 1
    
    def right_child(self, index):
        return index*2 + 2
    
    
def heap_sort(x):
    heap = Heap()
    for i in x:
        heap.insert(i)
        
    answer = []
    while heap.queue:
        answer.append(heap.delete())
    
    return answer
    
    
    
    
    
    