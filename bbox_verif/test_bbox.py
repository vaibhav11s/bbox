# See LICENSE.iitm for license details
'''

Author   : Santhosh Pavan
Email id : santhosha@mindgrovetech.in
Details  : This file consists cocotb testbench for bbox dut

--------------------------------------------------------------------------------------------------
'''
'''
TODO:
Task Description: Add list of instructions in Testfactory block. So that testbench generates tests for listed instructions. One instruction is implemented as an example. 
		  For multiple instructions, provided as comment (see after TestFactory(TB)). Please the use the same format.
                  Note - Comments are provided for TestFactory.
		  Note - The value of instr (ANDN) is a temp value, it needed to be changed according to spec.

Note - Here testbench assumes below verilog port names are generated by bluespec compiler. Please implement the bluespec design with below port names.

 DUT Ports:
 Name                         I/O  size 
 bbox_out                       O    65/33
 CLK                            I     1 
 RST_N                          I     1 
 instr                          I    32
 rs1                            I    64/32
 rs2                            I    64/32
   (instr, rs1, rs2) -> bbox_out
'''


# generates clock and reset


import string
import random
import cocotb
import logging as _log
from cocotb.decorators import coroutine
from cocotb.triggers import Timer, RisingEdge, FallingEdge
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.regression import TestFactory
from bbox_ref_model import bbox_rm
from constants import *
NUM_TEST = 10


async def initial_setup(dut):
    cocotb.start_soon(Clock(dut.CLK, 1, units='ns').start())

    dut.RST_N.value = 0
    await RisingEdge(dut.CLK)
    dut.RST_N.value = 1


# drives input data to dut
async def input_driver(dut, instr, rs1, rs2, single_opd):
    await RisingEdge(dut.CLK)
    dut.instr.value = instr
    dut.rs1.value = rs1
    dut._log.info("---------------- DUT Input Info -----------------------")
    if single_opd == 1:
        await RisingEdge(dut.CLK)
        dut._log.info("instr = %s  rs1 = %s ", hex(
            dut.instr.value), hex(dut.rs1.value))

    else:
        dut.rs2.value = rs2
        await RisingEdge(dut.CLK)
        dut._log.info("instr = %s  rs1 = %s rs2 = %s", hex(
            dut.instr.value), hex(dut.rs1.value), hex(dut.rs2.value))
    dut._log.info("-------------------------------------------------------")

# monitors dut output


async def output_monitor(dut):
    while True:
        await RisingEdge(dut.CLK)
        if (dut.bbox_out.value[0]):
            break

    dut_result = dut.bbox_out.value
    return dut_result

# compares output of dut and rm


async def scoreboard(dut, dut_result, rm_result):
    dut._log.info("------------ Compare DUT o/p & Ref Model o/p ----------")
    dut._log.info("Expected output  = %s", rm_result)
    dut._log.info("DUT output       = %s", dut_result)
    assert rm_result == str(dut_result), "Failed"
    dut._log.info("-------------------------------------------------------")

# Testbench


async def TB(dut, XLEN, instr, instr_name, single_opd, num_of_tests):
    await initial_setup(dut)
    dut._log.info("*******************************************************")
    dut._log.info(
        "------------- Test %r of RV%d starts --------------" % (instr_name, XLEN))
    dut._log.info("*******************************************************")
    for i in range(num_of_tests):
        rs1 = random.randint(0, (2**XLEN)-1)
        rs2 = random.randint(0, (2**XLEN)-1)
        rm_result = bbox_rm(instr, rs1, rs2, XLEN)

        await input_driver(dut, instr, rs1, rs2, single_opd)
        dut_result = await output_monitor(dut)

        await scoreboard(dut, dut_result, rm_result)
    dut._log.info("*******************************************************")
    dut._log.info(
        "------------- Test %r of RV%d ends ----------------" % (instr_name, XLEN))
    dut._log.info("*******************************************************")


