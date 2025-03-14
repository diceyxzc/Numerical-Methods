# Import all the essential libraries: os | matplotlib | numpy
import os 
import matplotlib.pyplot as plt
import numpy as np

os.environ['TCL_LIBRARY'] = 'C:/Users/fla10/AppData/Local/Programs/Python/Python313/tcl/tcl8.6'
os.environ['TK_LIBRARY'] = 'C:/Users/fla10/AppData/Local/Programs/Python/Python313/tcl/tk8.6'

# This section is responsible for graphing the methods.
# It is made possible with matplotlib.

# Main Function
def f(x):
    return -2 * x**6 - 1.5 * x**4 + 10 * x + 2

# X Function
def g(x):
    return (2 * x ** 6 + 1.5 * x ** 4 - 2) / 10

# Graphical Plot
def plot_graphical():
    x = np.linspace(-3, 3, 1000)
    y = f(x)

    # Plot the graph.
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=r'$f(x) = -2x^6 - 1.5x^4 + 10x + 2$', color='purple')

    # Add grid, labels, and title.
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of $f(x) = -2x^6 - 1.5x^4 + 10x + 2$')

    # Approximate where the function crosses y=0 using NumPy's root finder.
    coefficients = [-2, 0, 0, -1.5, 0, 10, 2]
    roots = np.roots(coefficients)

    # Filter only real roots within the plotted range.
    real_roots = roots[np.isreal(roots)].real

    # Plot the points of intersection.
    for root in real_roots:
        if -3 <= root <= 3: 
            plt.plot(root, 0, 'ro', label='Root (f(x)=0)' if root == real_roots[0] else "")
            plt.axvline(root, color='red', linestyle='--', alpha=0.7, label='Intersection Line' if root == real_roots[0] else "")
            plt.text(root, 1.5, f'({root:.2f}, 0)', fontsize=9)

    # Add a legend
    plt.legend(loc='lower right')
    plt.show()

# Bisection Plot
def plot_function_and_bisection(X_L, X_U, x_m_values):
    x = np.linspace(X_L - 0.5, X_U + 0.5, 400)  
    y = f(x)

    # Plots the method itself.
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label="f(x) = -2x⁶ - 1.5x⁴ + 10x + 2", color='b')
    plt.scatter(x_m_values, f(np.array(x_m_values)), color='r', marker='o', label="Bisection Midpoints")

    # Highlights the roots.
    final_xm = x_m_values[-1]
    plt.axvline(final_xm, color='g', linestyle="--", label=f"Root Approx. x = {final_xm:.4f}")

    # Adds titles, labels, legends, and window title.
    plt.gcf().canvas.manager.set_window_title("Bisection Method | Function Plot")
    plt.title("Function Graph with Bisection Method Points")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.axhline(0, color='black', linewidth=1)
    plt.legend()
    plt.grid()
    plt.show()

# Regula Falsi PLot
def plot_function_and_regula_falsi(xl,xu, xr, xl_values, xu_values, xr_values):
    x = np.linspace(xl - 1, xu + 1, 400)
    y = f(x)

    # Plots the method itself.
    plt.gcf().canvas.manager.set_window_title("Regula Falsi Method | Function Plot")
    plt.plot(x, y, label='Function f(x) = -$2x^6$-$1.5x^4$+10x+2')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)

    plt.scatter(xl_values, [f(val) for val in xl_values], color='red', label='Xl values')
    plt.scatter(xu_values, [f(val) for val in xu_values], color='blue', label='Xu values')
    plt.scatter(xr_values, [f(val) for val in xr_values], color='green', label='Xr values')

    # Highlights the roots.
    for xr_val in xr_values:
        plt.axvline(x=xr, color='green', linestyle=':', linewidth=1)

    # Adds titles, labels, legends, and window title.
    plt.legend()
    plt.title('Regula Falsi Method')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.show()

# Simple Fixed Point Plot
def plot_functin_and_simple_fixed_point(iterations):
    x_vals = np.linspace(-2, 2, 400)
    y_vals = g(x_vals)

    # Plots the method itself.
    plt.plot(x_vals, y_vals, label="g(x) = (2x⁶ + 1.5x⁴ - 2) / 10", color='blue')
    plt.plot(x_vals, x_vals, label="y = x", color='black', linestyle='--')

    for i, xi, xi_plus_1, e_a in iterations:
        plt.plot([xi, xi_plus_1], [xi_plus_1, xi_plus_1], 'r--')  
        plt.plot([xi_plus_1, xi_plus_1], [xi_plus_1, g(xi_plus_1)], 'g--')  
        plt.plot(xi, xi_plus_1, 'ro')  

    # Highlights the roots.
    final_x = iterations[-1][2]
    plt.axvline(final_x, color='green', linestyle=':', label=f"Root Approx. x = {final_x:.4f}")

    # Adds titles, labels, legends, and window title.
    plt.gcf().canvas.manager.set_window_title("Simple Fixed Method | Function Plot")
    plt.xlabel('x')
    plt.ylabel('g(x)')
    plt.title('Fixed-Point Iteration Method')
    plt.legend()
    plt.grid()
    plt.show()

# Newton Rhapson Plot
def plot_function_and_newton_rhapson(iterations):
    x_vals = np.linspace(-2, 2, 400)
    y_vals = f(x_vals)

    # Plots the method itself.
    plt.plot(x_vals, y_vals, label="f(x)")

    # Highlights the roots.
    for i, xi, fxi, fpxi, xi_plus_1, e_a in iterations:
        plt.plot(xi, fxi, 'ro')  
        plt.plot([xi, xi_plus_1], [fxi, 0], 'g--')
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')

    # Adds titles, labels, legends, and window title.
    plt.gcf().canvas.manager.set_window_title("Newton Rhapson Method | Function Plot")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Newton-Raphson Method')
    plt.legend()
    plt.grid()
    plt.show()

# Secant Plot
def plot_function_and_secant(x_vals, f_vals, xi_plus_1):
    x = np.linspace(-2, 2, 1000) 
    y = f(x)  

    # Plots the method itself.
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label="f(x) = -2x^6 - 1.5x^4 + 10x + 2", color="blue")  
    plt.scatter(x_vals, f_vals, color="red", label="Iteration Points")  

    # Highlights the roots.
    plt.scatter(xi_plus_1, f(xi_plus_1), color="green", label="Root", marker="x", s=100)  
    plt.axhline(0, color="black", linestyle="--", linewidth=0.5)  
    
    # Adds titles, labels, legends, and window title.
    plt.gcf().canvas.manager.set_window_title("Secant Method | Function Plot")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Secant Method: Root Finding")
    plt.legend()
    plt.grid()
    plt.show()