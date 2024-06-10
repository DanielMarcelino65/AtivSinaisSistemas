import sympy as sp

def zeroInputFirstOrderODE(a, b, y0):
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    ode = sp.Eq(a * y.diff(t) + b * y, 0)  
    print("The differential equation is:")
    sp.pprint(ode)
    print()
    
    general_solution = sp.dsolve(ode)
    print("The general solution to the ODE is:")
    sp.pprint(general_solution)
    print()
    
    C1 = sp.symbols('C1')
    
    initial_condition_eq = general_solution.rhs.subs(t, 0) - y0
    print("Setting initial condition:")
    sp.pprint(initial_condition_eq)
    print()
    
    constant_solution = sp.solve(initial_condition_eq, C1)
    
    if constant_solution:
        C1value = constant_solution[0]
        particular_solution = general_solution.subs(C1, C1value)
        print("C1 =", C1value)
        print("\nThe particular solution to the ODE with the given initial condition is:")
        sp.pprint(particular_solution)
    else:
        print("Error: Unable to find a solution for the constant.")

# Example usage
zeroInputFirstOrderODE(a=1, b=1, y0=1)