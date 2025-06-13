import random

def get_numbers_ticket(min, max, quantity):
    list_of_numbers = []
    if min < 1 or max > 1000 or quantity > (max - min + 1):
        return list_of_numbers
    else:
        list_of_numbers = random.sample(range(min, max + 1), quantity)
        return list_of_numbers

