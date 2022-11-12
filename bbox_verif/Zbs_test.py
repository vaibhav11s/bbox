from utils import getBits


def bclr(rs1, rs2, XLEN):
    """returns rs1 with a single bit cleared at the index specified in rs2"""

    i = rs2 & (XLEN-1)
    out = rs1 & ~(1 << i)

    return out


def bext(rs1, rs2, XLEN):
    """returns a single bit extracted from rs1 at the index specified in rs2"""

    i = rs2 & (XLEN-1)
    out = (rs1 >> i) & 1

    return out


def binv(rs1, rs2, XLEN):
    """returns rs1 with a single bit inverted at the index specified in rs2"""

    i = rs2 & (XLEN-1)
    out = rs1 ^ (1 << i)

    return out


def bset(rs1, rs2, XLEN):
    """returns rs1 with a single bit set at the index specified in rs2"""

    i = rs2 & (XLEN-1)
    out = rs1 | (1 << index)

    return out
