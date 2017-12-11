import test


# def array_diff(a, b):
#     result = []
#     for i in range(len(a)):
#         if a[i] not in b:
#             result.append(a[i])
#     return result



def array_diff(a, b):
    b = set(b)
    result = []
    for i in range(len(a)):
        if a[i] not in b:
            result.append(a[i])
    return result

print(array_diff([1, 2, 2, 3], [2]))
