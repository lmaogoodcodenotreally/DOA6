# Dead or Alive 6, 21:9 fix + reduced size
**Modified binaries for Dead Or Alive 6 (Steam)**
> **Note:**
> I am aware that the patch only works during gameplay. It should not significantly affect anything in the MainMenu (except for low resolution, of course).
> Config Tool is useful ONLY if you have a steam_emu.
 

*Disclaimer:
This is not the complete game but an unpacked version of `DOA6.exe`. It is essential to own a valid DOA6 copy for this to work.
I do not take responsibility for the usage of this .exe.
Its sole purpose is to modify the internal aspect ratio from `16:9` to `21:9` for widescreen support, as well as reducing executable size, all rights belongs to KOEI TECMO GAMES CO. LTD.
Please refrain from redistributing without linking to this repository or previous threads, it's crucial for individuals to create their own game patch if they choose to do so.
I have limited knowledge of copyright matters, and I'm indifferent, but please avoid reusing this without referencing the sources.
If you plan to create a patch yourself, check the credits; the Reddit thread contains the most up-to-date patterns.*



# Installation

Default steam path `C:\Program Files (x86)\Steam\steamapps\common\Dead or Alive 6\`
- Simply open game folder then locate and backup your `DOA6.exe`.
- Download the version you want for your game [here](https://github.com/lmaogoodcodenotreally/DOA6/releases/latest)

- Then place `DOA6-{version}.exe` to your game folder, rename it to `DOA6.exe` and run it.
`DOA6-low-res.exe` for low resolution executable and `DOA6-3440x1440.exe` for `3440x1440 21:9`

If you encouter any errors, open Steam and go to `Dead or Alive 6` right click for `Propreties > Installed Files > Verify integrity of game files`
Or just backup your original `DOA6.exe`.
Never got issue with it and I don't think any update will ever release again for the game so you're fine using this if you install it proprely.



# Unpacking&Repacking

- Unpacked SteamStub 3.1.x (using Steamless)
- Modified Assembly (x64dbg)
- Repacked with UPX (upx)
```
        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
  44227728 ->  13027984   29.46%    win64/pe     DOA6.exe                                                            
Packed 1 file.


Removed: 29.8 MB
```

# Modified const & patterns

**Patching constant**

Modify `const 3FE38E39` in `doa6.exe` module

```assembly
mov qword ptr ds:[rcx+14C],3FE38E39
```
replace the Hex data with:
```assembly
48 C7 81 4C 01 00 00 8E E3 18 40   | for 3440x1440, or
48 C7 81 4C 01 00 00 26 B4 17 40   | for 2560x1080
```
For the secound search result. 
```assembly
00007FF6FF095399 | Disassembly: mov dword ptr ds:[rdi+1268],3FE38E39; 
```
replace the Hex data with:
```assembly
C7 87 68 12 00 00 8E E3 18 40 for 3440x1440, or
C7 87 68 12 00 00 26 B4 17 40 for 2560x1080
```
Patching from pattern
`(CTRL+SHIFT+B)` Search this Hex pattern: 
```assembly
C7 44 ?? ?? 80 07 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? 
```
in doa6.exe module.
There'll be about 5 results. 
```assembly
C7 44 ** ** 80 07.
``` 
The `80 07` is what we need to change to:
```assembly
14 0A for 3440x1440, or

00 0A for 2560x1080
```
for example, 
```assembly 
C7 44 24 28 80 07 00 00 
```
becomes 
```assembly 
C7 44 24 28 14 0A 00 00.
```

**Patching jmp rcx**

`(CTRL+SHIFT+B)` Search for the pattern:
```assembly
FF E1 ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? ?? C7 44 24 30 ?? ?? 00 00 C7 44 24 34 ?? ?? 00 00
```
*Still in doa6.exe module. not main thread.*
There'll be one result:
```assembly
00007FF6FEE80F7C | Disassembly: jmp rcx
```
**Binary > Fill with NOPs and select OK.**

Then, look carefully at the highlighted row. A few addresses underneath it, there'll be a row with:
```assembly
mov dword ptr ss:[rsp+30],320
```
Select that row, and then Edit it `(CTRL+E)`; we need to change from:
```assembly
C7 44 24 30 20 03 00 00 
```
to:
```assembly
C7 44 24 30 70 0D 00 00 for 3440x1440, or
C7 44 24 30 00 0A 00 00 for 2560x1080
```
Then, underneath that row there'll be another row with 
```assembly
mov dword ptr ss:[rsp+34],1C2
```
Select that row, and then Edit it `(CTRL+E)`; we need to change from:
```assembly
C7 44 24 34 C2 01 00 00
```
to:
```assembly
C7 44 24 34 A0 05 00 00 for 3440x1440, or
C7 44 24 34 38 04 00 00 for 2560x1080
```
Those rows from step 3 and 4 should now end with `D70` and `5A0` or `A00` and `438` instead of `320` and `1C2` respectively and depending on your resolution choice.

# Credits


Huge thanks to
https://www.wsgf.org/phpBB3/viewtopic.php?f=64&t=33019 (jackfuste post)
and
https://www.reddit.com/r/widescreengamingforum/comments/12t9w60/dead_or_alive_6_v122a_ultrawide_hack/
