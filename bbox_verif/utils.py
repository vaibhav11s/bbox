def getBits(n, XLEN: int) -> str:
    """get bit representation of n of length XLEN"""
    b = bin(n)[2:]  # delete '0b'
    if len(b) > XLEN:
        b = b[-XLEN:]
    while len(b) != XLEN:
        b = '0' + b
    return b
