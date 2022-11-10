function Bit#(XLEN) fn_andn(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // AND with inverted operand
  return rs1 & ~rs2;
endfunction

function Bit#(XLEN) fn_orn(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // OR with inverted operand
  return rs1 | ~rs2;
endfunction

function Bit#(XLEN) fn_xnor(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Exclusive NOR
  return ~(rs1 ^ rs2);
endfunction

function Bit#(XLEN) fn_clz(Bit#(XLEN) rs); // Count leading zero bits
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

function Bit#(XLEN) fn_clzw(Bit#(XLEN) rs); // Count leading zero bits in word
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

function Bit#(XLEN) fn_ctz(Bit#(XLEN) rs); // Count trailing zero bits
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

function Bit#(XLEN) fn_ctzw(Bit#(XLEN) rs); // Count trailing zero bits in word
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

function Bit#(XLEN) fn_cpop(Bit#(XLEN) rs); // Count set bits
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  for(i = 0; i < ln; i = i + 1)
    if(rs[i] == 1)
      result = result + 1;
  return result;
endfunction

function Bit#(XLEN) fn_cpopw(Bit#(XLEN) rs); // Count set bits in word
  Bit#(XLEN) result = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 31;
  for(i = 31; i >= 0; i = i - 1)
    if(rs[i] == 1)
      result = result + 1;
  return result;
endfunction

function Bit#(XLEN) fn_max(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Maximum
  Int#(XLEN) s1 = unpack(rs1);
  Int#(XLEN) s2 = unpack(rs2);
  Bit#(XLEN) result = pack(max(s1,s2));
  return result;
endfunction

function Bit#(XLEN) fn_maxu(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Unsigned Maximum
  return max(rs1,rs2);
endfunction

function Bit#(XLEN) fn_min(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Minimum
  Int#(XLEN) s1 = unpack(rs1);
  Int#(XLEN) s2 = unpack(rs2);
  Bit#(XLEN) result = pack(min(s1,s2));
  return result;
endfunction

function Bit#(XLEN) fn_minu(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Unsigned Minimum
  return min(rs1,rs2);
endfunction

function Bit#(XLEN) fn_sextb(Bit#(XLEN) rs); // Sign-extend halfword
  Bit#(XLEN) result = rs;
  Integer ln = valueOf(XLEN);
  Integer i = 8;
  for(i = 8; i < ln; i = i + 1)
    result[i] = rs[7]; 
  return result;
endfunction

function Bit#(XLEN) fn_sexth(Bit#(XLEN) rs); 
  Bit#(XLEN) result = rs;
  Integer ln = valueOf(XLEN);
  Integer i = 16;
  for(i = 16; i < ln; i = i + 1)
    result[i] = rs[15];
  return result;
endfunction

function Bit#(XLEN) fn_zexth(Bit#(XLEN) rs); // Zero-extend halfword
  Integer ln = valueOf(XLEN);
  Bit#(XLEN) result = rs;
  Integer i = 16;
  for(i = 16; i < ln; i = i + 1)
    result[i] = 0;
  return result;
endfunction
