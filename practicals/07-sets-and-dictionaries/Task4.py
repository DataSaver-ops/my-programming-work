from collections import Counter

def frequency_analysis(message):
    message = message.lower()
    counter = Counter(filter(str.isalpha, message))
    most_common = counter.most_common(6)
    for letter, count in most_common:
        print(f"{letter}: {count}")

frequency_analysis("This is a sample message to demonstrate frequency analysis.")
