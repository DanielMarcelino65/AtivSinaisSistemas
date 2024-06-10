import sympy as sp
from scipy.integrate import solve_ivp

def model(t, y, a, b):
    dydt = -(b/a) * y
    return dydt

def solveODE(a, b, y0):
    initial_conditions = [y0]
    time_span = [0, 0]  
    
    sol = solve_ivp(lambda t, y: model(t, y, a, b), time_span, initial_conditions, dense_output=True)

    t = sol.t
    y = sol.y[0]
    
    tSymbol = sp.symbols('t')
    ySymbol = sp.Function('y')(tSymbol)
    equation = sp.Eq(a * ySymbol.diff(tSymbol) + b * ySymbol, 0)
    
    general_solution = sp.dsolve(equation)
    C1 = sp.symbols('C1')
    
    particular_solution = general_solution.subs(C1, y0)
    
    print("Solução numérica:")
    for ti, yi in zip(t, y):
        print(f"t = {ti:.2f}, y(t) = {yi:.2f}")

    print("\nSolução geral (simbólica):")
    sp.pprint(general_solution)

    print("\nSolução particular com condição inicial:")
    sp.pprint(particular_solution)

# Example usage
solveODE(a=1, b=1, y0=1)