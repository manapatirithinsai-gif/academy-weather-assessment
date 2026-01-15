def sort_numbers(numbers):
    """
    Sort the list of numbers in ascending order by
    using Bubble Sort algorithm.
    """
    n = len(numbers)

    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                # Swap elements
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    return numbers


def sortAndFindMedian(numbers):
    """
    Sorts the array and it returns the median value.
    """
    # Sort the numbers
    sorted_numbers = sort_numbers(numbers)

    n = len(sorted_numbers)

    # Check if number of elements is even or odd
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_numbers[n // 2]

    return median


def main():
    print("Median Finder Application")

    # User input
    user_input = input("Enter numbers separated by space: ")

    # Convert input to list of integers
    numbers = list(map(int, user_input.split()))

    median = sortAndFindMedian(numbers)

    print("Sorted numbers:", sort_numbers(numbers))
    print("Median:", median)


# Program starts here
main()
