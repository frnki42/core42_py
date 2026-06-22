import sys


def main():
    if len(sys.argv) < 2:
        print("usage: python3 exec.py <strings>")
        return
    text = " ".join(sys.argv[1:])
    text = text[::-1].swapcase()
    print(text)


main()
