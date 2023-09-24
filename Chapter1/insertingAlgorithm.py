import time

def insertion_sort_visualize(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        # Print the current state of the list.
        print("Step", i, ":", arr)

        # Pause for a moment to visualize the sorting process.
        time.sleep(1.5)  # Adjust the delay as needed.

if __name__ == "__main__":
    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))  # Convert input to a list of integers
    print("Unsorted list:", numbers)
    
    insertion_sort_visualize(numbers)
    
    print("Sorted list:", numbers)
