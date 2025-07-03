import sys

def nl(HelloAnas):
    try:
        with open(HelloAnas, 'r') as file:
            lines = file.readlines()
            for idx, line in enumerate(lines, start=1):
                print(f"{idx} {line.strip()}")
    except FileNotFoundError:
        print(f"File {HelloAnas} not found.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nl.py <HelloAnas>")
    else:
        nl(sys.argv[1])
