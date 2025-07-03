import sys

def count_arguments():
    num_args = len(sys.argv) - 1  # Exclude the program name itself
    print(f"Number of arguments: {num_args}")

count_arguments()
