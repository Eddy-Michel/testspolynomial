import numpy as np

from itertools import combinations
from plotly import data

from scipy.optimize import linprog
from scipy.sparse import csr_matrix, eye, hstack, vstack


data_A = np.loadtxt("data_group_A.csv", delimiter=";", skiprows=1)

data_B = np.loadtxt("data_group_B.csv", delimiter=";", skiprows=1)

# Lignes dont la troisième colonne vaut 1
data_A_1 = data_A[data_A[:, 2] == 1]

# Lignes dont la troisième colonne vaut 2
data_A_2 = data_A[data_A[:, 2] == 2]

print("tailles globales des deux fichiers A et B")

print(data_A.shape)
print(data_B.shape)

print("dans A, tailles globales group 1 et group 2 ")

print(data_A_1.shape)
print(data_A_2.shape)

n = len(data_A_1) // 2

m = len(data_A_2) // 2

data_A_1_group1 = data_A_1[:n]
data_A_1_group2 = data_A_1[n:2*n]

print("dans A group 1, division en deux parties ")

print(data_A_1_group1.shape)
print(data_A_1_group2.shape)

print(f"\n A group 1 1er groupe \n {data_A_1_group1[:5]}")
print(f"\n A group 1 2em groupe \n {data_A_1_group2[:5]}")

data_A_2_group1 = data_A_2[:m]
data_A_2_group2 = data_A_2[m:2*m]

print("dans A group 2, division en deux parties ")

print(data_A_2_group1.shape)
print(data_A_2_group2.shape)


print(f"\n A group 2 1er groupe \n {data_A_2_group1[:5]}")
print(f"\n A group 2 2eme groupe \n {data_A_2_group2[:5]}")

MAX_POWER = 9
N_TERMS = 5

def detect_polynomial(filename):
    data = filename
    
    x = data[:, 0]  # Première colonne
    y = data[:, 1]  # Deuxième colonne
    
    best = []

    for powers in combinations(range(1, MAX_POWER + 1), N_TERMS):
        # Columns are x**power for each candidate power, then the constant.
        X = csr_matrix(np.column_stack(
            [x**power for power in powers] + [np.ones_like(x)]
        ))
        n, k = X.shape
        I = eye(n, format="csr")

        # Minimize sum(|X @ coefficients - y|), which minimizes MAE.
        A_ub = vstack((
            hstack((X, -I)),
            hstack((-X, -I)),
        ), format="csr")
        result = linprog(
            c=np.r_[np.zeros(k), np.ones(n)],
            A_ub=A_ub,
            b_ub=np.r_[y, -y],
            bounds=[(None, None)] * k + [(0, None)] * n,
            method="highs",
        )

        if result.success:
            mae = result.fun / n
            if not best or mae < best[0]:
                best = (mae, powers, result.x[:k])

    return best



mae, powers, coeffs = detect_polynomial(data_A_1_group1)
terms = " + ".join(
    f"{coef:.5g}*x^{power}"
    for power, coef in zip(powers, coeffs[:-1])
)
print(f"data_A_1_group1 y = {terms} + {coeffs[-1]:.5g}")
print(f"MAE = {mae:.6g}\n")




# print(f"\n CSV 1 \n {data_A}")

# print(f"\n CSV 2 \n {data_B}")
