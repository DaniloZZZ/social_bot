import sys, logging

def init_logging():
    logging.basicConfig(level=logging.DEBUG)
    return logging

def save_file(fname,txt):
    with open(fname,'w+') as f:
        logging.debug(f"writing file {fname}")
        f.write(txt)

def append_file(fname,txt):
    with open(fname,'a+') as f:
        logging.debug(f"appending file {fname}")
        f.write(txt+'\n')

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

