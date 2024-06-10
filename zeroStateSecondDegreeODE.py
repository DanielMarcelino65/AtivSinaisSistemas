import sympy as sp

def solve_homogeneous_ode(a, b, c, y0, dy0):
    """
    Resolve a equação diferencial homogênea de segunda ordem:
    a y'' + b y' + c y = 0

    Parâmetros:
    a (float): coeficiente de y''
    b (float): coeficiente de y'
    c (float): coeficiente de y
    y0 (float): condição inicial y(0)
    dy0 (float): condição inicial y'(0)
    
    Retorna:
    solução geral (sympy expression)
    solução particular com constantes (sympy expression)
    """
    # Definir a variável independente e a função dependente
    x = sp.symbols('x')
    y = sp.Function('y')

    # Definir a equação diferencial homogênea
    ode = a*sp.diff(y(x), x, x) + b*sp.diff(y(x), x) + c*y(x)

    # Resolver a equação diferencial
    sol = sp.dsolve(ode, y(x))

    # Extrair a função geral de solução
    gen_sol = sol.rhs

    # Determinar as constantes de integração usando as condições iniciais
    C1, C2 = sp.symbols('C1 C2')

    # Substituir a solução geral na forma C1 e C2
    particular_sol = gen_sol.subs(sp.symbols('C1'), C1).subs(sp.symbols('C2'), C2)

    # Definir as equações com base nas condições iniciais
    eq1 = sp.Eq(particular_sol.subs(x, 0), y0)
    eq2 = sp.Eq(sp.diff(particular_sol, x).subs(x, 0), dy0)

    # Resolver para as constantes C1 e C2
    constants = sp.solve((eq1, eq2), (C1, C2))

    # Substituir as constantes na solução geral
    particular_sol = gen_sol.subs(constants)

    print("Solução geral:")
    sp.pprint(sol)

    print("\nSolução particular com condições iniciais:")
    sp.pprint(particular_sol)


# Exemplo de uso
solve_homogeneous_ode(a=1, b=2, c=2, y0=1, dy0=-1)
