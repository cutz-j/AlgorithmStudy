################ IMPOSSIBLE !! ###################
############### OFFLINE SEARCH ####################
def num_generator(num=1983):
    A = (num * 214013 + 2531011)%(2**32)
    res = num % 10000 + 1
    return A, res

class Generator:
    def __init__(self):
        self.seed = 1983

    def next_(self):
        ret = self.seed
        self.seed = ((self.seed * 214013) + 2531011)%(2**32)
        return ret % 10000 + 1
    

class Queue:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop(0)
    
    def empty(self):
        return not self.items
    
    def top(self):
        return self.items[0]
    


C = input()
for i in range(int(C)):
    K, N = input(), input()
    queue = Queue()
    cnt, range_sum = 0, 0
    gen = Generator()
    for j in range(int(N)):
        new_num = gen.next_()
        range_sum += new_num
        queue.push(new_num)
        
        while(range_sum > int(K)):
            range_sum -= queue.top()
            queue.pop()
        
        if range_sum == int(K):
            cnt += 1
    print(cnt)
