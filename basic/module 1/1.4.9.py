n = int(input()) # количество запросов
# n = 9
def get (nms, var):
    if var in namespaces[nms]:
        return nms
    # найти парента nms
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
        # print(namespaces)
        # print(parents)
        # print(parents.get(varParentArg))
        # print()
    if comArg == 'add':
        namespaces[namespaceArg] += [varParentArg]
        # print(namespaces)
        # print(parents)
        # print()
    if comArg == 'get':
        # print(namespaces)
        # print(parents)
        # print()
        print(get(namespaceArg,varParentArg))
        # print('namespaces.get(var)  =   ', namespaces.get(varParentArg))
        # for key, v in namespaces.items():
        #     if v == varParentArg:
                # print('So value found in newspace: ', key)
    print('Namespaces = ', namespaces)
    print('Parents = ', parents)
#
