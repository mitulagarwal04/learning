import sys

def cat():
    print('C!')

def default():
    print('Hello!')

def main():
    if sys.argv == 'cat':
        cat()
    else:
        default()

if __name__ == '__main__':
    main()
