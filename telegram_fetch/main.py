from helpers import cli_args, init_logging, append_file
import telefetch as tg
import json
import time, random

log = init_logging()
TELEGRAM_CLI_PATH = '/usr/bin/telegram-cli'
TELEGRAM_KEY_PATH = '/etc/telegram-cli/server.pub'

def main():
    """
    Parses command line arguments
    and calls a telegram api for messages
    """
    peer, msg_path = cli_args(None, "./messages")
    log.debug(f"using database {msg_path} and user {peer}")
    tg.init(TELEGRAM_CLI_PATH,
            TELEGRAM_KEY_PATH)

    step = 30
    count = 10*1000
    start = 990
    if peer:
        for offset in range(start,count,step):
            hist = tg.history(peer, limit=step, offset=offset, retry_connect=3, result_timeout=13)
            hist.reverse()
            time.sleep(random.random())
            for m in hist:
                s = json.dumps(m,ensure_ascii=False)
                append_file(msg_path+'/'+peer, s)

if __name__=='__main__':
    main()

