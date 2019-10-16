
def before(func):
    def newfunc():
        print('befor')
        func()
        print('after')
    return newfunc
@before
def now():
    print('2019')

def demo():
    now()

demo()