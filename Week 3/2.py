def find_maximum(list1):
    maximum = list1[0]

    for num in list1:
        if num > maximum:
            maximum = num

    return maximum


numbers = input("Enter numbers separated by spaces: ")
list1 = list(map(int, numbers.split()))

print("Maximum number:", find_maximum(list1))