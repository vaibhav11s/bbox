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

function Bit#(XLEN) fn_sextb(Bit#(XLEN) rs); // Sign-extend byte
  Bit#(XLEN) result = rs;
  Integer ln = valueOf(XLEN);
  Integer i = 8;
  for(i = 8; i < ln; i = i + 1)
    result[i] = rs[7]; 
  return result;
endfunction

function Bit#(XLEN) fn_sexth(Bit#(XLEN) rs);  // Sign-extend halfword
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

function Bit#(XLEN) fn_rol(Bit#(XLEN) rs1, Bit#(XLEN) rs2) provisos (Log#(XLEN,b), Mul#(XLEN,2,x2len)); // Rotate Left (Register)
  Integer ln = valueOf(XLEN);
  Integer ln2 = valueOf(x2len);
  Bit#(6) shamt = rs2[5:0];
  if(ln == 32)
    shamt[5] = 0;
  Bit#(XLEN) zeros = 0;
  Bit#(x2len) x = {zeros,rs1} << shamt;
  Bit#(XLEN) result = x[ln2-1:ln] | x[ln-1:0];
  return result;
endfunction

function Bit#(XLEN) fn_rolw(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Rotate Left Word (Register)
  Bit#(32) zeros = 0; 
  Integer ln = valueOf(XLEN);
  Bit#(5) shamt = rs2[4:0];
  Bit#(64) x = {zeros,rs1[31:0]} << shamt;
  Bit#(32) w = x[63:32]|x[31:0];
  Bit#(XLEN) result = rs1;
  Integer i = 0;
  for(i = 0; i < 32; i = i + 1)
    result[i] = w[i];
  for(i = 32; i < ln; i = i + 1)
    result[i] = w[31];
  return result;
endfunction

function Bit#(XLEN) fn_ror(Bit#(XLEN) rs1, Bit#(XLEN) rs2) provisos (Log#(XLEN,b),Mul#(XLEN,2,x2len)); // Rotate Right (Register)
  Integer ln = valueOf(XLEN);
  Integer ln2 = valueOf(x2len);
  Bit#(6) shamt = rs2[5:0];
  if(ln == 32)
    shamt[5] = 0;
  Bit#(XLEN) zeros = 0;
  Bit#(x2len) x = {rs1,zeros} >> shamt;
  Bit#(XLEN) result = x[ln2-1:ln] | x[ln-1:0];
  return result;
endfunction

function Bit#(XLEN) fn_rorw(Bit#(XLEN) rs1, Bit#(XLEN) rs2); // Rotate Right Word (Register)
  Bit#(32) zeros = 0; 
  Integer ln = valueOf(XLEN);
  Bit#(5) shamt = rs2[4:0];
  Bit#(64) x = {rs1[31:0],zeros} >> shamt;
  Bit#(32) w = x[63:32]|x[31:0];
  Bit#(XLEN) result = rs1;
  Integer i = 0;
  for(i = 0; i < 32; i = i + 1)
    result[i] = w[i];
  for(i = 32; i < ln; i = i + 1)
    result[i] = w[31];
  return result;
endfunction


function Bit#(XLEN) fn_orcb(Bit#(XLEN) rs1); // Bitwise OR-Combine, byte granule
  let ln = valueOf(XLEN);
  Bit#(XLEN) result = 0;
  Integer i = 0;
  for(i = 0; i < ln; i = i + 8) begin
    Bit#(8) dbyte = rs1[i+7:i];
    Bit#(1) isSet = |(dbyte);
    Bit#(8) newbyte = 0;
    if(isSet == 1)
      newbyte = 255;
    result[i+7:i] = newbyte;
  end
  return result;
endfunction

function Bit#(XLEN) fn_rev8(Bit#(XLEN) rs1); // Byte-reverse register
  let xlen = valueOf(XLEN);
  Bit#(XLEN) result = 0;
  Integer j = xlen-1;
  Integer i = 0;
  for(i = 0; i < xlen; i = i + 8) begin
    Bit#(8) dbyte = rs1[j:j-7];
    result[i+7:i] = dbyte;
    j = j - 8;
  end
  return result;
endfunction