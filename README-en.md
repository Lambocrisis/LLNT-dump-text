# LLNT-dump-text

*Lilja and Natsuka Painting Lies*' dumped text.

[简体中文](README.md) | [English](README-en.md)

## dump

The game uses the krkrz engine. [krkrDump](https://github.com/crskycode/KrkrDump) can be used to extract game resources as the game progresses, including `.ks` scripts, character voices and background music, fonts, background images, character portraits, etc. The game script is stored as `.ks.scn` (e.g. the file name `scn00_01.ks.scn` is the first paragraph of the prologue.)

[FreeMote](https://github.com/UlyssesWu/FreeMote) can be used to decompile `.ks.scn` into `ks.json` files. After opening, you can jump to the keyword `texts` to read the in-game text.

## to do

1. My personal game progress has reached the end of Chapter 3, and the remaining content is to be completed.
2. It is expected to use [KiriKiriSCNJSONParser](https://github.com/HoodedTissue/KiriKiriSCNJSONParser) to parse `.json` into a more readable `.txt` text.
