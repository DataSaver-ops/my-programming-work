def valid_number(number):
    """Check if the number is between 0 and 100 inclusive."""
    return 0 <= number <= 100
sample_numbers = [-4,0,3,35,-9,105]

for num in sample_numbers:
    if valid_number(num):
        print(f"{num} is in the range 0 to 100.")
    else:
        print(f"{num} is NOT in the range 0 to 100.")

