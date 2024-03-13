import random
import csv


def new_numbers(a, b):
    return 1 / (a + b)


def merge_sort(list):
    # sorts the list using merge sort
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            list[k] = right[j]
            j += 1
            k += 1


def add_numbers(a, b, limit):
    numbers = [a, b]
    i = 0
    j = 0
    while len(numbers) < limit:
        i = random.randint(0, len(numbers) - 1)
        j = random.randint(0, len(numbers) - 1)
        numbers += [new_numbers(numbers[i], numbers[j])]
    merge_sort(numbers)
    i = 1
    while i != len(numbers):
        if numbers[i] == numbers[i - 1]:
            numbers.pop(i)
        i += 1
    return numbers
    

def main():
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    limit = int(input("Enter limit: "))

    numbers = add_numbers(a, b, limit)
    with open("numbers.csv", "w", newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["iteration", "numbers"])
        for i in range(0, len(numbers)):
            csvwriter.writerow((i, numbers[i]))


if __name__ == '__main__':
    main()