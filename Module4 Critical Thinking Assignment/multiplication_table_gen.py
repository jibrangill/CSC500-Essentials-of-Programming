limit = 5

for number in range(1, limit + 1):  # Iterate over numbers from 1 to 5
    print(f"Multiplication table for {number}:")
    multiplier = 1
    
    while multiplier <= 10:  # Generate multiplication table up to 10
        result = number * multiplier
        print(f"{number} x {multiplier} = {result}")
        multiplier += 1