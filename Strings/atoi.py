class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self, string):
        # Code here
        # array = list(string)
        # for i in range(len(array)):
        #     if i == 0 and (array[0] in ['-', '+'] or array[0] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']):
        #         pass
        #     elif array[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        #         return -1
        # return int(string)
        for i in string:
            if i in ['-', '+'] or i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                pass
            elif i not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                return -1
        return int(string)
