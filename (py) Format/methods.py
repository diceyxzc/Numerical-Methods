# Import all the essential libraries: os | main | plot
import os
import main as run
import plot as plt
import plot as graph

# This section is used to get all the initial guesses from the user.
# It is also used for calling out the methods itself. All the methods are located at main.ipynb.

# Graphical Method
# Made by: Calvin Berlandino

def graphical_call():
    
    # Plots the function itself with its determined roots.
    plt.plot_graphical()

# Bisection Method
# Made by: Calvin Berlandino

def bisection_call():    
    os.system('cls')         
    print("+------------------+")
    print("| Bisection Method |")
    print("+------------------+")

    # Initial gueseses.
    X_L = float(input("| Enter X_L (Lower Bound): "))
    X_u = float(input("| Enter X_U (Upper Bound): "))

    # Runs the bisection method.
    result, x_m_values = run.bisection(X_L, X_u)

    # Displays the results.
    run.print_table_bisection(result)
    graph.plot_function_and_bisection(X_L, X_u, x_m_values)

# Regula Falsi Method
# Made by: Jireh Dela Cruz

def regula_falsi_call():
    os.system('cls')
    print("+---------------------+")
    print("| Regula Falsi Method |")
    print("+---------------------+")

    # Initial guesses.
    xl = float(input("Enter Lower Limit\nXl: "))
    xu = float(input("Enter Upper Limit\nXu: "))

    # Runs the regula falsi method.
    xr, xr_values, xu_values, xl_values = run.regula_falsi(xl, xu)
    
    # Displays the results.
    graph.plot_function_and_regula_falsi(xl,xu,xr,xr_values,xu_values,xl_values)

# Simple Fixed Point Method
# Made by: Rylle Acotin

def simple_fixed_point_call():
    os.system('cls')
    print("+---------------------------+")
    print("| Simple Fixed Point Method |")
    print("+---------------------------+")

    # Initial guess.
    xi = float(input("Enter xi (Initial Value): "))

    # Runs the simple fixed method.
    iterations = run.simple_fix_point(xi)

    # Displays the results.
    graph.plot_functin_and_simple_fixed_point(iterations)

# Newton Rhapson Method
# Made by: Rylle Acotin

def newton_rhapson_call():
    os.system('cls')
    print("+-----------------------+")
    print("| Newton Rhapson Method |")
    print("+-----------------------+")

    # Initial guess.
    xi = float(input("Enter xi (Initial Value): "))

    # Runs the newton rhapson method. 
    iterations = run.newton_rhapson(xi)

    # Displays the results.
    graph.plot_function_and_newton_rhapson(iterations)

# Secant Method
# Made by: Von Acosta

def secant_call():
    os.system('cls')
    print("+-----------------------+")
    print("| Newton Rhapson Method |")
    print("+-----------------------+")

    # Initial Guesses.
    xi_minus_1 = float(input("Enter the First Initial Guess (x_i-1): "))
    xi = float(input("Enter the Second Initial Gues (x_i): "))

    # Runs the secant method.
    x_vals, f_vals, xi_plus_1 = run.secant(xi_minus_1, xi)

    # Displays the result.
    graph.plot_function_and_secant(x_vals, f_vals, xi_plus_1)