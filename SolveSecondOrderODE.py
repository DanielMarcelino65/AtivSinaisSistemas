import numpy as np
from scipy.integrate import solve_ivp
import sympy as sp

def secondOrderModel(t, y, a, b, c, d):
    dydt = y[1]
    dzdt = -(b * y[1] + c * y[0] + d) / a
    return [dydt, dzdt]

def solveSecondOrderODE(a, b, c, d, y0, yd0):
    initial_conditions = [y0, yd0]
    time_span = [0, 0]
    
    # Solve the ODE numerically
    sol = solve_ivp(secondOrderModel, time_span, initial_conditions, args=(a, b, c, d), dense_output=True)
    
    t = sol.t
    y = sol.y[0]
    
    # Symbolic solution
    tSymbol = sp.symbols('t')
    ySymbol = sp.Function('y')(tSymbol)
    equation = sp.Eq(a * ySymbol.diff(tSymbol, tSymbol) + b * ySymbol.diff(tSymbol) + c * ySymbol + d, 0)
    
    general_solution = sp.dsolve(equation)
    constants = sp.symbols('C1 C2')
    
    # Apply initial conditions to solve for constants
    eq1 = general_solution.rhs.subs(tSymbol, 0) - y0
    eq2 = sp.diff(general_solution.rhs, tSymbol).subs(tSymbol, 0) - yd0
    
    constants_solution = sp.solve((eq1, eq2), constants)
    particular_solution = general_solution.subs(constants_solution)
    
    # Print results
    print("Numerical solution values:")
    for ti, yi in zip(t, y):
        print(f"t = {ti:.2f}, y(t) = {yi:.2f}")
    
    print("\nGeneral solution (symbolic):")
    sp.pprint(general_solution)
    
    print("\nValues of C1 and C2 (from symbolic solution):")
    for constant, value in constants_solution.items():
        print(f"{constant} = {value.evalf()}")
    
    print("\nParticular solution with constants:")
    sp.pprint(particular_solution)
    
    return t, y, particular_solution

# Example usage
t, y, particular_solution = solveSecondOrderODE(a=1, b=5, c=4, d=0, y0=1, yd0=0)
