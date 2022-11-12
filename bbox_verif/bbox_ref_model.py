# See LICENSE.iitm for license details
'''

Author   : Santhosh Pavan
Email id : santhosh@mindgrovetech.in
Details  : This file consists reference model which is used in verifying the bbox design (DUT).

--------------------------------------------------------------------------------------------------
'''
'''
TODO:
Task Description: Add logic for all instructions. One instruction is implemented as an example. 
                  Note - The value of instr (ANDN) is a temp value, it needed to be changed according to spec.

Note - if instr has single operand, take rs1 as an operand
'''

# Reference model




import Zbb_test as Zbb
import Zbc_test as Zbc
import Zbs_test as Zbs
import Zba_test as Zba
from constants import *
def bbox_rm(instr, rs1, rs2, XLEN):

    if instr == ZBB_ANDN:  # andn vrfy
        res = Zbb.andn(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_ORN:
        res = Zbb.orn(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_XNOR:  # xnor vrfy
        res = Zbb.xnor(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_CLZ:
        res = Zbb.clz(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_CLZW:
        res = Zbb.clzw(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_CTZ:
        res = Zbb.ctz(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_CTZW:
        res = Zbb.ctzw(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_CPOP:
        res = Zbb.cpop(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_CPOPW:
        res = Zbb.cpopw(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_MAX:
        res = Zbb.max(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_MAXU:
        res = Zbb.maxu(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_MIN:
        res = Zbb.min(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_MINU:
        res = Zbb.minu(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_SEXTB:
        res = Zbb.sextb(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_SEXTH:
        res = Zbb.sexth(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_ZEXTH:
        res = Zbb.zexth(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_ROL:
        res = Zbb.rol(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_ROLW:
        res = Zbb.rolw(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_ROR:
        res = Zbb.ror(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_RORI:
        res = Zbb.ror(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_RORIW:
        res = Zbb.rorw(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_RORW:
        res = Zbb.rorw(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBB_ORCB:
        res = Zbb.orcb(rs1, XLEN)
        valid = '1'
    elif instr == ZBB_REV8:
        res = Zbb.rev8(rs1, XLEN)
        valid = '1'
    elif instr == ZBC_CLMUL:
        res = Zbc.clmul(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBC_CLMULH:
        res = Zbc.clmulh(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBC_CLMULR:
        res = Zbc.clmulr(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BCLR:
        res = Zbs.bclr(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BCLRI:
        res = Zbs.bclr(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BEXT:
        res = Zbs.bext(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BEXTI:
        res = Zbs.bext(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BINV:
        res = Zbs.binv(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BINVI:
        res = Zbs.binv(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BSET:
        res = Zbs.bset(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBS_BSETI:
        res = Zbs.bset(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_ADDUWZ:
        res = Zba.adduwz(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SH1ADD:
        res = Zba.sh1add(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SH1ADDUW:
        res = Zba.sh1adduw(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SH2ADD:
        res = Zba.sh2add(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SH2ADDUW:
        res = Zba.sh2adduw(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SH3ADD:
        res = Zba.sh3add(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SH3ADDUW:
        res = Zba.sh3adduw(rs1, rs2, XLEN)
        valid = '1'
    elif instr == ZBA_SLLIUW:
        res = Zba.slliuw(rs1, XLEN)
        valid = '1'
    # logic for all other instr ends
    else:
        res = 0
        valid = '0'
    result = ''
    if XLEN == 32:
        result = '{:032b}'.format(res)
    elif XLEN == 64:
        result = '{:064b}'.format(res)
    return valid+result
