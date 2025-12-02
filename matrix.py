import random

def get_random_number():
    return round(random.uniform(-100, 100), 2)


def get_matrix(n_rows, n_cols):
    return [[get_random_number() for _ in range(n_cols)] for _ in range(n_rows)]


def matrix_multiply(A, B):
    get_row_column_length = lambda m: [get_row_length(m), get_column_length(m)]

    A_row_size, A_column_size = get_row_column_length(A)
    B_row_size, B_column_size = get_row_column_length(B)

    if A_column_size != B_row_size:
        raise ValueError(
            "Número de colunas de A deve ser igual ao número de linhas de B"
        )

    result = [[0 for _ in range(B_column_size)] for _ in range(A_row_size)]

    for i in range(A_row_size):
        for j in range(B_column_size):
            soma = 0
            for k in range(A_column_size):
                soma += A[i][k] * B[k][j]
            result[i][j] = soma
    return result


def get_row_length(m):
    return len(m)


def get_column_length(m):
    return len(m[0])


def get_row(m, r_idx):
    return [m[r_idx]]


def get_column(m, c_idx):
    return [[i[c_idx]] for i in m]
