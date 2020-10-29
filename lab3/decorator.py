def print_result(func, *arg):


    def decorator(*arg):
        print(func.__name__)
        result = func(*arg)
        if type(result) is list:
            for item in result:
                print(item)
        elif type(result) is dict:
            for key, value in result.items():
                print(str(key) + ' = ' + str(value))
        else:
            print(result)
        return result
    return decorator



@print_result
def test1():
    return 1

@print_result
def test2():
    return 'iu5'

@print_result
def test3():
    return {'a': 1, 'b': 2}

@print_result
def test4():
    return [1, 2]

if __name__ == '__main__':
    print('!!!!!!!!')
    test1()
    test2()
    test3()
    test4()