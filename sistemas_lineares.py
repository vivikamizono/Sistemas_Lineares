def gaussian_elimination(A, b):
    n = len(A)
    
    # Fase de eliminação
    for i in range(n):
        # Encontrando o pivô
        max_index = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_index][i]):
                max_index = j
        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]

        # Eliminando
        for j in range(i + 1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    
    # Fase de substituição
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] / A[i][i] * x[j]
    
    return x

def read_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

# Pedindo ao usuário as dimensões do sistema linear
n = read_int_input("Digite o tamanho do sistema linear (por exemplo, 10 para um sistema 10x10): ")

# Criando a matriz de coeficientes e o vetor de termos constantes com valores fornecidos pelo usuário
A = [[0] * n for _ in range(n)]
b = [0] * n

# Preenchendo a matriz de coeficientes e o vetor de termos constantes com valores fornecidos pelo usuário
print("Digite os coeficientes da matriz de coeficientes:")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input(f"Digite o valor do elemento A[{i}][{j}]: "))

print("\nDigite os termos constantes:")
for i in range(n):
    b[i] = float(input(f"Digite o valor do termo constante b[{i}]: "))

# Imprimindo o sistema original
print("\nSistema original:")
for i in range(n):
    equation = " + ".join([f"{A[i][j]}x{j}" for j in range(n)])
    print(f"{equation} = {b[i]}")

# Resolvendo o sistema linear
x = gaussian_elimination(A, b)

# Imprimindo o sistema escalonado
print("\nSistema escalonado:")
for i in range(n):
    equation = " + ".join([f"{A[i][j]}x{j}" for j in range(n)])
    print(f"{equation} = {b[i]}")

# Imprimindo a solução do sistema linear
print("\nSolução do sistema linear:")
for i in range(n):
    print(f"x[{i}] = {x[i]}")
