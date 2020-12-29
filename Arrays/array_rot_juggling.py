def leftRotate(array_in, num_digits, n):
    num_digits = num_digits % n
    gcd_in = gcd(num_digits, n)
    for i in range(gcd_in):

        temp = array_in[i]
        j = i
        while 1:
            k = j + num_digits
            if k >= n:
                k = k - n
            if k == i:
                break
            array_in[j] = array_in[k]
            j = k
        array_in[j] = temp

    print(array_in)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d = 2
leftRotate(arr, d, n)
