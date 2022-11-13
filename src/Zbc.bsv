function Bit#(XLEN) fn_clmul(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Carry-less multiply (low-part)
  Bit#(XLEN) res = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  for(i = 0; i < ln; i = i + 1)
    if(((rs2 >> i) & 1) != 0)
      res = res ^ (rs1 << i);
  return res;
endfunction

function Bit#(XLEN) fn_clmulh(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Carry-less multiply (high-part)
  Bit#(XLEN) res = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  for(i = 1; i < ln; i = i + 1)
    if(((rs2 >> i) & 1) != 0)
      res = res ^ (rs1 >> (ln-i));
  return res;
endfunction

function Bit#(XLEN) fn_clmulr(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Carry-less multiply (reversed)
  Bit#(XLEN) res = 0;
  Integer ln = valueOf(XLEN);
  Integer i = 0;
  for(i = 0; i < ln; i = i + 1)
    if(((rs2 >> i) & 1) != 0)
      res = res ^ (rs1 >> (ln-i-1));
  return res;
endfunction