#Implementation of Counting Sort in Python 
def counting_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
    max_value = max(arr)
    count = [0] * (max_value + 1)
    output = [0] * n
    for i in range(n):
        count[arr[i]] += 1
    for i in range(1, max_value + 1):
        count[i] += count[i-1]
    for i in range(n-1, -1, -1):
        output[count[arr[i]]- 1] = arr[i]
        count[arr[i]] -= 1
    return output
num = [1,3,4,2,5,4,7,6,9,8]
print(counting_sort(num))
