---
date:
  created: 2025-01-24
---

# 在灯塔自评、互评系统整活

首先指路[灯塔系统学生端](https://student.lighthouse.ren)。

有些学校会用这玩意在期末让学生写“综合素质评价”：自评和互评，用于音乐、美术、体育、品德等科目，来生成成绩报告单。互评时只能给同学打 A、B、C 等级，自评的时候则既可以打等级，还可以写文字评价。

然而灯塔系统的 bug 就在于，文字评价内容中可以输入 HTML 文本，所以理论上你就可以打出<b style="color:#339900;font-weight:400">各</b><b style="color:#009999;font-weight:400">种</b><b style="color:#0099ff;font-weight:400">颜</b><b style="color:#6666ff;font-weight:400">色</b><b style="color:#9900ff;font-weight:400">的</b>、<b style="font-weight:300">各</b><b style="font-weight:400">种</b><b style="font-weight:500">粗</b><b style="font-weight:700">细</b><b style="font-weight:800">的</b>、<b style="font-size:0.6em;font-weight:400">各</b><b style="font-size:0.9em;font-weight:400">种</b><b style="font-size:1.2em;font-weight:400">大</b><b style="font-size:1.4em;font-weight:400">小</b><b style="font-size:1.6em;font-weight:400">的</b>文字，甚至还可以是……  

<!-- more -->

<marquee style="width:4em">滚动屏</marquee>  

……以及非文本内容！如果你技术高超（且勇气可嘉），你还可以插入其它东西，比如图片、视频、放首歌。

就只剩学 HTML 的事情了。

<!-- TODO

## 进阶版本

还能玩得再离谱一些吗？

比如……强迫同学给你打 A 等级？

-->
