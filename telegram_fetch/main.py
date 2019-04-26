from helpers import cli_args, init_logging
import telefetch as tg

log = init_logging()
TELEGRAM_CLI_PATH = '/usr/bin/telegram-cli'
TELEGRAM_KEY_PATH = '/etc/telegram-cli/server.pub'

def main():
    """
    Parses command line arguments
    and calls a telegram api for messages
    """
    peer, msg_path = cli_args(None, "./tg_messages")
    log.debug(f"using database {msg_path} and user {peer}")
    tg.init(TELEGRAM_CLI_PATH,
            TELEGRAM_KEY_PATH)
    print(tg)

    if peer:
        hist = tg.history(peer)
        print(hist,10)

if __name__=='__main__':

    main()

