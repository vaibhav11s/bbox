from utils import getBits


def adduw(rs1, rs2, XLEN):
    """performs an XLEN-wide addition between rs2 and the zero-extended least-significant word of rs1"""

    b1 = getBits(rs1, XLEN)
    c = b1[-32:]
    for i in range(32):
        c = '0'+c
    rs = int(c, 2)
    out = rs2 + rs
    return out


def sh1add(rs1, rs2, XLEN):
    """shifts rs1 to the left by 1 bit and adds it to rs2"""

    out = rs2 + (rs1 << 1)
    ans = getBits(out, XLEN)
    return int(ans, 2)


def sh1adduw(rs1, rs2, XLEN):
    """performs an XLEN-wide addition of two addends"""

    b1 = getBits(rs1, XLEN)
    c = b1[-32:]
    for i in range(32):
        c = '0'+c
    rs = int(c, 2)

    out = rs2 + (rs << 1)

    return out


def sh2add(rs1, rs2, XLEN):
    """shifts rs1 to the left by 2 places and adds it to rs2"""

    out = rs2 + (rs1 << 2)
    ans = getBits(out, XLEN)
    return int(ans, 2)


def sh2adduw(rs1, rs2, XLEN):
    """performs an XLEN-wide addition of two addends"""

    b1 = getBits(rs1, XLEN)
    c = b1[-32:]
    for i in range(32):
        c = '0'+c
    rs = int(c, 2)

    out = rs2 + (rs << 2)

    return out


def sh3add(rs1, rs2, XLEN):
    """shifts rs1 to the left by 3 places and adds it to rs2"""

    out = rs2 + (rs1 << 3)
    ans = getBits(out, XLEN)
    return int(ans, 2)


def sh3adduw(rs1, rs2, XLEN):
    """performs an XLEN-wide addition of two addends"""

    b1 = getBits(rs1, XLEN)
    c = b1[-32:]
    for i in range(32):
        c = '0'+c
    rs = int(c, 2)

    out = rs2 + (rs << 3)

    return out


def slliuw(rs1, shamt, XLEN):
    """takes the least-significant word of rs1, zero-extends it, and shifts it left by the immediate"""

    b = int(getBits(rs1, XLEN)[-32:] + "0"*shamt, 2)
    ans = getBits(b, XLEN)
    return int(ans, 2)


"""
rs1 = 0b11000010000111001000101100110011011010001010101001000111100111 rs2 = 0b11010010100010100001101010101010100111011010010100100000100010

111011010001010101001000111100111000000000000000000000000000000000000000000000000000000
10111100111000000000000000000000000000000000000000000000000000000
"""
