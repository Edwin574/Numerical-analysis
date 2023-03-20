#determining the root using bisection method

def equation(x):
    return x**3-2*x - 5


a = 2
b = 3


tolerance = 1e-6
maxiterations = 100
iterations = 0

for i in range(maxiterations):

    c = (a+b)/2
    iterations += 1
    if abs(equation(c)) < tolerance:
        print(f'root found at x={c:.6f}')
        break
    elif equation(c)*equation(a) < 0:
        b = c
    else:
        a = c

print((iterations))
