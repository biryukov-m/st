# namespaces = {'parent': {'namespace': ['value1', 'value2']}}
namespaces = dict(parent={'namespace': ['value1', 'value2']}, parent2={'namespace2': ['value3', 'value4']})

# print(len(namespaces['parent']))
# print(namespaces['parent']['namespace'])
# print()
# print(namespaces.keys())
# print()
# print(namespaces.values())
# print(namespaces['parent2']['namespace2'])
# print(namespaces['parent2']['namespace2'][0])


nms = 'namespace'
val = 'value1'

for key, value in namespaces.items():
    for n in value:  # перебираем все неймспейсы
       # print(n)
       if n == nms:
           print("нашли неймспейс: ", n)
           print("вот где он: ", value)
           print(len(value.values()))
           for q in value.values():
               if val in q:
                   print("Опля")
                   print('Парент -  ', key)

           # if val in value.items():
           #     print("А в нем нашли переменную")
           # for va in n:
           #     print(va)







       # когда нашли нужный нам,