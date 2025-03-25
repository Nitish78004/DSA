def find_second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements for second largest

    largest = second_largest = float('-inf')

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None


# Example usage
array = [10, 20, 4, 45, 99]
result = find_second_largest(array)
print("Second largest element is:", result)