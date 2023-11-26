# DOA6
Modified binaries for Dead Or Alive 6 (Steam)


# Modified const & patterns

*Patching constant*
Modify const 3FE38E39 in doa6.exe module

mov qword ptr ds:[rcx+14C],3FE38E39

replace the Hex data with:

48 C7 81 4C 01 00 00 8E E3 18 40   | for 3440x1440, or

48 C7 81 4C 01 00 00 26 B4 17 40   | for 2560x1080

For the secound search result. 
00007FF6FF095399 | Disassembly: mov dword ptr ds:[rdi+1268],3FE38E39; 

replace the Hex data with:

C7 87 68 12 00 00 8E E3 18 40 for 3440x1440, or

C7 87 68 12 00 00 26 B4 17 40 for 2560x1080

Patching from pattern

Search this Hex pattern: C7 44 ?? ?? 80 07 ?? ?? ?? ?? ?? ?? ?? ?? ?? ??. | in doa6.exe module, still not in ntdl or whatever

There'll be about 5 results. 

C7 44 ** ** 80 07. 
The 80 07 is what we need to change to:

14 0A for 3440x1440, or

00 0A for 2560x1080

for example, C7 44 24 28 80 07 00 00 becomes C7 44 24 28 14 0A 00 00.


*Patching jmp rcx*

Search for the pattern FF E1 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? C7 44 24 30 ?? ?? 00 00 C7 44 24 34 ?? ?? 00 00. Still in doa6.exe module. not main thread.
There'll be one result:

00007FF6FEE80F7C | Disassembly: jmp rcx

Binary > Fill with NOPs and select OK.

Then, look carefully at the highlighted row. A few addresses underneath it, there'll be a row with mov dword ptr ss:[rsp+30],320. Select that row, and then Edit it (ctrl+e); we need to change from C7 44 24 30 20 03 00 00 to:

C7 44 24 30 70 0D 00 00 for 3440x1440, or

C7 44 24 30 00 0A 00 00 for 2560x1080

Then, underneath that row there'll be another row with mov dword ptr ss:[rsp+34],1C2. Select that row, and then Edit it (ctrl+e); we need to change from C7 44 24 34 C2 01 00 00 to:

C7 44 24 34 A0 05 00 00 for 3440x1440, or

C7 44 24 34 38 04 00 00 for 2560x1080

Those rows from step 3 and 4 should now end with D70 and 5A0 or A00 and 438 instead of 320 and 1C2 respectively and depending on your resolution choice.

# Credits


Huge thanks to
https://www.wsgf.org/phpBB3/viewtopic.php?f=64&t=33019 (jackfuste post)
and
https://www.reddit.com/r/widescreengamingforum/comments/12t9w60/dead_or_alive_6_v122a_ultrawide_hack/
