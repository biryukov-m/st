#
#
# Пример № 1
#
# def f(x, y):
#     try:
#         return x/y
#     except:
#         print('Ошибочка')
# f(5, 0)
# f(5, '3')

# Пример № 2
# try:
#     x = [1, 2, 'hello', 3]
#     x.sort()
#     print(x)
# except TypeError:
#     print('I catched Type error')

# Пример № 3
# try:
#     5/0
# except ZeroDivisionError:
#     print('OOPS')
# print(TypeError.mro())

# Пример № 4
errors = (ZeroDivisionError,)
def divide(x,y):
    try:
        result = x/y
    except errors as e:
        print(e)
        print('x/0 ? No no no')
    else:
        print('Result is', result)
    finally:
        print('Fin.')

# divide(2,1)
divide(2,0)
# divide(2,[])