# generates sets of tests based on the different permutations of the possible arguments to the test function
tf = TestFactory(TB)

base = 'RV64'
# To run tests for RV32, change base = 'RV32'

# generates tests for instructions of RV32
if base == 'RV32':
    tf.add_option('XLEN', [32])
    tf.add_option(('instr', 'instr_name', 'single_opd'),
                  [
        (ZBB_ANDN, 'andn', 0),
        (ZBB_ORN, 'orn', 0),
        (ZBB_XNOR, 'xnor', 0),
        (ZBB_CLZ, 'clz', 1),
        (ZBB_CLZW, 'clzw', 1),
        (ZBB_CTZ, 'ctz', 1),
        (ZBB_CTZW, 'ctzw', 1),
        (ZBB_CPOP, 'cpop', 1),
        (ZBB_CPOPW, 'cpopw', 1),
        (ZBB_MAX, 'max', 0),
        (ZBB_MAXU, 'maxu', 0),
        (ZBB_MIN, 'min', 0),
        (ZBB_MINU, 'minu', 0),
        (ZBB_SEXTB, 'sextb', 1),
        (ZBB_SEXTH, 'sexth', 1),
        (ZBB_ZEXTH, 'zexth', 1),
        (ZBB_ROL, 'rol', 0),
        (ZBB_ROLW, 'rolw', 0),
        (ZBB_ROR, 'ror', 0),
        (ZBB_RORI, 'rori', 0),
        (ZBB_RORIW, 'roriw', 0),
        (ZBB_RORW, 'rorw', 0),
        (ZBB_ORCB, 'orcb', 1),
        (ZBB_REV8, 'rev8', 1)
    ])
    # tf.add_option(('instr','instr_name','single_opd'), [(3, 'xnor', 0)])
    # if instruction has single operand, provide single_opd = 1 (please see below line).
    # To run multiple instr - tf.add_option(((('instr','instr_name','single_opd'), [(1, 'andn', 0),(2,'clz',1),(...)])

# generates tests for instructions of RV64
elif base == 'RV64':
    tf.add_option('XLEN', [64])
    tf.add_option(('instr', 'instr_name', 'single_opd'),
                  [
        (ZBB_ANDN, 'andn', 0),
        (ZBB_ORN, 'orn', 0),
        (ZBB_XNOR, 'xnor', 0),
        (ZBB_CLZ, 'clz', 1),
        (ZBB_CLZW, 'clzw', 1),
        (ZBB_CTZ, 'ctz', 1),
        (ZBB_CTZW, 'ctzw', 1),
        (ZBB_CPOP, 'cpop', 1),
        (ZBB_CPOPW, 'cpopw', 1),
        (ZBB_MAX, 'max', 0),
        (ZBB_MAXU, 'maxu', 0),
        (ZBB_MIN, 'min', 0),
        (ZBB_MINU, 'minu', 0),
        (ZBB_SEXTB, 'sextb', 1),
        (ZBB_SEXTH, 'sexth', 1),
        (ZBB_ZEXTH, 'zexth', 1),
        (ZBB_ROL, 'rol', 0),
        (ZBB_ROLW, 'rolw', 0),
        (ZBB_ROR, 'ror', 0),
        (ZBB_RORI, 'rori', 0),
        (ZBB_RORIW, 'roriw', 0),
        (ZBB_RORW, 'rorw', 0),
        (ZBB_ORCB, 'orcb', 1),
        (ZBB_REV8, 'rev8', 1)
    ])
    # tf.add_option(('instr','instr_name','single_opd'), [(3, 'xnor', 0)])
    # if instruction has single operand, provide single_opd = 1 (please see below line).
    # To run multiple instr - tf.add_option(((('instr','instr_name','single_opd'), [(1, 'andn', 0),(2,'clz',1),(...)])

# for each instruction below line generates 10 test vectors, can change to different no.
tf.add_option('num_of_tests', [NUM_TEST])
tf.generate_tests()
