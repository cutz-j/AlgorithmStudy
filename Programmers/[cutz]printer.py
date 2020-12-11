class Queue:
    def __init__(self):
        self.front, self.rear = 0, 0
        self.list = []
        self.pop_count = 0

    def append(self, x):
        self.list.append(x)
        self.rear += 1

    def pop(self):
        res = self.list[self.front]
        self.front += 1
        self.pop_count += 1
        return res

    def empty(self):
        return len(self.list) == self.pop_count


def solution(priorities, location):
    answer = 0
    queue = Queue()
    for idx, p in enumerate(priorities):
        queue.append((p, idx))

    sort_p = sorted(priorities, reverse=True)
    idx = 0
    while queue.empty() == False:
        item = queue.pop()
        if sort_p[idx] > item[0]:
            queue.append(item)
        else:
            answer += 1
            idx += 1
            if item[1] == location:
                break
    return answer