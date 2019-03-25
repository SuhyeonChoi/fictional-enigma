import sys


def create_dictionary(file_name):
    f = open(file_name)
    text = f.read()
    f.close()

    words = text.split()

    d = {}

    for w in range(len(words)):
        if '!' or '.' or '?' not in words:
            d[words[w]] == words[w+1]
        else:
            return ' '
    print(d)


def main():
    try:
        name = sys.argv[1]
        create_dictionary(name)
    except FileNotFoundError:
        print("This file doesn't exist.")


if __name__ == "__main__":
	main()