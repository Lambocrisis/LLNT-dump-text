# LLNT-dump-text

*Lilja and Natsuka Painting Lies*' dumped text.

[简体中文](README.md) | [English](README-en.md)

## dump

The game uses the **krkrz** engine. [krkrDump](https://github.com/crskycode/KrkrDump) can be used to extract game resources as the game progresses, including `.ks` scripts, character voices and background music, fonts, background images, character portraits, etc. The game script is stored as `.ks.scn` (e.g. the file name `scn00_01.ks.scn` is the first paragraph of the prologue.)

[FreeMote](https://github.com/UlyssesWu/FreeMote) can be used to decompile `.ks.scn` into `ks.json` files. After opening, you can jump to the keyword `texts` to read the in-game text.

## parse

Use the modified [KiriKiriSCNJSONParser](https://github.com/HoodedTissue/KiriKiriSCNJSONParser) to parse `.ks.json` into a more readable `.txt` text.

The modified `parser.py` is put in `dump-ks.json`. After running, a `parsed` folder will be automatically generated in the same directory, and the parsed `.txt` file will be stored in it. For easy viewing, it has been placed in the external `script` folder.

The modified parts are as follows:

1. Since the structure of `.ks.json` of *LLNT* is different, the following code is added to read the character name and lines respectively and adjust the format:

    ```python
    def process(text):

    name0 = str(text[0])

    name1 = str(text[1][0][0])

    if name1 == "None":
    name1 = str(text[0])
    stc1 ​​= str(text[1][0][1])

    name2 = str(text[1][1][0])

    if name2 == "None":
    name2 = str(text[0])
    stc2 = str(text[1][1][1])

    name3 = str(text[1][2][0])

    if name3 == "None":
    name3 = str(text[0])
    stc3 = str(text[1][2][1])

    return name0 + '\n' + name1 + " : " + stc1+'\n' + name2+ " : " + stc2+'\n' + name3 + " : " + stc3 + '\n'
    ```

    There are also changes in line 41: add a line `rslt = process(scns)`, and replace `scns` in the original `createFile.write(scns + "\n")` below with `rslt`.

2. It would originally add `.txt` directly after the file name, which made it a bit lengthy, so it was changed to delete the original extension first and then add `.txt`.

## to do

1. My personal game progress has reached the end of Chapter 3, and the remaining content is to be completed.

## special thanks

- [Yazawazi](https://yazawazi.moe/)
- [拾壹Tymen](https://space.bilibili.com/486926861)
