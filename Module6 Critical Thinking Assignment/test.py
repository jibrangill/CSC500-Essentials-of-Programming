print('\nUsing Built-in sum() Function with a lambda expression')
numbers = [1, 2, 3, 4, 5]
running_total = 0
sum_with_prints = sum(num for num in numbers if not print(running_total := running_total + num))
print("Final sum:", sum_with_prints)

print('\nMelissa\'s Custom Function Implementation:')
def sum_vals(numbers):
    total = 0
    for val in numbers:
        total += val
        print(total)
    return total
result = sum_vals(numbers)
print("Final sum:", result)
