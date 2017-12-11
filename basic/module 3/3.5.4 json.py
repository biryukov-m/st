import json

tree = [  # тестовый граф наследования в виде json-объекта
    {'name': 'G', 'parents': ['F']},
    {'name': 'A', 'parents': []},
    {'name': 'B', 'parents': ['A']},
    {'name': 'C', 'parents': ['A']},
    {'name': 'D', 'parents': ['B', 'C']},
    {'name': 'E', 'parents': ['D']},
    {'name': 'F', 'parents': ['D']},
    {'name': 'X', 'parents': []},
    {'name': 'Y', 'parents': ['X', 'A']},
    {'name': 'Z', 'parents': ['X']},
    {'name': 'V', 'parents': ['Z', 'Y']},
    {'name': 'W', 'parents': ['V']},
]
# tree = json.loads(input())
classes = {i['name']: 1 for i in tree}
for di in tree:
    for ke in di['parents']:
        classes[ke] += 1
out = [print(key, ':', classes[key]) for key in sorted(classes.keys())]