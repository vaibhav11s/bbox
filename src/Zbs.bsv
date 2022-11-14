// bclr
function Bit#(XLEN) fn_bclr(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Bit#(XLEN) tmp = fromInteger(valueOf(XLEN)-1);
    return rs1 & ~( 1 << (rs2 & tmp));
  endfunction

// bclri
function Bit#(XLEN) fn_bclri(Bit#(XLEN) rs1, Bit#(6) shamt);
    if(valueOf(XLEN) == 32) shamt[5] = 0;
    return rs1 & ~( 1 << (shamt));
  endfunction

// bext
function Bit#(XLEN) fn_bext(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Bit#(XLEN) tmp = fromInteger(valueOf(XLEN)-1);
    return (rs1 >> (rs2 & tmp)) & 1;
  endfunction

// bexti
function Bit#(XLEN) fn_bexti(Bit#(XLEN) rs1, Bit#(6) shamt);
    if(valueOf(XLEN) == 32) shamt[5] = 0;
    return (rs1 >> (shamt)) & 1;
  endfunction

// binv
function Bit#(XLEN) fn_binv(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Bit#(XLEN) tmp = fromInteger(valueOf(XLEN)-1);
    return rs1 ^ (1 << (rs2 & tmp));
  endfunction

// binvi
function Bit#(XLEN) fn_binvi(Bit#(XLEN) rs1, Bit#(6) shamt);
    if(valueOf(XLEN) == 32) shamt[5] = 0;
    return rs1 ^ (1 << (shamt));
  endfunction

// bset
function Bit#(XLEN) fn_bset(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
    Bit#(XLEN) tmp = fromInteger(valueOf(XLEN)-1);
    return rs1 | (1 << (rs2 & tmp));
  endfunction

// bseti
function Bit#(XLEN) fn_bseti(Bit#(XLEN) rs1, Bit#(6) shamt);
    if(valueOf(XLEN) == 32) shamt[5] = 0;
    return rs1 | (1 << (shamt));
  endfunction