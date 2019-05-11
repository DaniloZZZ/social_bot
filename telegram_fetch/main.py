from helpers import cli_args, init_logging, append_file
import telefetch as tg
import json
import time, random

log = init_logging()
TELEGRAM_CLI_PATH = '/usr/bin/telegram-cli'
TELEGRAM_KEY_PATH = '/etc/telegram-cli/server.pub'

def lines_in_file(fname):
    i = 0
    try:
        with open(fname) as f:
            for i,l in enumerate(f,1):
                pass
    except FileNotFoundError:
        print("File {fname} does not exist")
        return 0
    print("File {fname} has {i} lines")
    return i

def main():
    """
    Parses command line arguments
    and calls a telegram api for messages
    """
    peer, msg_path, count, step = cli_args(None, "./messages", 10*1000, 300)
    count, step = int(count), int(step)
    log.debug(f"using database {msg_path} and user {peer}")
    tg.init(TELEGRAM_CLI_PATH,
            TELEGRAM_KEY_PATH)
    DUMP_FILE = msg_path+'/'+peer
    file_len = lines_in_file(DUMP_FILE)

    start = file_len
    if peer:
        for offset in range(start,count,step):
            hist = tg.history(peer, limit=step, offset=offset, retry_connect=3, result_timeout=13)
            hist.reverse()
            time.sleep(random.random())
            for m in hist:
                s = json.dumps(m,ensure_ascii=False)
                append_file(DUMP_FILE, s)

if __name__=='__main__':
    main()

