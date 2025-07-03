def convert_temperature(temp):
    if temp[-1].upper() == 'C':
        celsius = float(temp[:-1])
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit
    else:
        return None


def main():
    temperatures = []
    for _ in range(6):
        temp = input("Enter temperature in centigrade (e.g., 25C): ")
        fahrenheit = convert_temperature(temp)
        if fahrenheit is not None:
            temperatures.append(fahrenheit)
        else:
            print("Invalid input format. Please enter a number followed by 'C'.")

    if temperatures:
        max_temp = max(temperatures)
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        print(f"Maximum Temperature: {max_temp:.2f}F")
        print(f"Minimum Temperature: {min_temp:.2f}F")
        print(f"Mean Temperature: {mean_temp:.2f}F")

main()
