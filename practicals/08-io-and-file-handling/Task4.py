import sys

def wc(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            num_chars = sum(len(line) for line in lines)
            print(f"Lines: {num_lines}")
            print(f"Characters: {num_chars}")
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python wc.py Hello")
    else:
        wc(sys.argv[1])







