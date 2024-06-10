import sympy as sp

def solveZeroState(a, b, y0):
    """
    Resolve a equação diferencial homogênea de primeira ordem:
    a(x) y' + b(x) y = 0

    Parâmetros:
    a (sympy expression): coeficiente de y'
    b (sympy expression): coeficiente de y
    y0 (float): condição inicial y(0)
    
    Retorna:
    solução geral (sympy expression)
    solução particular com constante (sympy expression)
    """
    # Definir a variável independente e a função dependente
    x = sp.symbols('x')
    y = sp.Function('y')

    # Definir a equação diferencial homogênea
    ode = a*sp.diff(y(x), x) + b*y(x)

    # Resolver a equação diferencial
    sol = sp.dsolve(ode, y(x))

    # Extrair a função geral de solução
    gen_sol = sol.rhs

    # Determinar a constante de integração usando a condição inicial
    C1 = sp.symbols('C1')

    # Substituir a solução geral na forma C1
    particular_sol = gen_sol.subs(sp.symbols('C1'), C1)

    # Definir a equação com base na condição inicial
    eq = sp.Eq(particular_sol.subs(x, 0), y0)

    # Resolver para a constante C1
    constant = sp.solve(eq, C1)[0]

    print("C = ", constant)

    # Substituir a constante na solução geral
    particular_sol = gen_sol.subs(C1, constant)

    print("Solução geral:")
    sp.pprint(sol)

    print("\nSolução particular com condição inicial:")
    sp.pprint(particular_sol)