errors = (ZeroDivisionError, ArithmeticError, AssertionError)
try:
    foo()
    # pass
# except errors as e:
#     print(str(e))
except ZeroDivisionError:
    print('ZeroDivisionError')
except ArithmeticError:
    print('ArithmeticError')
except AssertionError:
    print('AssertionError')