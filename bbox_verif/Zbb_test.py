
def andn(rs1, rs2, XLEN):  # rs1 & ~rs2
    return rs1 & ~rs2


def orn(rs1, rs2, XLEN):  # rs1 | ~rs2
    b1 = bin(rs1)[2:]  # delete '0b'
    b2 = bin(rs2)[2:]  # delete '0b'
    b2 = "".join(['1' if n == '0' else '0' for n in b2])  # b2 = ~ b2
    ba = ''
    for i in range(1, XLEN+1):  # calc ( rs1 | ~ rs2 )
        c1 = 0
        c2 = 1
        if len(b1) >= i:  # preceding 0's
            c1 = int(b1[-i])
        if len(b2) >= i:  # preceding 1's
            c2 = int(b2[-i])
        ba = str(c1 or c2) + ba
    return int(ba, 2)


def xnor(rs1, rs2, XLEN):  # ~(rs1 ^ rs2)
    b1 = bin(rs1)[2:]  # delete '0b'
    b2 = bin(rs2)[2:]  # delete '0b'
    ba = ''
    for i in range(1, XLEN+1):  # calc ~ ( rs1 ^ rs2 )
        c1 = 0
        c2 = 0
        if len(b1) >= i:  # preceding 0's
            c1 = int(b1[-i])
        if len(b2) >= i:  # preceding 0's
            c2 = int(b2[-i])
        ba = str(1 - (c1 ^ c2)) + ba
    return int(ba, 2)
