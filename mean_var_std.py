import numpy as np

def calculate(list):
    try:
        array = np.array(list)
        matrix = array.reshape(3, 3)
        calculations = {
            'mean': [np.mean(matrix, axis=0), np.mean(matrix, axis=1), np.mean(array)],
            'variance': [np.var(matrix, axis=0), np.var(matrix, axis=1), np.var(array)],
            'standard deviation': [np.std(matrix, axis=0), np.std(matrix, axis=1), np.std(array)],
            'max': [np.max(matrix, axis=0), np.max(matrix, axis=1), np.max(array)],
            'min': [np.min(matrix, axis=0), np.min(matrix, axis=1), np.min(array)],
            'sum': [np.sum(matrix, axis=0), np.sum(matrix, axis=1), np.sum(array)]}
    except ValueError:
        calculations = "List must contain nine numbers."

    # print("array", array)
    # print("matrix", matrix)
    # print("calculations", calculations)
    # print("--")

    return calculations