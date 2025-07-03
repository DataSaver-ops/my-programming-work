import sys

def grep(pattern, Say_Cheese):
    try:
        with open(Say_Cheese, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if pattern in line:
                    print(line.strip())
    except FileNotFoundError:
        print(f"File {fSay_Cheese} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python grep.py <pattern> <Say_Cheese>")
    else:
        grep(sys.argv[1], sys.argv[2])
