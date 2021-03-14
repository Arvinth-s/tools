#OM NAMO NARAYANA
import numpy as np
import subprocess
import sys


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from tabulate import tabulate
except:
    install("tabulate")
    from tabulate import tabulate

A  = np.array([
    [1, 2, 3],
    [-1, 0, -2],
    [2, 1, 2]
])


print(tabulate(np.matmul(A, A.T), tablefmt="fancy_grid"))