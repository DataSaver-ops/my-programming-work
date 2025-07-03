import sys

def load_dictionary(dict_path):
    try:
        with open(dict_path, 'r') as file:
            return set(word.strip().lower() for word in file.readlines())
    except FileNotFoundError:
        print(f"Dictionary file {dict_path} not found.")
        return set()

def spell(filename, dict_path):
    dictionary = load_dictionary(dict_path)
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            for word in words:
                if word.lower() not in dictionary:
                    print(word)
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python spell.py HELLO.TXT DIC.XT")
    else:
        spell(sys.argv[1], sys.argv[2])




