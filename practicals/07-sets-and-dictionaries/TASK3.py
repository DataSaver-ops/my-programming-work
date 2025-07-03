def manage_countries():
    countries = {}
    while True:
        country = input("Enter the name of a country (or 'exit' to quit): ").strip().lower()
        if country == 'exit':
            break
        if country in countries:
            print(f"The capital of {country.title()} is {countries[country]}.")
        else:
            capital = input(f"Enter the capital city of {country.title()}: ").strip()
            countries[country] = capital
            print(f"Added {country.title()} with its capital {capital}.")


manage_countries()
