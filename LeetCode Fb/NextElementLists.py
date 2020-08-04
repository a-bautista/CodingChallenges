import math

class NextElement:
    def __init__(self, arr):
        self.lists = arr
        self.idx = []
        for i in range(len(self.lists)):
            self.idx.append(0)

    def next_element(self):
        min = math.inf
        for i in range(len(self.lists)):
            if self.idx[i] == len(self.lists[i]): continue
            if self.lists[i][self.idx[i]] < min:
                min = self.lists[i][self.idx[i]]

        for i in range(len(self.lists)):
            if self.idx[i] == len(self.lists[i]): continue
            if self.lists[i][self.idx[i]] == min:
                self.idx[i] += 1

        return min if min != math.inf else -1

    def has_next_element(self):
        for i in range(len(self.idx)):
            if self.idx[i] + 1 < len(self.lists[i]): return True
        return False