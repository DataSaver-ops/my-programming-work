def count_case_letters(input_string):

    uppercase_count = sum(1 for char in input_string if char.isupper())
    lowercase_count = sum(1 for char in input_string if char.islower())
    return uppercase_count, lowercase_count


test_string = "Mohamed Anas"
uppercase, lowercase = count_case_letters(test_string)
print(f"In the string '{test_string}':")
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
