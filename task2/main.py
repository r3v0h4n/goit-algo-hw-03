import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Check for valid input data
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity > (max_num - min_num + 1):
        return []

    # Generate a unique set of numbers
    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort()

    return numbers

# Example usage
print(get_numbers_ticket(1, 49, 6))