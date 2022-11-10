from utils import getBits


def clmul(rs1, rs2, XLEN):
    """produces the lower half of the 2·XLEN carry-less product"""

    out = 0
    for i in range(XLEN):
        if rs2 >> i & 1:
            out ^= rs1 << i

    return out


def clmulh(rs1, rs2, XLEN):
    """produces the upper half of the 2·XLEN carry-less product"""

    out = 0
    for i in range(1, XLEN):
        if rs2 >> i & 1:
            out ^= (rs1 >> (XLEN - i))

    return out


def clmulr(rs1, rs2, XLEN):
    """produces bits 2·XLEN−2:XLEN-1 of the 2·XLEN carry-less product"""

    out = 0
    for i in range(XLEN-1):
        if rs2 >> i & 1:
            out ^= (rs1 >> (XLEN - i - 1))

    return out
