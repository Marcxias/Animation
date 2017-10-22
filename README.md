# Animation

> 本项目从我（[@Wolther47](https://github.com/wolther47)）的 [Bangumi](https://github.com/wolther47/Bangumi) 项目分离

这是一个非常简单的项目，主要目的只有一个：**从 Wikipedia 上将从 2009 年开始的每年的番剧爬取，并以 Json 的形式保存**。

## TODO

- [ ] ~~利用 Wikitables 项目获取表格~~
- [ ] ~~繁简体转换~~
- [ ] ~~匹配 Template 正则~~
- [x] 完成主要功能
  - [x] 解析 Table
  - [x] 解析 Row
  - [x] 解析 Text
- [ ] 持续集成

## 踩坑

项目一开始带歪了方向，用了 MediaWiki 的 API，结果发现：

1. 似乎没有 zh_CN 的 API，只有繁体；
2. 使用 OpenCC 项目后，解析出的表格，由于是繁体，会有 Wiki 的 Template，指定特定的繁简转换，这部分使用正则也比较难处理，重点是，Wikipedia 的维护人员没有统一标准，没法写出形式化定义；

睡了一觉，起来后，发现，还不如直接使用 BS4 拆页面

## 协议

所有采集得来的 Json 文件，采用同维基百科相同的 [CC BY-SA 3.0 协议](https://zh.wikipedia.org/zh-cn/Wikipedia%3ACC_BY-SA_3.0%E5%8D%8F%E8%AE%AE%E6%96%87%E6%9C%AC)开源