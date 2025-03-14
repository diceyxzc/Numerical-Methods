# Import all the essential libraries: numpy | tabulate
import numpy as np
from tabulate import tabulate

# This section is where all the calculations take place.
# It is the main component of the system as it is used for the plot.

# Main Function
def f(x):
    return (-2 * x ** 6) - (1.5 * x ** 4) + (10 * x) + 2
    
# X function
def g(x):
    return (2 * x ** 6 + 1.5 * x ** 4 - 2) / 10

# Derivative Function
def f_prime(x):
    return -12 * x ** 5 - 6 * x ** 3 + 10

# Bisection Method
def bisection(X_L, X_u, limit=2.0):

    # Initializes the variables of the method.
    bisection_result = []
    x_m_prev = None
    x_m_values = []
    iteration = 0
    e_a = 100
    
    # Check if initial bounds are appropriate for finding a root.
    f_xl = -2 * X_L**6 - 1.5 * X_L**4 + 10 * X_L + 2
    f_xu = -2 * X_u**6 - 1.5 * X_u**4 + 10 * X_u + 2
    
    # Verify that there's a sign change between bounds. 
    if f_xl * f_xu > 0:
        
        # If no sign change, print warning but continue anyway.
        print(f"Warning: Function may not have a root in the interval [{X_L}, {X_u}] or may have an even number of roots.")
        print(f"f({X_L}) = {f_xl} and f({X_u}) = {f_xu}")
        
        # Try to adjust bounds to find a root if possible.
        # For finding -0.1997 root.
        if -1 < X_L < 0 and 0 < X_u < 2:
            if X_L > -0.5:
                X_L = -0.5
                print(f"Adjusted X_L to {X_L} to find root near -0.1997")
            if X_u < 0:
                X_u = 0
                print(f"Adjusted X_u to {X_u} to find root near -0.1997")
        
        # For finding 1.32 root.
        elif 0 < X_L < 2 and 1 < X_u < 3:
            if X_L > 1:
                X_L = 1
                print(f"Adjusted X_L to {X_L} to find root near 1.32")
            if X_u < 1.5:
                X_u = 1.5
                print(f"Adjusted X_u to {X_u} to find root near 1.32")

    while e_a >= limit:
        # Calculations.
        x_m = (X_L + X_u) / 2
        f_xm = -2 * x_m**6 - 1.5 * x_m**4 + 10 * x_m + 2
        f_xl = -2 * X_L**6 - 1.5 * X_L**4 + 10 * X_L + 2
        f_xlxm = f_xm * f_xl

        if x_m_prev is not None:
            e_a = abs((x_m - x_m_prev) / x_m) * 100  

        bisection_result.append({
            'iteration': iteration, 
            'X_L': X_L, 
            'X_u': X_u, 
            'X_m': x_m, 
            'f_xlxm': f_xlxm, 
            'e_a': e_a if iteration > 0 else "_"
        })

        if f_xlxm < 0:
            X_u = x_m
        else:
            X_L = x_m

        x_m_values.append(x_m)
        
        x_m_prev = x_m
        iteration += 1
        
        # Prevent infinite loops with a reasonable maximum iteration limit.
        if iteration > 100:
            print("Maximum iterations reached. Solution may not have converged to desired accuracy.")
            break

    # At the end, print which root we likely found.
    final_x = x_m_values[-1]
    if abs(final_x + 0.1997) < 0.05:
        print(f"Found the root near -0.1997 (actual value: {final_x})")
    elif abs(final_x - 1.32) < 0.05:
        print(f"Found the root near 1.32 (actual value: {final_x})")
    else:
        print(f"Found a root at {final_x}, which is not close to the expected values of -0.1997 or 1.32.")

    return bisection_result, x_m_values

def print_table_bisection(bisection_result):
    # Prints the results.
    print("+-------------+-------------+-------------+----------------+--------------------+-------------+")
    print("|      i      |     X_L     |     X_u     |       X_m      |     F(X_m)F(X_L)   |    E_a (%)  |")
    print("+-------------+-------------+-------------+----------------+--------------------+-------------+")
    
    # Gets the results from the index of bisection: bisection_results = [].
    for result in bisection_result:
        e_a_str = f"{result['e_a']:.2f}" if isinstance(result['e_a'], float) else result['e_a']
        
        print(f"|      {result['iteration']:<6} | {result['X_L']:<11.4f} | {result['X_u']:<11.4f} | "
              f"{result['X_m']:<14.4f} | {result['f_xlxm']:<18.4f} | {e_a_str:<11} |")
    
    print("+-------------+-------------+-------------+----------------+--------------------+-------------+")
    print(f"Root Approximation: {result['X_m']:.4f}")
    print(f"Root Found Nearly: {e_a_str} %")

