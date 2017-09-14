# PiskellToVerilog
## Usage
```Bash
python3 path/to/piskell/file/ > path/to/output/file
```
The Piskell file must be one that has been exported as a C file, one of the many save options given on the site. The output will be a full multidimensional register array that can be copied into
Verilog and used as such.
If output is headed to a VGA display with base pointers hbp and vbp along with current coordinates hc and vc, for example, getting the current pixel would look like this (the array is upside down):
```Verilog
currSprite = currArray[(currArrayHeight*currArray-1) - (((vc - vbp - currSpriteY) * currArrayWidth) + ((hc - hbp - currSpriteX)))];
```
where the currArray values are given in the output file.
