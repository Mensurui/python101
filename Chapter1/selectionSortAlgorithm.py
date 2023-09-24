import time

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            print(arr[i], arr[min_index])
            time.sleep(1.0)

if __name__ == "__main__":
    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))  # Convert input to a list of integers
    print("Unsorted list:", numbers)
    
    selection_sort(numbers)
    
    print("Sorted list:", numbers)
