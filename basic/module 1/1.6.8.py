# Стековая машина или реверсивный польский калькулятор
class ExtendedStack(list):
    def sum(self):
        self.append((self.pop()+self.pop()))

    def sub(self):
        self.append((self.pop() - self.pop()))

    def mul(self):
        self.append((self.pop() * self.pop()))

    def div(self):
        self.append((self.pop() // self.pop()))

l = ExtendedStack()

l.append(50)
l.append(50)
l.sum()
print(l)
l.append(900)
l.mul()
print(l)