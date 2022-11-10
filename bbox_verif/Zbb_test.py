from utils import getBits


def andn(rs1, rs2, XLEN):
    """rs1 & ~rs2"""

    return rs1 & ~rs2


def orn(rs1, rs2, XLEN):
    """rs1 | ~rs2"""

    b1, b2 = getBits(rs1, XLEN), getBits(rs2, XLEN)
    ba = ''

    for B1, B2 in zip(b1, b2):
        c1 = int(B1)
        c2 = int(B2)
        out = c1 or (1-c2)
        ba = ba + str(out)

    return int(ba, 2)


def xnor(rs1, rs2, XLEN):
    """~(rs1 ^ rs2)"""

    b1, b2 = getBits(rs1, XLEN), getBits(rs2, XLEN)
    ba = ''

    for B1, B2 in zip(b1, b2):  # calc ~ ( rs1 ^ rs2 )
        c1 = int(B1)
        c2 = int(B2)
        out = 1 - (c1 ^ c2)
        ba = ba + str(out)

    return int(ba, 2)


def clz(rs, XLEN):
    """counts the number of 0’s before the first 1, starting at the most-significant bit"""

    b = getBits(rs, XLEN)
    count = 0

    for B in b:
        if B == '0':
            count += 1
        else:
            break

    return count


def clzw(rs, XLEN):
    """counts the number of 0’s before the first 1 starting at bit 31 and progressing to bit 0"""

    b = getBits(rs, XLEN)
    count = 0

    for B in b[-32:]:
        if B == '0':
            count += 1
        else:
            break

    return count


def ctz(rs, XLEN):
    """counts the number of 0’s before the first 1, starting at the least-significant bit"""

    b = getBits(rs, XLEN)
    count = 0

    for B in reversed(b):
        if B == '0':
            count += 1
        else:
            break

    return count


def ctzw(rs, XLEN):
    """counts the number of 0’s before the first 1, starting at the least-significant bit (i.e., 0) and progressing to the most-significant bit of the least-significant word """

    b = getBits(rs, XLEN)
    count = 0

    for B in reversed(b[-32:]):
        if B == '0':
            count += 1
        else:
            break

    return count


def cpop(rs, XLEN):
    """counts the number of 1’s (i.e., set bits) in the source register."""

    b = getBits(rs, XLEN)
    count = 0

    for B in b:
        if B == '1':
            count += 1

    return count


def cpopw(rs, XLEN):
    """counts the number of 1’s (i.e., set bits) in the least-significant word of the source register"""

    b = getBits(rs, XLEN)
    count = 0

    for B in (b[-32:]):
        if B == '1':
            count += 1

    return count


def max(rs1, rs2, XLEN):
    """returns the larger of two signed integers"""

    b1, b2 = getBits(rs1, XLEN), getBits(rs2, XLEN)

    if b1[0] == b2[0]:
        if rs1 > rs2:
            return rs1
        return rs2

    if b1[0] == '0':
        return rs1

    return rs2


def maxu(rs1, rs2, XLEN):
    """returns the larger of two unsigned integers"""

    if rs1 > rs2:
        return rs1
    return rs2


def min(rs1, rs2, XLEN):
    """returns the smaller of two signed integers"""

    b1, b2 = getBits(rs1, XLEN), getBits(rs2, XLEN)

    if b1[0] == b2[0]:
        if rs1 < rs2:
            return rs1
        return rs2

    if b1[0] == '0':
        return rs2

    return rs1


def minu(rs1, rs2, XLEN):
    """returns the smaller of two unsigned integers"""

    if rs1 < rs2:
        return rs1
    return rs2


def sextb(rs, XLEN):
    """sign-extends the least-significant byte in the source to XLEN by copying the most-significant bit in the byte to all of the more-significant bits"""

    b = getBits(rs, XLEN)
    c = b[-8]
    ba = b[-8:]
    i = 0
    while i < (XLEN-8):
        ba = c + ba
        i += 1

    return int(ba, 2)


def sexth(rs, XLEN):
    """sign-extends the least-significant halfword in rs to XLEN by copying the most-significant bit in the halfword to all of the more-significant bits"""

    b = getBits(rs, XLEN)
    c = b[-16]
    ba = b[-16:]

    i = 0
    while i < (XLEN-16):
        ba = c + ba
        i += 1

    return int(ba, 2)


def zexth(rs, XLEN):
    """zero-extends the least-significant halfword of the source to XLEN by inserting 0’s into all of the bits more significant"""

    b = getBits(rs, XLEN)

    ba = b[-16:]
    i = 0
    while i < (XLEN-16):
        ba = '0' + ba
        i += 1

    return int(ba, 2)
