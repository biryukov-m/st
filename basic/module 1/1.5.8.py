class MoneyBox:
    def __init__(self, v):
        self.capacity = v
        self.inside = 0

    def can_add(self, v):
        return self.inside+v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.inside += v

xnxx = MoneyBox(100)
print(xnxx.inside)
xnxx.add(10)
print(xnxx.inside)
xnxx.add(89)
print(xnxx.inside)
xnxx.add(2)
print(xnxx.inside)
xnxx.add(1)
print(xnxx.inside)
print(xnxx.can_add(1))
print(xnxx.can_add(2))
print(xnxx.can_add(0))