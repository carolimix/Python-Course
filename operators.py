check_number = int(input('Please enter a number'))
is_number_even= (check_number % 2 == 0)
is_number_odd= (check_number % 2 != 0)
is_number_within_range = (check_number >= 10 and check_number >= 1000)
print('¿Is the number even?')
print(is_number_even)
print('¿Is the number odd?')
print(is_number_odd)
print('Is the number within the range between 10 and 1000?')
print(is_number_within_range)