
"""
@arr array containing elements of any data type
@returns reverse of array passed
"""
def reverse_array(arr):
    if None == arr:
        return None
    start_index = 0
    end_index = len(arr) - 1
    # using indexes to swap elements of array
    while start_index < end_index:
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp
        start_index += 1
        end_index -= 1
    return arr


if __name__ == '__main__':
    arr = []
    arr_length = int(input("Enter number of elements in array: "))
    for i in range(0, arr_length):
        arr.append(input())
    print("Reversed array is : ", reverse_array(arr))
