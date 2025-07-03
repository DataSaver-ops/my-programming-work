
def remove_last_character(input_string):
    if len(input_string) > 1:
        return input_string[:-1]
    return input_string


print(remove_last_character("hi\n"))
print(remove_last_character("A"))
print(remove_last_character(""))

