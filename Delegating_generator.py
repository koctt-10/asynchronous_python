

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g     
    return inner


class BlaBlaExeption(Exception):
    pass


@coroutine
def subgen():
    while True:
        try:
            message = yield
        except BlaBlaExeption:
            #print('drop')
            break
        else:
            print(f'........{message}')
    
    return 'Returned from subgen()'
        

@coroutine
def delegator(g):
    while True:
        try:
            data = yield
            g.send(data)
        except BlaBlaExeption as e:
            g.throw(e)
            
    result = yield from g
    print(result)