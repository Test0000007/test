def base58Encode(hexs):
    text=""
    letters = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    if(isinstance(hexs, bytes)):
        hx = int.from_bytes(hexs,"big")
    hhh=0
    while(hx>0):
        hx, hhh = divmod(hx,58)
        text = letters[hhh] + text

    for i in range(len(hexs)):
        if(hexs[i] > 0):
            break;
        else:
            text = '1' + text
    return text


def base58Decode(s58):
    byt = b''
    letters = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    ss = list(s58)
    total = 0
    place = 0
    while(len(ss) > 0):
        total += ((58**place)*letters.index(ss.pop()))
        place += 1
    return hex(total)

def newChange():
    print("TEST")
    print("ADDITION")

def secondChange():
    print(2 + 2)
    
