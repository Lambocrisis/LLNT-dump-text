# LLNT-dump-text

《丽露娅与夏夏的纯白谎言》文本提取。*Lilja and Natsuka Painting Lies*' dumped text.

[简体中文](README.md) | [English](README-en.md)

## dump

游戏使用了 **krkrz** 引擎，用 [krkrDump](https://github.com/crskycode/KrkrDump) 可以随游戏进度将游戏资源提取出来，包括 `.ks` 脚本，角色语音和背景音乐，字体，背景图片，角色立绘等。其中游戏剧本（脚本）是以 `.ks.scn` 的形式存储的（示例：文件名 `scn00_01.ks.scn` 是序章的第一段。）

通过 [FreeMote](https://github.com/UlyssesWu/FreeMote) 可以将 `.ks.scn` 反编译为 `.ks.json` 文件，打开后可以跳转至关键词 `texts` 处阅读游戏内文本。

## parse

使用修改后的 [KiriKiriSCNJSONParser](https://github.com/HoodedTissue/KiriKiriSCNJSONParser) 将 `.ks.json` 解析成更易读的 `.txt` 文本。

修改后的 `parser.py` 放在 `dump-ks.json` 中，运行后会自动在同一目录下生成 `parsed` 文件夹，在其中存入解析好的 `.txt` 文件。为方便查看，这里已经将其放在外面的 `script` 文件夹中。

修改部分如下：

1. 由于《纯白谎言》的 `.ks.json` 的结构不太一样，这边加入了这样的代码以分别读取角色名称和台词并调整格式：

    ```python
    def process(text):
    
        name0 = str(text[0])

        name1 = str(text[1][0][0])
        if name1 == "None":
            name1 = str(text[0])
        stc1 = str(text[1][0][1])

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

    同时，在 41 行处也有改动：加入一行 `rslt = process(scns)`，并将下方原本 `createFile.write(scns + "\n")` 中的 `scns` 替换成 `rslt`。

2. 原本直接在文件名后面加 `.txt` 有点冗长，改成了先删去原本的拓展名再加 `.txt`。

## to do

目前我个人的游戏进度推到第三章结束，剩余内容待补全。

## 特别感谢

- [Yazawazi](https://yazawazi.moe/)
- [拾壹Tymen](https://space.bilibili.com/486926861)
