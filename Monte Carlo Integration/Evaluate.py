#! /usr/bin/env python

# Necessary Libraries
import sys
import numpy as np
import matplotlib.pyplot as plt

# import our Generator class file
sys.path.append(".")
from IntegralClass import Integration


if __name__ == "__main__":
    
    N= 20
    lower = 0
    upper = np.pi
    precision = 4
    func = lambda x: np.round(np.sin(x),precision)
    # Analytic result
    I_exact = 2

    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-func] 'func' [-ana] analytical_result [-lower] lower_limit [-upper] upper_limit [-N] Sub_Intervarls\n [-prec] significant_figure" % sys.argv[0])
        sys.exit(1)

    # read the user-provided seed from the command line (if there)
    if '-lower' in sys.argv:
        p = sys.argv.index('-lower')
        lower = float(sys.argv[p+1])
    if '-upper' in sys.argv:
        p = sys.argv.index('-upper')
        upper = float(sys.argv[p+1])

    if '-N' in sys.argv:
        p = sys.argv.index('-N')
        N = int(sys.argv[p+1])
    
    if '-prec' in sys.argv:
        p = sys.argv.index('-prec')
        precision = int(sys.argv[p+1])

    if '-ana' in sys.argv:
        p = sys.argv.index('-ana')
        I_exact = float(sys.argv[p+1])

    if '-func' in sys.argv:
        p = sys.argv.index('-func')
        func = eval('lambda x: ' + sys.argv[p+1])
    
    
    fx = Integration(func,lower,upper)

    ns = np.arange(2, N+1)
    I_midpoint = np.array([fx.midpoint_rule(n) for n in ns])
    I_gauss = np.array([fx.gauss_quad() for _ in ns])

    # Compute errors
    error_midpoint = np.abs(I_midpoint - I_exact)
    error_gauss = np.abs(I_gauss - I_exact)

    # Plot errors

    plt.plot(ns, error_midpoint, label='Midpoint rule')
    plt.plot(ns, error_gauss, label='Gauss-Legendre quadrature')
    plt.xlabel('Number of sub-intervals')
    plt.ylabel('Absolute error')
    plt.title("Integral Evaluation:"+ r'$\int_0^{{\pi}} \sin(x)\,dx = 2$')
    plt.legend()
    plt.show()


