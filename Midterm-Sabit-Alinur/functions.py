#Alinur Sabit 16BD02113
def prod_non_zero_diag(x):
    """Compute product of nonzero elements from matrix diagonal.

    input:
    x -- 2-d numpy array
    output:
    product -- integer number


    Not vectorized implementation.
    """
    result = 1
    for i in range(len(x)): #делает итерацию по массиву для доступа к индексам массива
        for j in range(len(x[i])):
            if(i == j and x[i][j] != 0):
                result *= x[i][j]
    return result
    pass


def are_multisets_equal(x, y):
    """Return True if both vectors create equal multisets.

    input:
    x, y -- 1-d numpy arrays
    output:
    True if multisets are equal, False otherwise -- boolean

    Not vectorized implementation.
    """
    x.sort()
    y.sort()
    return (x == y).all() == True
    pass


def max_after_zero(x):
    """Find max element after zero in array.

    input:
    x -- 1-d numpy array
    output:
    maximum element after zero -- integer number

    Not vectorized implementation.
    """
    az = [] #массив элементов после нуля
    for i in range(len(x)-1):
        if(x[i] == 0):
            az.append(x[i+1]) #добавить в конец массива элемент после нуля
    return max(az) #макс элемент в массиве
    pass


def convert_image(img, coefs):
    """Sum up image channels with weights from coefs array

    input:
    img -- 3-d numpy array (H x W x 3)
    coefs -- 1-d numpy array (length 3)
    output:
    img -- 2-d numpy array

    Not vectorized implementation.
    """
    for x, x_el in range(len(img)):
        for y, y_el in range(len(img[x_el])):
            img[x, y] = (y_el[0] * coefs[0] + 
                         y_el[1] * coefs[1] + 
                         y_el[2] * coefs[2])
    return img
        
    pass


def run_length_encoding(x):
    """Make run-length encoding.

    input:
    x -- 1-d numpy array
    output:
    elements, counters -- integer iterables

    Not vectorized implementation.
    """
    dic = {}
    for i in x:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return list(dic.keys()), list(dic.values())
    pass


def pairwise_distance(x, y):
    """Return pairwise object distance.

    input:
    x, y -- 2d numpy arrays
    output:
    distance array -- 2d numpy array

    Not vectorized implementation.
    """
    euclid = []
    for i in range(len(x)):
        temp = []
        for j in range(len(y)):
            temp.append(((x[i] - y[j])**2)**(1/2))
        euclid.append(temp)
    return euclid
    pass