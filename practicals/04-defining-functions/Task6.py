def convert_temperature(temp):
    if temp[-1].upper() == 'C':
        celsius = float(temp[:-1])
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit:.2f}F"
    else:
        return "Invalid input format. Please enter a number followed by 'C'."


temperature = input("Enter temperature in centigrade (e.g., 25C): ")
print(convert_temperature(temperature))
