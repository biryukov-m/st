n = int(input()) # количество запросов
def get (nms, var):
    if var in namespaces[nms]:
        return nms
    parent = 'None'
    for key, value in parents.items():
        if nms in value:
            parent = key
    if parent == 'None':
        return 'None'
    return get(parent,var)
namespaces = {'global':[]}
parents = {'None':'global'}
for c in range(n):
    comArg, namespaceArg, varParentArg = input().split()
    if comArg == 'create':
        if parents.get(varParentArg) is None:
            parents[varParentArg] = [namespaceArg]
        else:
            parents[varParentArg] += [namespaceArg]
        namespaces[namespaceArg] = []
    if comArg == 'add':
        namespaces[namespaceArg] += [varParentArg]
    if comArg == 'get':
        print(get(namespaceArg,varParentArg))