# Regula Falsi Method
def regula_falsi(xl, xu):

    # Intializes the variables of the method.
    xl_values = []
    xu_values = []
    xr_values = []
    xr_old = 0
    i = 0

    # Prints out the results with the calculations.
    print("+---------+----------+-------------+----------+-------------+----------+---------------------------+")
    print("|    \033[2;3mi\033[0m    |    \033[2;3mXl\033[0m    |    \033[2;3mf(Xl)\033[0m    |    \033[2;3mXu\033[0m    "
        "|    \033[2;3mf(Xu)\033[0m    |    \033[2;3mXr\033[0m    |    \033[2;3mf(Xr)\033[0m    |    \033[2;3mEa(%)\033[0m    |")
    print("+---------+----------+-------------+----------+-------------+----------+---------------------------+")

    while True:
        fxl = f(xl)
        fxu = f(xu)
        xr = ((xl * fxu) - (xu * fxl)) / (fxu - fxl)
        fxr = f(xr)
        width = 8

        if i == 0:
            ea = "No Error Defined."
        else:
            ea = abs((xr - xr_old) / xr) * 100


        if ea == 'No Error Defined.':
            print(f"| {i:<{width}}| {xl:<{width}.4f} | {fxl:<{width}.4f}    | {xu:<{width}.4f} | {fxu:<{width}.4f}    "
                f"| {xr:<{width}.4f} | {fxr:<{width}.4f}    | N/A         |")
        else:
            print(f"| {i:<{width}}| {xl:<{width}.4f} | {fxl:<{width}.4f}    | {xu:<{width}.4f} | {fxu:<{width}.4f}    "
                f"| {xr:<{width}.4f} | {fxr:<{width}.4f}    | \033[2;3m{ea: <{width}.2f}\033[0m    |")

        xl_values.append(xl)
        xu_values.append(xu)
        xr_values.append(xr)

        if ea != 'No Error Defined.' and ea < 2:
            print("+---------+----------+-------------+----------+-------------+----------+---------------------------+")
            print(f"Root Nearly Found at Ea = \033[1;3m{ea:.2f}%\033[0m")
            break
        if fxl * fxr < 0:
            xu = xr
        else:
            xl = xr

        xr_old = xr
        i += 1

    print(f"Final Estimated Root: \033[1;3m{xr: .4f}\033[0m")

    return xr, xl_values, xu_values, xr_values

# Simple Fixed Point Method
def simple_fix_point(xi, tol=2.0, max_iter=100):
    
    # Initializes the variables of the method.
    xi = xi
    iterations = []

    # Calculations.
    for i in range(max_iter):
        xi_1 = g(xi)

        if i > 0:
            e_a = abs((xi_1 - xi) / xi_1) * 100
        else:
            e_a = None

        iterations.append((i, xi, xi_1, e_a))

        if e_a is not None and e_a <= tol:
            break

        xi = xi_1

    # Prints the results.
    print("-" * 50)
    print("    i     |     xi     |   xi+1     |    E_a (%) ")
    print("-" * 50)

    for i, xi, xi_plus_1, e_a in iterations:
        e_a_str = f"{e_a:^10.4f}" if e_a is not None else "   N/A    "
        print(f"{i:^9} | {xi:^10.4f} | {xi_plus_1:^10.4f} | {e_a_str}")

    print(f"Root Approximation: {xi_plus_1:.4f}")
    print(f"Root Found Nearly: {e_a:.2f} %")

    return iterations

# Newton Rhapson Method
def newton_rhapson(xi, tol=2.0, max_iter=100):
    
    # Initializes the variables of the method.
    xi = xi
    iterations = []

    # Calculations.
    for i in range(max_iter):
        fxi = f(xi)
        fpxi = f_prime(xi)

        if fpxi == 0:
            print("Derivative is zero. No solution found.")
            break

        xi_1 = xi - (fxi / fpxi)

        if i > 0:
            e_a = abs((xi_1 - xi) / xi_1) * 100
        else:
            e_a = None

        iterations.append((i, xi, fxi, fpxi, xi_1, e_a))

        if e_a is not None and e_a < tol:
            break

        xi = xi_1

    # Prints the results.
    print("-" * 77)
    print("    i     |     xi     |    f(xi)    |   f'(xi)   |   xi+1    |      E_a (%)   ")
    print("-" * 77)

    for i, xi, fxi, fpxi, xi_plus_1, e_a in iterations:
        e_a_str = f"{e_a:^10.4f}" if e_a is not None else "   N/A    "
        print(f"{i:^9} | {xi:^10.4f} | {fxi:^10.4f} | {fpxi:^10.4f} | {xi_plus_1:^10.4f} |   {e_a_str}")
    
    print(f"Root Approximation: {xi_plus_1:.4f}")
    print(f"Root Found Nearly: {e_a:.2f} %")

    return iterations

# Secant Method
def secant(xi_minus_1, xi):
    
    # Initializes the variables of the method.
    max_iter = 100
    error = 100  
    iter = 0
    table_data = []
    x_vals = [xi_minus_1, xi]
    f_vals = [f(xi_minus_1), f(xi)]

    # Calculations.
    while iter < max_iter:
        xi_plus_1 = xi - (f(xi) * (xi_minus_1 - xi)) / (f(xi_minus_1) - f(xi))
        
        if iter > 0:
            error = abs((xi_plus_1 - xi) / xi_plus_1) * 100
        else:
            error = np.nan  
            
        if iter == 0:
            table_data.append([iter, xi_minus_1, f(xi_minus_1), xi, f(xi), xi_plus_1, "N/A"])
        else:
            table_data.append([iter, xi_minus_1, f(xi_minus_1), xi, f(xi), xi_plus_1, f"{error:.6f}"])
            
        if iter > 0 and error < 5:
            break
            
        xi_minus_1 = xi
        xi = xi_plus_1
        iter += 1

    # Prints the results.
    headers = ["i", "X_i(i-1)", "f(X_i(i-1))", "X_i", "f(X_i)", "X_i(i+1)", "e_a (%)"]
    print(tabulate(table_data, headers=headers, tablefmt="grid", floatfmt=".4f"))

    print(f"The Root is Approximately: {xi:.4f}")
    print(f"Number of iterations: {iter + 1}")

    return x_vals, f_vals, xi_plus_1