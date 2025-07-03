import sys

def find_shortest_argument():
    if len(sys.argv) > 1:
        arguments = sys.argv[1:]  # Exclude the program name itself
        shortest = min(arguments, key=len)
        print(f"Shortest argument: {shortest}")
    else:
        print("No arguments provided.")

find_shortest_argument()
