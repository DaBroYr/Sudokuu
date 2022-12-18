import itertools as it
import pycosat

clauses = []

n = int(input())

def varnum(i, j, k):
    assert i in range(n * n) and j in range(n * n) and k in range(n * n + 1)
    return i * n * n * n * n  + j * n * n + k

for i in range(n * n):
    string = str(input())
    row = string.split()
    for j in range(n * n):
        k = int(row[j])
        if k!= 0:
            clauses.append([varnum(i, j, k)])

for (i, j) in it.product(range(n * n), range(n * n)):
    clauses.append([varnum(i, j, k) for k in range(1,n * n + 1)])

for k in range(1,n * n + 1):
    for i in range(n * n):
        for (j1, j2) in it.combinations(range(n * n), 2):
            clauses.append([-varnum(i, j1, k), -varnum(i, j2, k)])

for k in range(1,n * n + 1):
    for j in range(n * n):
        for (i1, i2) in it.combinations(range(n * n), 2):
            clauses.append([-varnum(i1, j, k), -varnum(i2, j, k)])

for k in range(1, n * n + 1):
    for i in range(0, n * n, n):
        for j in range(0, n * n, n):
            m = []
            s = []

            for l in range(n):
                s.append(l)

            for u, v in it.product(s, repeat=2):
                m.append(varnum(i + u, j + v, k))
            clauses.append(m)

assignment = pycosat.solve(clauses)

for i in range(n * n):
    print("|", end="")
    for j in range(n * n):
        for k in range(1, n * n + 1):
            if assignment[varnum(i, j, k)-1] > 0:
                print(k, "|", end="")

    print("")
