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
        res = Zbb.clz(rs1,XLEN)
        valid = '1'
    elif instr == ZBB_CLZW:
        res = Zbb.clzw(rs1,XLEN)
        valid = '1'
    elif instr == ZBB_CTZ:
        res = Zbb.ctz(rs1,XLEN)
        valid = '1'
    elif instr == ZBB_CTZW:
        res = Zbb.ctzw(rs1,XLEN)
        valid = '1'
    elif instr == ZBB_CPOP:
        res = Zbb.cpop(rs1,XLEN)
        valid = '1'
    elif instr == ZBB_CPOPW:
        res = Zbb.cpopw(rs1,XLEN)
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
