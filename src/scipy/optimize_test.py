import numpy as np
from scipy import optimize
from scipy.optimize import minimize
def f(x):
    return (x-3)**2 + 10

x0 = np.array([0])
res = minimize(f, x0)

print("Optimal for x:", res.x)
print("Function value:", res.fun)



def bond_price(y):
    C = 5
    F = 100
    P = 95
    N = 3
    return sum(C/(1+y)**t for t in range(1, N+1)) + F/(1+y)**N - P

ytm = brentq(bond_price, 0.0001, 1.0)