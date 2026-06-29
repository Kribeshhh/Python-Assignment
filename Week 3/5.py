def sum_of_list(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = input("Enter numbers separated by spaces: ")
list1 = list(map(int, numbers.split()))

print("Sum:", sum_of_list(list1))