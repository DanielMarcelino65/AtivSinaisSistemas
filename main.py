import sympy as sp
import os

def zeroInputFirstDegreeODE():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    # Define a EDO
    ode = sp.Eq(y.diff(t) + 3 * y, 0)
    print("A equação diferencial é:")
    sp.pprint(ode)
    print()
    
    # Resolve a EDO para obter a solução geral
    general_solution = sp.dsolve(ode)
    print("A solução geral da EDO é:")
    sp.pprint(general_solution)
    print()
    
    # Condição inicial
    y0 = 2
    
    # Extrai o símbolo da constante C1
    C1 = sp.symbols('C1')
    
    # Substitui t=0 e y(0)=y0 na solução geral e resolve para C1
    initial_condition_eq = general_solution.rhs.subs(t, 0) - y0
    print("Definindo a condição inicial:")
    sp.pprint(initial_condition_eq)
    print()
    
    constant_solution = sp.solve(initial_condition_eq, C1)
    
    if constant_solution:
        C1_val = constant_solution[0]
        particular_solution = general_solution.subs(C1, C1_val)
        print("C1 =", C1_val)
        print("\nA solução particular da EDO com a condição inicial dada é:")
        sp.pprint(particular_solution)
    else:
        print("Erro: Não foi possível encontrar uma solução para a constante.")

def zeroInputSecondDegreeODE():
    t = sp.symbols('t')
    y = sp.Function('y')(t)
    
    # Define a EDO
    ode = sp.Eq(y.diff(t, t) + 2 * y.diff(t) + y, 0)
    print("A equação diferencial é:")
    sp.pprint(ode)
    print()
    
    # Resolve a EDO para obter a solução geral
    general_solution = sp.dsolve(ode)
    print("A solução geral da EDO é:")
    sp.pprint(general_solution)
    print()
    
    # Condições iniciais
    y0 = 1
    dy0 = 0
    
    # Encontra os símbolos das constantes (C1, C2) e resolve para elas usando as condições iniciais
    constants = list(general_solution.rhs.free_symbols)
    C1, C2 = constants[0], constants[1]
    
    eq1 = general_solution.rhs.subs(t, 0) - y0
    eq2 = sp.diff(general_solution.rhs, t).subs(t, 0) - dy0
    print("Definindo as condições iniciais:")
    sp.pprint(eq1)
    sp.pprint(eq2)
    print()
    
    constants_solution = sp.solve((eq1, eq2), (C1, C2))
    
    if constants_solution:
        C1_val = constants_solution[C1]
        C2_val = constants_solution[C2]
        particular_solution = general_solution.subs(constants_solution)
        print("C1 =", C1_val.evalf())  # Avalia C1 para um valor específico
        print("C2 =", C2_val.evalf())  # Avalia C2 para um valor específico
        print("\nA solução particular da EDO com as condições iniciais dadas é:")
        sp.pprint(particular_solution)
    else:
        print("Erro: Não foi possível encontrar uma solução para as constantes.")

def zeroStateFirstDegreeODE():
    t, s = sp.symbols('t s')
    Y = sp.Function('Y')(s)
    y = sp.Function('y')(t)
    
    # Define a função de excitação
    f = t  # Por exemplo, vamos tomar f(t) = t
    
    # Define a transformada de Laplace da função de excitação
    F = sp.laplace_transform(f, t, s, noconds=True)
    print("Transformada de Laplace da função de excitação F(s):")
    sp.pprint(F)
    print()
    
    # Define a transformada de Laplace da EDO
    ode_laplace = sp.Eq(s * Y - 0 + 3 * Y, F)  # Supondo y(0) = 0 para resposta ao estado zero
    print("Transformada de Laplace da equação diferencial:")
    sp.pprint(ode_laplace)
    print()
    
    # Resolve para Y(s)
    Y_sol = sp.solve(ode_laplace, Y)[0]
    print("Resolvendo para Y(s):")
    sp.pprint(Y_sol)
    print()
    
    # Toma a transformada inversa de Laplace para encontrar y(t)
    y_sol = sp.inverse_laplace_transform(Y_sol, s, t)
    print("Transformada inversa de Laplace para encontrar y(t):")
    sp.pprint(y_sol)
    print("\nA solução do estado zero da EDO é:")
    sp.pprint(y_sol)

def zeroStateSecondDegreeODE():
    t, s = sp.symbols('t s')
    Y = sp.Function('Y')(s)
    y = sp.Function('y')(t)
    
    # Define a função de excitação
    f = t  # Por exemplo, vamos tomar f(t) = t
    
    # Define a transformada de Laplace da função de excitação
    F = sp.laplace_transform(f, t, s, noconds=True)
    print("Transformada de Laplace da função de excitação F(s):")
    sp.pprint(F)
    print()
    
    # Define a transformada de Laplace da EDO
    ode_laplace = sp.Eq(s**2 * Y - s*0 - 0 + 2 * s * Y + Y, F)  # Supondo y(0) = 0 e y'(0) = 0 para resposta ao estado zero
    print("Transformada de Laplace da equação diferencial:")
    sp.pprint(ode_laplace)
    print()
    
    # Resolve para Y(s)
    Y_sol = sp.solve(ode_laplace, Y)[0]
    print("Resolvendo para Y(s):")
    sp.pprint(Y_sol)
    print()
    
    # Toma a transformada inversa de Laplace para encontrar y(t)
    y_sol = sp.inverse_laplace_transform(Y_sol, s, t)
    print("Transformada inversa de Laplace para encontrar y(t):")
    sp.pprint(y_sol)
    print("\nA solução do estado zero da EDO é:")
    sp.pprint(y_sol)

def main():
    while True:
        print('(1) EDO de Primeira Ordem com Entrada Nula')
        print('(2) EDO de Segunda Ordem com Entrada Nula')
        print('(3) EDO de Primeira Ordem com Estado Nulo')
        print('(4) EDO de Segunda Ordem com Estado Nulo')
        usrInput = input()

        os.system('cls')

        if int(usrInput) in [1, 2, 3, 4]:
            break

    if int(usrInput) == 1:
        zeroInputFirstDegreeODE()
    elif int(usrInput) == 2:
        zeroInputSecondDegreeODE()
    elif int(usrInput) == 3:
        zeroStateFirstDegreeODE()
    elif int(usrInput) == 4:
        zeroStateSecondDegreeODE()

if __name__ == "__main__":
    main()
