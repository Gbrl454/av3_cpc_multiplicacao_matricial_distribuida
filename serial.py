from datetime import datetime
from save_json_util import save_json
from matrix import get_matrix, matrix_multiply

if __name__ == "__main__":
    n = 15
    
    na1 = n
    na2 = n
    nb1 = n
    nb2 = n
    initial_time = datetime.now()
    
    matrix_1 = get_matrix(na1, na2)
    matrix_2 = get_matrix(nb1, nb2)
    print("matrix_1:", matrix_1)
    print("matrix_2:" ,matrix_2)
    
    matrix_result = matrix_multiply(matrix_1, matrix_2)
    print("matrix_result:", matrix_result)
    
    final_time = datetime.now()
    duration_time = final_time - initial_time

    info = {
        "initial_time": initial_time,
        "final_time": final_time,
        "duration_time": duration_time,
    }
    save_json(info, f'results/serial/matrix_{n}.json')