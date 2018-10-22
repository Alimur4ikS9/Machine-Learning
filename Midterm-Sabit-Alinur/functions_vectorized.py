#Alinur Sabit 16BD02113
import numpy as np


def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Vectorized implementation.
    """
    diagonal = np.diag(x)
    diagonal = diagonal[diagonal != 0]
    return np.prod(diagonal) #произведение ненулевых диогональных элементов 
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Vectorized implementation.
    """
    x = np.sort(x)
    y = np.sort(y)
    return np.array_equal(x, y) #сравнение отсортированных массивов
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Vectorized implementation.
    """
    indices = np.where(x == 0) 
    indices = np.add(indices, np.array([1]))
    indices = indices[indices != len(x)] #удаляет индекс больше длины (Например, последний элемент 0, поэтому indices + 1 не сможем сделать)
    return np.amax(np.take(x, indices)) #макс элемент в массиве между индексами(полученными выше)
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Vectorized implementation.
    """
    return np.dot(img[..., :3], coefs)
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Vectorized implementation.
    """
    return np.unique(x, return_counts = True) #Находим каждый разный элемент, и считаем их количество повторения  
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Vctorized implementation.
    """
    import scipy.spatial.distance as dist
    return dist.cdist(x, y, 'euclidean') #формула высчитывания Эвклидового расстояния 
    pass
