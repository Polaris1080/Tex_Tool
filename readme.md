# Tex_Tool

Tex_Tool can Bond/Unbond/Frip/Mirror/Convert texture without opening image editing software

## Description

### Until now

Editing texture need to open image editing software,
and also took time and effort.

### Now

This tool can quickly edit textures, as long as you register.

## VS

### case1 Bond

**software** # launch:40s + setting:40s*3 + save:20s = 180s  
**tool** # edit:40s + use:5s = 45s  

### case2 UnBond

**software** # launch:30s + use:30s + save:30s*3 = 150s  
**tool** # edit:40s + use:5s = 45s  

### case3 frip

**Frip all channel** # launch:30s + flip:10s + save:20s = 60s  
**Frip only-one channel** # launch:30s + select:15s + flip:10s + save:20s = 75s  
**Using tool** # edit:55s + use:5s = 60s (Can batch processing)  

## Requirement

- python3
- PIL
- pandas(Replaceable csv)

## Usage

XXX = using-tool name

1. edit XXX.csv.
2. run XXX.bat, or "python XXX.py".
3. select XXX.csv location. (if no input, use default 'XXX.csv')

## Install

1. "git clone git://github.com/schacon/grit.git"
2. Click 'Colne or Download', Download zip, unzip this.

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[Polaris1080](https://github.com/Polaris1080)
