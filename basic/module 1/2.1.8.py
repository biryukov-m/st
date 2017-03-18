class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError

vasa = PositiveList()
vasa.append(2)
print(vasa)
vasa.append(0)
print(vasa)
vasa.append(-1)


