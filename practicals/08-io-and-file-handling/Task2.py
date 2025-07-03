import sys

def diff(Anas, Mohamed):
    try:
        with open(Anas, 'r') as f1, open(Mohamed, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            if content1 == content2:
                print("Files are the same.")
            else:
                print("Files are different.")
    except FileNotFoundError as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diff.py <Anas> <Mohamed>")
    else:
        diff(sys.argv[1], sys.argv[2])
