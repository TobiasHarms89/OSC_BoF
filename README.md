# OSC_BoF
This Rep describes my steps for BoF. 


1. To find the EIP offset net to create a pattern with msfvenom 

 /usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2100 > exploit.txt
 -> check the EIP value: example EIP: 43346943
 then use command to find out the offset: 
 /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2100 -q 42367242
 additional step:  /usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2100 -q Aa0A (first 4 chars of offset to find how many chars until ESP)
 offset = 1812, -> need to fill until then with 1812 Chars
 1. Step in code: #buf = b"A" * OFFSET #junk get to EIP

2. Find bad Characters, send all chars, in hex to File and filter out bad ones: 
3. find a jmp ESP instruction in code, so that we can put in our shellcode 
4. use mona !mona jmp -r esp -cpb "\x00\x1a" use jump esp instruction. 
