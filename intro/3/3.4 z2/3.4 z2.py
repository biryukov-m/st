inf = open('dataset.txt', 'r')
textStr = ''
with open('dataset.txt') as inf:
    for line in inf:
        line = line.strip().lower()
        textStr += line
words = textStr.split()
#
# Решение с помощью списка
words.sort()
words.reverse()
cnt = 0
topWord = ''
for word in words:
    if words.count(word) > cnt:
        cnt = words.count(word)
        topWord = word
print(topWord, cnt)
#
# Или с помощью словаря
# wordDic = {}
# for word in words:
#     if word not in wordDic:
#         wordDic[word] = 1
#     else:
#         wordDic[word] += 1
# longest = max(wordDic.values())
# topwords = []
# for key, item in wordDic.items():
#     if item == longest:
#         topwords += [key]
# print(max(topwords), longest)