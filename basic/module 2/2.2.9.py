lst = [1, 2, 3, 4, 5, 6]
book = {'title': 'Gondoleri',
        'author': 'Papa Romanian XVI',
        'year published': '1999'}
string = 'Hola amigos!'

# for i in book.items():
#     print(i)

iterator = iter(book)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))