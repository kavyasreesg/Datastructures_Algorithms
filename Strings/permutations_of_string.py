def permute(str_arr, low, high):
    if low == high:
        print(''.join(str_arr))
    else:
        for i in range(low, len(str_arr)):
            str_arr[i], str_arr[low] = str_arr[low], str_arr[i]
            permute(str_arr, low + 1, high)
            str_arr[low], str_arr[i] = str_arr[i], str_arr[low]


class Solution:
    def __init__(self):
        self.res = []

    def find_permutation(self, S):
        # Code here
        array = list(S)
        self.permute(array, [])
        return sorted(self.res)

    def permute(self, nums, path):
        if not nums:
            self.res.append(''.join(path))
        else:
            for i in range(len(nums)):
                self.permute(nums[:i] + nums[i + 1:], path + [nums[i]])


if __name__ == '__main__':
    string = "ABCD"  # 4! combinations
    permute(list(string), 0, 3)
