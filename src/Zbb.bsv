function Bit#(XLEN) fn_andn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 & ~rs2;
endfunction

function Bit#(XLEN) fn_orn(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return rs1 | ~rs2;
endfunction

function Bit#(XLEN) fn_xnor(Bit#(XLEN) rs1, Bit#(XLEN) rs2);
  return ~(rs1 ^ rs2);
endfunction

function Bit#(XLEN) fn_clz(Bit#(XLEN) rs); // TODO :
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = ln - 1;
  Bool add = True;
  for(i = ln - 1; i >= 0; i = i - 1)
    if(add == True && rs[i] == 0)
      result = result + 1;
    else
      add = False;
  return result;
endfunction

function Bit#(XLEN) fn_clzw(Bit#(XLEN) rs); // TODO :
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 31;
  Bool add = True;
  for(i = 31; i >= 0; i = i - 1)
    if(add == True && rs[i] == 0)
      result = result + 1;
    else
      add = False;
  return result;
endfunction

function Bit#(XLEN) fn_ctz(Bit#(XLEN) rs); // TODO :
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  Bool add = True;
  for(i = 0; i < ln; i = i + 1)
    if(add == True && rs[i] == 0)
      result = result + 1;
    else
      add = False;
  return result;
endfunction

function Bit#(XLEN) fn_ctzw(Bit#(XLEN) rs); // TODO :
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  Bool add = True;
  for(i = 0; i < 32; i = i + 1)
    if(add == True && rs[i] == 0)
      result = result + 1;
    else
      add = False;
  return result;
endfunction

function Bit#(XLEN) fn_cpop(Bit#(XLEN) rs); // TODO :
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  for(i = 0; i < ln; i = i + 1)
    if(rs[i] == 1)
      result = result + 1;
  return result;
endfunction

function Bit#(XLEN) fn_cpopw(Bit#(XLEN) rs); // TODO :
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 31;
  for(i = 31; i >= 0; i = i - 1)
    if(rs[i] == 1)
      result = result + 1;
  return result;
endfunction