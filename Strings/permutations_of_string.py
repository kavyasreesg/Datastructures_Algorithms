def permute(str_arr, low, high):
    if low == high:
        print(''.join(str_arr))
    else:
        for i in range(low, len(str_arr)):
            str_arr[i], str_arr[low] = str_arr[low], str_arr[i]
            permute(str_arr, low + 1, high)
            str_arr[low], str_arr[i] = str_arr[i], str_arr[low]


if __name__ == '__main__':
    string = "ABCD"  # 4! combinations
    permute(list(string), 0, 3)
