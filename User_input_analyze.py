import sys


def main():
    args = sys.argv
    help_message = 'Type -h or --help to get help.'
    info = 'Use -p or --path to specify path to file'

    if len(args) <= 1:
        print('Need more arguments.', help_message, sep='\n')
        exit()

    elif args[0] == '-h' or args[0] == '--help':
        print(info)

    elif args[0] == '-p' or args[0] == '--path':
        print(args[1])

    else:
        print('Invalid arguments.', help_message, sep='\n')
        exit()


if __name__ == "__main__":
    main()
