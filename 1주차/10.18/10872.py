def set_open(input_):
    class open:
        def __init__(self, x):
            self.read = lambda: input_

        def __iter__(self):
            return iter(input_.split("\n"))
    return open

def set_input(input_):
    return iter(input_.split("\n")).__next__

input = set_input('''10''')



############################

N = int(input())

def fecto(n):
    if n == 0:
        return 1
    elif n ==1 :
        return 1
    else:
        return n * fecto(n-1)
    
print(fecto(N))