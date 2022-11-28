def mean(numbers):
    average = sum(numbers) / len(numbers)
    print(f"The mean is equal to {average}")

numbers = input('Enter a list of integers seperated by spaces: ')
numbers = [int(num) for num in numbers.split()]

mean(numbers)