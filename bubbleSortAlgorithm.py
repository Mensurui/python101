def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        print("This is i "+str(i))
        
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n-i-1):
            print("This is j "+str(j))
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example usage:
if __name__ == "__main__":
    # Your list of numbers to be sorted
    numbers = input()
    
    print("Unsorted list:", numbers)
    
    # Perform bubble sort
    bubble_sort(numbers)
    
    print("Sorted list:", numbers)


def bubble_sort_descending_length(arr):
    n = len(arr)
    
    # Traverse through all elements in the list
    for i in range(n):
        
        # Last i elements are already in place
        for j in range(0, n-i-1):
            
            # Compare the lengths of adjacent strings and swap if needed
            if len(arr[j]) < len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    # Prompt the user to enter a list of strings separated by spaces
    user_input = input("Enter a list of strings separated by spaces: ")
    
    # Split the user input into a list of strings
    strings = user_input.split()
    
    # Perform bubble sort in descending order of string lengths
    bubble_sort_descending_length(strings)
    
    # Display the sorted list
    print("Sorted list (descending by length):", strings)


def bubble_sort_descending_numbers(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    user_input = input("Enter a list of numbers separated by spaces: ")
    
    numbers_str = user_input.split()
    
    numbers = [int(x) for x in numbers_str]
    
    bubble_sort_descending_numbers(numbers)
    
    print("Sorted list (descending order):", numbers)



