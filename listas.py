def double(arr):
    for i in range(len(arr)):
        arr[i] *= 2
    return arr

def maximum(arr):
    max_value = arr[0]
    for num in arr:
        if num > max_value:
            max_value = num
    return max_value

def average(arr):
    return sum(arr) / len(arr)

def main():
    arr = [12, 132, 142, 12, 3, 1, 23, 12, 33, 2, 321321]
    print("Original list:", arr)
    
    arr_doble = double(arr.copy())
    print("Doubled list:", arr_doble)
    
    max_value = maximum(arr)
    print("Maximum value:", max_value)
    
    avg_value = average(arr)
    print("Average value:", avg_value)