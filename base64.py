def base64Encode(hexs):
    text=b''
    letters = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    b64 = hexs

    while(b64):
        b64text = b64[:3]
        b64 = b64[3:]

        xo = b64text[0] >> 2
        text += bytes([letters[xo]])

        if(len(b64text)%3 == 1):
            xo =(b64text[0]%4 << 4)
            text += bytes([letters[xo]])
            return text + "=="

        xo =(b64text[0]%4 << 4)+(b64text[1] >> 4)
        text += bytes([letters[xo]])

        if(len(b64text)%3 == 2):
            xo =( (b64text[1]%16) << 2 )
            text += bytes([letters[xo]])
            return text+"="
        xo =( (b64text[1] % 16) << 2 ) + (b64text[2] >> 6)
        text += bytes([letters[xo]])
        xo =(b64text[2] % 64)
        text += bytes([letters[xo]])
    return text


def base64Decode(s64):
    byt = b''
    letters = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    while(s64):
        templet = s64[:4]
        s64 = s64[4:]
        byt += bytes([( letters.index(bytes([templet[0]])) <<2 )+ (letters.index(bytes([templet[1]])) >> 4)])
        if(templet[2] == '='):
            endbyt = bytes([( (letters.index(bytes[templet[1]]) % 16) << 4) ])
            if(endbyt[0]):
                byt + endbyt
            return byt
        byt += bytes([( (letters.index(bytes([templet[1]])) % 16) << 4) + ( letters.index(bytes([templet[2]])) >> 2)])
        if(templet[3] == '='):
            endbyt = bytes([((letters.index(bytes[templet[2]]) % 4) << 6) ])
            if(endbyt[0]):
                byt + endbyt
            return byt
        byt += bytes([((letters.index(bytes([templet[2]])) % 4) << 6) + letters.index(bytes([templet[3]]))])

    return byt
