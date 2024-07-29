# LLNT-dump-text

《丽露娅与夏夏的纯白谎言》文本提取。*Lilja and Natsuka Painting Lies*' dumped text.

## dump

游戏使用了 krkrz 引擎，用 [krkrDump](https://github.com/crskycode/KrkrDump) 可以随游戏进度将游戏资源提取出来，包括 .ks 脚本，角色语音和背景音乐，字体，背景图片，角色立绘等。其中游戏剧本（脚本）是以 .ks.scn 的形式存储的（示例：文件名 `scn00_01.ks.scn` 是序章的第一段。）

通过 [FreeMote](https://github.com/UlyssesWu/FreeMote) 可以将 .ks.scn 反编译为 ks.json 文件，打开后可以跳转至关键词 texts 处阅读游戏内文本。

## to do

1. 目前我个人的游戏进度推到第三章结束，剩余内容待补全。
2. 预计用 [KiriKiriSCNJSONParser](https://github.com/HoodedTissue/KiriKiriSCNJSONParser) 将 .json 解析成更易读的 .txt 文本。
