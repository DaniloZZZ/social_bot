import sys, logging

def init_logging():
    logging.basicConfig(level=logging.DEBUG)
    return logging

def cli_args(*a):
    """
    Gets some arguments and
    tries to override them from sys.argv
    """
    args = list(a)
    for i in range(len(sys.argv)):
        try:
            args[i] = sys.argv[i+1]
        except IndexError:
            break
    print(args)
    return args

