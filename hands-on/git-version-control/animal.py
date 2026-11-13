import sys

def dog():
    print('D')

def default():
    print('hello')

def main():
    if sys.argv == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()
