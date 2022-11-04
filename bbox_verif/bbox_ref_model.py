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




from constants import *
def bbox_rm(instr, rs1, rs2, XLEN):

    if instr == C_ANDN:  # andn vrfy
        res = rs1 & ~rs2
        valid = '1'
    # logic for all other instr starts
    elif instr == C_ORN:  # orn vrfy
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

        res = int(ba, 2)
        valid = '1'
    elif instr == C_XNOR:  # xnor vrfy
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

        res = int(ba, 2)
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
