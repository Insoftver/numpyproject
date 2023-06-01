from django.shortcuts import render
from django.http import HttpResponse


def sum_matrix(request):
    import numpy as np
    matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    matrix2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    addition = matrix1 + matrix2
    subtract = matrix1 - matrix2
    multiply = matrix1 * matrix2
    divide = matrix1 / matrix2

    shape = matrix1.shape
    length = len(matrix1)
    number_of_elements = matrix1.size
    dimensions = matrix1.ndim

    exponentiation = np.exp(matrix1)
    square_root = np.sqrt(matrix1)
    sin = np.sin(matrix1)
    cos = np.cos(matrix1)
    log = np.log(matrix1)

    wise_sum = matrix1.sum()
    wise_minimum_value = matrix1.min()
    maximum_value_of_a_row = matrix1.max(axis=0)
    cumulative_sum_of_a_row = matrix1.cumsum(axis=1)
    mean = matrix1.mean(axis=0)
    median = np.median(matrix1)
    correlation_coeficient = np.corrcoef(matrix1)
    standard_deviation = matrix1.std()

    return render(request, 'matrix/start.html', {
        'matrix1': matrix1,
        'matrix2': matrix2,
        'matrix_shape': shape,
        'matrix_length': length,
        'matrix_number_of_elements': number_of_elements,
        'matrix_dimensions': dimensions,
        'matrix_addition': addition,
        'matrix_subtract': subtract,
        'matrix_multiply': multiply,
        'matrix_divide': divide,
        'matrix_exponentiation': exponentiation,
        'matrix_square_root': square_root,
        'matrix_sin': sin,
        'matrix_cos': cos,
        'matrix_log': log,
        'matrix_wise_sum': wise_sum,
        'matrix_wise_minimum_value': wise_minimum_value,
        'matrix_maximum_value_of_a_row': maximum_value_of_a_row,
        'matrix_cumulative_sum_of_a_row': cumulative_sum_of_a_row,
        'matrix_mean': mean,
        'matrix_median': median,
        'matrix_correlation_coeficient': correlation_coeficient,
        'matrix_standard_deviation': standard_deviation,
    })
