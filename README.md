# Extractor
This is a super simple python utility that will extract all the individual sprites from a tiled spritesheet.

## Example
There is an example png tileset file that comes from the free Kenney 2d asset pack.

![Kennys art assets](example.png)

Here are some examples of extracted images.

![image1](extract/0_4.png)
![image1](extract/0_5.png)
![image1](extract/0_7.png)
![image1](extract/0_8.png)

## Required Installs
This uses python3 and the python imaging library (PIL).  PIL can be installed via pip.

## Execution

```
python3 extractor.py <image_path> <x_size_tile> <y_size_tile>

python3 extractor.py pic.png 16 16
```

Note that all old files are deleted on each run and new files are put into the extract folder.