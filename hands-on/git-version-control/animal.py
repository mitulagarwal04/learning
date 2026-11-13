import sys

def cat():
    print('cat')

def dog():
    print('D')

def default():
    print('Hello!')

def main():

    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1]=='dog':
        dog()
    else:
        default()

if __name__ == "__main__":
    main()  