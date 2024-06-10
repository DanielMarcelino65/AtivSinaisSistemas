import sympy as sp

def zeroInputSecondDegreeODE(a, b, c, y0, dy0):
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    ode = sp.Eq(a * y.diff(t, t) + b * y.diff(t) + c * y, 0)  
    print("The differential equation is:")
    sp.pprint(ode)
    print()
    
    general_solution = sp.dsolve(ode)
    print("The general solution to the ODE is:")
    sp.pprint(general_solution)
    print()
    
    constants_solution = sp.solve((general_solution.rhs.subs(t, 0) - y0, sp.diff(general_solution.rhs, t).subs(t, 0) - dy0), dict=True)
    
    if constants_solution:
        constants_solution = constants_solution[0]
        particular_solution = general_solution.subs(constants_solution)
        print("The particular solution to the ODE with the given initial conditions is:")
        sp.pprint(particular_solution)
    else:
        print("Error: Unable to find a solution for the constants.")

# Exemplo de uso
zeroInputSecondDegreeODE(1, -6, 9, 2, 4)
