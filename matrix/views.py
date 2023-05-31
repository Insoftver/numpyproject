from django.shortcuts import render
from django.http import HttpResponse


def sum_matrix(request):
    import numpy as np
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    c = a + b
    return HttpResponse(c)
