xpath是在xml文档中搜索内容的一种语言
html是xml的一个子集
# xpath的语法介绍
1from lxml import etree
tree=etree.parse(xml)
result=tree.xpath("")

/表示层级关系，/(第一个)表示根目录
使用text（）拿文本
//表示后代
*表示任意的节点

另外在页面源代码中，使用开发者工具可以查询某一位置的xpath，十分方便