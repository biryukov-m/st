class Buffer:
    def __init__(self):
        self.pool = []

    def add(self, *a):
        for i in range(len(a)):
            if len(self.pool) == 4:
                print(sum(self.pool, a[i]))
                self.pool.clear()
            else:
                self.pool.append(a[i])

    def get_current_part(self):
        return self.pool

buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part())
buf.add(4, 5, 6)
print(buf.get_current_part())
buf.add(7, 8, 9, 10)
print(buf.get_current_part())
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
print(buf.get_current_part()) # вернуть [1]
