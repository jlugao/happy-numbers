

def vigenere(inp: str, passfrase: str) -> str:
    new_pass = extend_string(passfrase, len(inp))
    return ''.join(map(encode_letter, inp.lower() , new_pass.lower()))

def encode_letter(inp: str, pwd: str) -> str:
    '''
    rotate to the position of the letter
    '''
    return chr( ((position(inp) + position(pwd)) %26) + ord('a') )

def extend_string(text: str, size: int) -> str:
    '''
        extends string to fit desired length
        'teste', 2 -> te
        'teste', 6 - testet
        ...
    '''
    factor = (size // len(text)) + 1
    return (text * factor)[:size]

def position(letra: str) -> int:
    '''
        gives the position in the alphabet
        ( shifted to 'a' -> 0)
    '''
    return ord(letra.lower()) - ord('a') 