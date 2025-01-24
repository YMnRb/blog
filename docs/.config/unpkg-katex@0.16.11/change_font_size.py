# change KaTeX font sizes into each devided by `shrink`

import re
file = open('D:/C++/Dev/mkdocs-site/docs/.config/unpkg-katex@0.16.11/katex.min.css', 'r', encoding="utf-8")
new_file = open('D:/C++/Dev/mkdocs-site/docs/.config/unpkg-katex@0.16.11/katex.min.custom.css', 'w', encoding="utf-8")
css = file.read()
file.close()
shrink = 1.1

# 处理没有整数部分的纯小数
# matched = re.findall(r'(?<![0123456789])\.\d+em', css)
# for each in sorted(set(matched)):
# 	css = css.replace(each, '0'+each)
f = open('D:/C++/Dev/mkdocs-site/docs/.config/unpkg-katex@0.16.11/a.css', 'w')
f.write(css)
f.close()

# 为了防止类似 `1.2em` 中的 `2em` 被替换，出现类似 `1.1.8181818181818181em` 的情况
# 特别情况特别对待
css = css.replace('{font-size:1em}', '{font-size:1.0em}')
css = css.replace('margin:1em 0', 'margin:1.0em 0')
css = css.replace('{font-size:2em}', '{font-size:2.0em}')
css = css.replace('padding-left:2em', 'padding-left:2.0em')

# 使字体大小变为原来的 \frac{1}{\tt{shrink}}
matched = re.findall(r'[-0123456789.]+(?=em)', css)
matched = sorted(set(matched))
matched.reverse()
for each in matched:
	css = css.replace(each+'em', str(float(each)/shrink)+'@#!em')

matched = re.findall(r'0\.\d+@#!em', css)
for each in sorted(set(matched)):
	css = css.replace(each, each[1:])

new_file.write(css.replace('@#!em', 'em'))
new_file.close()