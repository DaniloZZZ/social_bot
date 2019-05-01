import json
import sys

NEW_MSG =" <MSG> "
NEW_PEER =" <PEER>\n"

def msg_source(path):
    with open(path, 'r') as f:
        for num, msg_json in enumerate(f):
            msg = json.loads(msg_json)
            yield msg

def main():
    if len(sys.argv)<2: print("Please provide a filepath to telegram messages dump")
    path = sys.argv[1]

    result=''
    current_usr = None
    for message in msg_source(path):
        text = message.get('text','')
        user = message.get('from',{}).get('peer_id',-1)
        if user!=current_usr:
            result= NEW_PEER + result
            current_usr=user
        result=text+ NEW_MSG +result
    print(result)

if __name__=='__main__':
    main()
